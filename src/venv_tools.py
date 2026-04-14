from pathlib import Path
import subprocess
import logging

logger = logging.getLogger(__name__)

def create_virtualenv(project_dir: Path, env_manager: str = "venv") -> None:
    if env_manager == "venv":
        subprocess.run(["python", "-m", "venv", ".venv"], cwd = project_dir)
        logging.info("Virtual environment created. Activate it with: \n source .venv/bin/activate")
        subprocess.run([".venv/bin/pip", "install","pytest"], cwd =project_dir)
