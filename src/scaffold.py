from pathlib import Path
from github_tools import create_CICD

def create_project_structure(project_name: str) -> None:
    dir_path = Path.cwd() / f"{project_name}"
    dir_path.mkdir(exist_ok=True, parents = True)
    requirements = dir_path / "requirements.txt"
    requirements.write_text("pytest")
    readme = dir_path / "README.md"
    readme.write_text(f"# {project_name}")
    gitignore = dir_path / ".gitignore"
    gitignore.write_text(".venv/\n __pycache__/\n .pytest_cache/ \n *.pyc")
    create_CICD(dir_path)
    conftest = dir_path / "conftest.py"
    conftest.write_text("")

    src_path = dir_path / "src"
    src_path.mkdir(exist_ok=True)
    init = src_path / "__init__.py"
    init.write_text('__version__ = "0.1.0"')
    main = src_path / "main.py"
    main.write_text("def build_greeting(name:str) -> str: \n"
                    "   return f'Hello,{name}!' \n"
                    "def main(): \n"
                    "   print(build_greeting('world')) \n"
                    "if __name__ == '__main__':\n"
                    "   main()")

    tests_path = dir_path / "tests"
    tests_path.mkdir(exist_ok=True)
    test = tests_path / "test_basic.py"
    test.write_text('from src.main import build_greeting \n'
                    'def test_build_greeting(): \n'
                    '   assert build_greeting("Alice") == "Hello,Alice!"')
