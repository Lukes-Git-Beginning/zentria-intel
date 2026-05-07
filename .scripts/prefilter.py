"""LLM-freier Pre-Filter. Spam-Regex, KMU-Irrelevanz, Marketing-Pure-Push.

Konfiguration aus settings.yaml geladen.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
SETTINGS_FILE = REPO_ROOT / "settings.yaml"


def load_prefilter_rules() -> dict[str, list[re.Pattern]]:
    with SETTINGS_FILE.open(encoding="utf-8") as f:
        settings = yaml.safe_load(f)
    raw = settings.get("prefilter", {})
    return {
        "spam": [re.compile(p) for p in raw.get("spam_regex", [])],
        "kmu_irrelevance": [re.compile(p) for p in raw.get("kmu_irrelevance", [])],
        "marketing_pure_push": [re.compile(p) for p in raw.get("marketing_pure_push", [])],
    }


_RULES_CACHE: dict[str, list[re.Pattern]] | None = None


def _get_rules() -> dict[str, list[re.Pattern]]:
    global _RULES_CACHE
    if _RULES_CACHE is None:
        _RULES_CACHE = load_prefilter_rules()
    return _RULES_CACHE


def is_spam(item: dict[str, Any]) -> bool:
    rules = _get_rules()
    haystack = " ".join(filter(None, [item.get("title"), item.get("summary", "")[:300]]))
    return any(p.search(haystack) for p in rules["spam"])


def is_kmu_irrelevant(item: dict[str, Any]) -> bool:
    rules = _get_rules()
    haystack = item.get("title", "")
    return any(p.search(haystack) for p in rules["kmu_irrelevance"])


def is_marketing_push(item: dict[str, Any]) -> bool:
    rules = _get_rules()
    haystack = item.get("title", "")
    return any(p.search(haystack) for p in rules["marketing_pure_push"])


def keep(item: dict[str, Any], muted_sources: set[str] | None = None) -> tuple[bool, str | None]:
    """Returns (keep_item, reason_if_filtered).

    reason ist None falls keep_item True ist.
    """
    if muted_sources and item.get("source_id") in muted_sources:
        return False, "muted_source"
    if is_spam(item):
        return False, "spam"
    if is_kmu_irrelevant(item):
        return False, "kmu_irrelevant"
    if is_marketing_push(item):
        return False, "marketing_push"
    title = item.get("title", "")
    if len(title.split()) <= 5 and not item.get("modul_match_keywords"):
        return False, "too_short_no_keywords"
    return True, None


def filter_items(items: list[dict[str, Any]], muted_sources: set[str] | None = None) -> tuple[list[dict[str, Any]], dict[str, int]]:
    """Filtert eine Item-Liste, gibt (kept, stats) zurueck.

    stats: counts pro reason
    """
    kept: list[dict[str, Any]] = []
    stats: dict[str, int] = {}
    for item in items:
        ok, reason = keep(item, muted_sources)
        if ok:
            kept.append(item)
        else:
            stats[reason or "unknown"] = stats.get(reason or "unknown", 0) + 1
    return kept, stats


# Heuristisches Pre-Score (kein LLM)

def pre_score(item: dict[str, Any], target_modules: list[str] | None = None) -> float:
    """Score = module_match * source_trust * recency_decay * (1 + 0.2*n_sources) * competitor_directness.

    Returns Wert zwischen 0 und ~10. Hoeher = wichtiger.
    """
    from datetime import datetime, timezone

    # source_trust 0-10
    trust = item.get("source_trust", 5) / 10.0

    # module_match: 1.0 falls modul direkt in target, 0.7 falls verwandt, 0.3 sonst
    if target_modules:
        if any(m in (item.get("modules") or []) for m in target_modules):
            mod = 1.0
        else:
            mod = 0.4
    else:
        mod = 1.0

    # recency_decay: ueber 7 Tage halbiert sich der Wert
    pub = item.get("published_at")
    if pub:
        try:
            pub_dt = datetime.fromisoformat(pub.replace("Z", "+00:00"))
            age_days = (datetime.now(timezone.utc) - pub_dt).total_seconds() / 86400
            recency = max(0.1, 0.95**age_days)
        except (ValueError, TypeError):
            recency = 0.5
    else:
        recency = 0.5

    n_sources = item.get("n_sources", 1)
    cluster_bonus = 1.0 + 0.2 * (n_sources - 1)

    competitor_direct = 1.5 if item.get("competitor_threat") == "high" else 1.0

    return trust * mod * recency * cluster_bonus * competitor_direct
