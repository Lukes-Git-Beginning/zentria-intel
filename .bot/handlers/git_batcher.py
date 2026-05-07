"""Git-Batcher: 60s-Window-Queue fuer gepickte Files -> commit + push."""
from __future__ import annotations

import asyncio
import logging
import os
from pathlib import Path

import git

log = logging.getLogger("intel-bot.git")
REPO_ROOT = Path("/app")
_GIT_LOCK = asyncio.Lock()


async def flush_loop(queue: asyncio.Queue, window_seconds: int = 60) -> None:
    """Sammelt Tuples (filepath, action, msg) fuer window_seconds, dann flush."""
    while True:
        await asyncio.sleep(window_seconds)
        if queue.empty():
            continue
        await flush_all(queue)


async def flush_all(queue: asyncio.Queue) -> None:
    """Leert Queue sofort — auch beim Shutdown aufrufbar."""
    items: list[tuple[str, str, str]] = []
    while not queue.empty():
        try:
            items.append(queue.get_nowait())
        except asyncio.QueueEmpty:
            break
    if not items:
        return
    async with _GIT_LOCK:
        await asyncio.get_event_loop().run_in_executor(
            None, _sync_flush, items
        )


def _sync_flush(items: list[tuple[str, str, str]]) -> None:
    """Synchrone Git-Operationen (laeuft im Thread-Pool)."""
    try:
        repo = git.Repo(str(REPO_ROOT))
        _configure_git_identity(repo)
        # Dedup Pfade — derselbe Index-File kann mehrfach in der Queue sein
        seen: set[str] = set()
        filepaths = []
        for fp, _action, _msg in items:
            if fp not in seen:
                filepaths.append(fp)
                seen.add(fp)
        repo.index.add(filepaths)
        n = len(items)
        commit_msg = f"feat(intel): batch picks ({n} item{'s' if n != 1 else ''})"
        repo.index.commit(commit_msg)
        log.info("Committed: %s", commit_msg)
        _push_with_retry(repo)
    except git.exc.GitCommandError as e:
        log.error("Git-Fehler beim Batch-Flush: %s", e)
    except Exception:
        log.exception("Unerwarteter Fehler im git_batcher")


def _push_with_retry(repo: git.Repo) -> None:
    """Push mit einmaligem Rebase-Retry bei Conflict."""
    try:
        origin = repo.remote("origin")
        origin.push()
        log.info("Git push erfolgreich")
    except git.exc.GitCommandError as e:
        msg = str(e)
        if "rejected" in msg or "non-fast-forward" in msg:
            log.warning("Push rejected — versuche pull --rebase")
            try:
                repo.git.pull("--rebase", "origin", repo.active_branch.name)
                repo.remote("origin").push()
                log.info("Push nach Rebase erfolgreich")
            except git.exc.GitCommandError:
                log.error("Push nach Rebase fehlgeschlagen — manuell pruefen")
        else:
            log.error("Push-Fehler (kein Rebase-Kandidat): %s", e)


def _configure_git_identity(repo: git.Repo) -> None:
    user_email = os.environ.get(
        "GITHUB_USER_EMAIL", "intel-bot@zentria.local"
    )
    user_name = os.environ.get("GITHUB_USER_NAME", "zentria-intel-bot")
    with repo.config_writer() as cw:
        cw.set_value("user", "email", user_email)
        cw.set_value("user", "name", user_name)
