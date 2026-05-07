"""Quellen-Adapter fuer zentria-intel.

Jeder Adapter hat eine `fetch(source_config, since_iso=None) -> list[Item]`-Funktion.
Item-Schema:
    {
        "source_id": str,          # aus YAML-Config
        "source_trust": int,        # 0-10 aus YAML
        "title": str,
        "url": str,
        "summary": str | None,
        "body": str | None,         # falls extrahiert
        "published_at": str (ISO),
        "modules": list[str],       # gefuellt vom Caller via YAML-Mapping
    }
"""
