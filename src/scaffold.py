from pathlib import Path
from .github_tools import create_CICD

def create_project_structure(project_name: str, base_dir: Path = None) -> None:
    base = base_dir if base_dir else Path.cwd()
    dir_path = base / project_name
    dir_path.mkdir(exist_ok=True, parents = True)
    pyproject = dir_path / "pyproject.toml"
    pyproject.write_text(
        f'[project]\n'
        f'name = "{project_name}"\n'
        f'version = "0.1.0"\n'
        f'description = ""\n'
        f'requires-python = ">=3.10"\n'
        f'dependencies = []\n'
        f'\n'
        f'[project.optional-dependencies]\n'
        f'dev = [\n'
        f'    "pytest"\n'
        f']\n'
        f'\n'
        f'[tool.pytest.ini_options]\n'
        f'testpaths = ["tests"]\n'
    )
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
