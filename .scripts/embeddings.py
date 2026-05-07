"""Self-hosted bge-m3 Embeddings via Ollama localhost.

Persistenter Cache in .state/embeddings.sqlite damit nur Delta-Items neu embedded werden.
"""

from __future__ import annotations

import hashlib
import json
import os
import sqlite3
from pathlib import Path

import requests

REPO_ROOT = Path(__file__).resolve().parent.parent
EMBEDDINGS_DB = REPO_ROOT / ".state" / "embeddings.sqlite"

ENDPOINT = os.environ.get("EMBEDDINGS_ENDPOINT", "http://localhost:11434/api/embeddings")
MODEL = os.environ.get("EMBEDDINGS_MODEL", "bge-m3")


def _init_db() -> sqlite3.Connection:
    EMBEDDINGS_DB.parent.mkdir(exist_ok=True)
    conn = sqlite3.connect(str(EMBEDDINGS_DB))
    conn.execute(
        "CREATE TABLE IF NOT EXISTS embeddings ("
        "  text_hash TEXT PRIMARY KEY,"
        "  vector_json TEXT NOT NULL,"
        "  model TEXT NOT NULL,"
        "  created_at TEXT NOT NULL"
        ")"
    )
    conn.commit()
    return conn


def text_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:32]


def get_cached(conn: sqlite3.Connection, h: str) -> list[float] | None:
    cur = conn.execute("SELECT vector_json FROM embeddings WHERE text_hash = ? AND model = ?", (h, MODEL))
    row = cur.fetchone()
    if row:
        return json.loads(row[0])
    return None


def put_cached(conn: sqlite3.Connection, h: str, vec: list[float]) -> None:
    from datetime import datetime, timezone
    conn.execute(
        "INSERT OR REPLACE INTO embeddings(text_hash, vector_json, model, created_at) VALUES(?, ?, ?, ?)",
        (h, json.dumps(vec), MODEL, datetime.now(timezone.utc).isoformat()),
    )
    conn.commit()


def embed(text: str) -> list[float]:
    """Embed einzelnen Text via Ollama. Cached.

    Returns leere Liste falls Ollama nicht erreichbar (Caller muss Heuristik-Fallback nutzen).
    """
    conn = _init_db()
    h = text_hash(text)
    cached = get_cached(conn, h)
    if cached is not None:
        return cached
    try:
        resp = requests.post(
            ENDPOINT,
            json={"model": MODEL, "prompt": text},
            timeout=30,
        )
        resp.raise_for_status()
        vec = resp.json().get("embedding", [])
        if vec:
            put_cached(conn, h, vec)
        return vec
    except (requests.RequestException, ValueError) as e:
        print(f"[embeddings] WARN: ollama call failed for hash={h[:8]}: {e}")
        return []


def embed_batch(texts: list[str]) -> list[list[float]]:
    """Sequenzielle Embeddings (Ollama hat kein Batch-Endpoint per default)."""
    return [embed(t) for t in texts]


def cosine_similarity(a: list[float], b: list[float]) -> float:
    if not a or not b:
        return 0.0
    dot = sum(x * y for x, y in zip(a, b, strict=False))
    norm_a = sum(x * x for x in a) ** 0.5
    norm_b = sum(y * y for y in b) ** 0.5
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


def kmeans_cluster(vectors: list[list[float]], k: int = 10, max_iter: int = 50) -> list[int]:
    """Simple k-means. Returns Cluster-ID pro Vektor.

    Bei k > len(vectors) wird k auf len(vectors) geclamped.
    Falls Vectors leer (Embeddings-Service down): returns Liste mit Cluster 0 fuer alle.
    """
    import random

    if not vectors or all(not v for v in vectors):
        return [0] * len(vectors)
    valid = [v for v in vectors if v]
    if not valid:
        return [0] * len(vectors)
    k = min(k, len(valid))

    centroids = random.sample(valid, k)

    def closest_centroid(v: list[float]) -> int:
        best_i, best_sim = 0, -1.0
        for i, c in enumerate(centroids):
            sim = cosine_similarity(v, c)
            if sim > best_sim:
                best_sim, best_i = sim, i
        return best_i

    assignments = [closest_centroid(v) if v else 0 for v in vectors]

    for _ in range(max_iter):
        new_centroids: list[list[float]] = []
        for i in range(k):
            cluster_vecs = [vectors[j] for j, a in enumerate(assignments) if a == i and vectors[j]]
            if not cluster_vecs:
                new_centroids.append(centroids[i])
                continue
            dim = len(cluster_vecs[0])
            mean = [sum(v[d] for v in cluster_vecs) / len(cluster_vecs) for d in range(dim)]
            new_centroids.append(mean)
        new_assignments = [closest_centroid(v) if v else 0 for v in vectors]
        if new_assignments == assignments:
            break
        assignments = new_assignments
        centroids = new_centroids

    return assignments
