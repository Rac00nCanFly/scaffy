from pathlib import Path
import subprocess
import shutil
import logging

logger = logging.getLogger(__name__)

def git_init(project_dir : Path) -> None:
    project_dir.mkdir(parents=True, exist_ok=True)
    ans = subprocess.call(["git", "init"], cwd=project_dir)
    if ans == 0:
        for cache in project_dir.rglob("__pycache__"):
            shutil.rmtree(cache, ignore_errors=True)
        subprocess.run(["git", "add", "."], cwd = project_dir)
        subprocess.run(["git", "commit", "-m", "Initial commit generated automatically by scaffy"], cwd = project_dir)
    logger.info("Git repository setup complete")