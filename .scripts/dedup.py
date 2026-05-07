"""SimHash-basierte Dedup. Hamming-Distance <= 3 -> dupliert, n_sources counter erhoeht.

Nutze `simhash` Package (Charikar-Algorithmus, 64-bit).
"""

from __future__ import annotations

from typing import Any

from simhash import Simhash


def item_hash(item: dict[str, Any]) -> int:
    """Berechnet SimHash auf title + url + body[:200]."""
    parts = [
        item.get("title", ""),
        item.get("url", ""),
        (item.get("body") or item.get("summary") or "")[:200],
    ]
    return Simhash(" ".join(parts), f=64).value


def hamming_distance(a: int, b: int) -> int:
    return bin(a ^ b).count("1")


def dedup(items: list[dict[str, Any]], threshold: int = 3) -> list[dict[str, Any]]:
    """Sortiert duplicate Items zusammen, erhoeht n_sources, behaelt hoechstes source_trust.

    Returns: dedupte Items mit `n_sources` und `source_ids` (Liste der Original-Quellen).
    """
    canonical: list[dict[str, Any]] = []
    canonical_hashes: list[int] = []

    for item in items:
        h = item_hash(item)
        merged = False
        for i, ch in enumerate(canonical_hashes):
            if hamming_distance(h, ch) <= threshold:
                canonical[i]["n_sources"] = canonical[i].get("n_sources", 1) + 1
                canonical[i].setdefault("source_ids", [canonical[i].get("source_id")])
                if item.get("source_id") not in canonical[i]["source_ids"]:
                    canonical[i]["source_ids"].append(item.get("source_id"))
                # behalte hoechstes trust
                if item.get("source_trust", 0) > canonical[i].get("source_trust", 0):
                    canonical[i]["source_trust"] = item["source_trust"]
                merged = True
                break
        if not merged:
            new_item = dict(item)
            new_item.setdefault("n_sources", 1)
            new_item.setdefault("source_ids", [item.get("source_id")])
            canonical.append(new_item)
            canonical_hashes.append(h)

    return canonical
