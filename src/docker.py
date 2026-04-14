import subprocess
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

def create_virtual_container(project_dir: Path, project_name: str) -> None:
    success = create_dockerfile(project_dir)
    if not success:
        logger.error("Failed to create Dockerfile, aborting build")
        return

    try:
        subprocess.run(["docker", "build", "-t", f"{project_name}", ".", "--progress", "plain"], cwd=project_dir, check=True)
        logger.info("Docker image '%s' succesfully built", project_name)
    except subprocess.CalledProcessError as e:
        logger.error("Docker build failed with return code %d", e.returncode)

def create_dockerfile(project_dir: Path) -> bool:
    path = project_dir / "Dockerfile"
    try:
        path.write_text(
            "FROM python:3.9-slim \n"
            "WORKDIR /usr/src/app \n"
            "COPY . . \n"
            "RUN pip install --no-cache-dir -r requirements.txt \n"
            'CMD ["python", "src/main.py"]'
        )
        logger.info("Dockerfile created at %s", path)
        return True
    except OSError as e:
        logger.error("Failed to write Dockerfile: %s", e)
        return False