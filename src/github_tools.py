import subprocess
from pathlib import Path
import textwrap

def create_repo(project_dir : Path, private) -> None:
    auth = subprocess.run(["gh", "auth", "status"])
    if private == "y" or private == "Y":
        private = "--private"
    else:
        private = "--public"
    if auth.returncode==0:
        dir_path = project_dir.resolve()
        subprocess.run(["gh", "repo", "create", "-s", f"{dir_path}", f"{private}", "--push"] )

def create_CICD(project_dir : Path) ->None:
    path = project_dir/".github" /"workflows"/"ci.yml"
    path.parent.mkdir(parents=True, exist_ok=True)
    ci_text = textwrap.dedent("""\
    name: CI
    on: [push, pull_request]
    jobs:
      test:
        runs-on: ubuntu-latest
        steps:
          - uses: actions/checkout@v4
          - uses: actions/setup-python@v5
            with:
              python-version: "3.12"
          - run: pip install pytest
          - run: pytest
    """)
    path.write_text(ci_text)