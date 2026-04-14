# scaffy
![CI](https://github.com/Rac00nCanFly/scaffy/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.10+-blue)
![Docker](https://img.shields.io/badge/docker-ready-blue)

CLI tool for automating Python project setup. Scaffy generates a complete project structure, configures a virtual environment, creates a Dockerfile, sets up a GitHub Actions CI/CD pipeline, and pushes the project to GitHub — all with a single command.

## Features

- 📁 Generates project structure with `src/`, `tests/`, `pyproject.toml`, `.gitignore`
- 🐳 Creates a ready-to-use `Dockerfile` for containerization
- ⚙️ Sets up GitHub Actions CI/CD workflow with automated pytest runs
- 🐙 Initializes Git, creates a GitHub repository and pushes — automatically
- 🐍 Creates and configures a virtual environment

## Requirements

- Python 3.10+
- Git
- Docker
- [GitHub CLI (`gh`)](https://cli.github.com/) — authenticated via `gh auth login`

## Installation

```bash
git clone https://github.com/Rac00nCanFly/scaffy.git
cd scaffy
pip install -e ".[dev]"
```

## Usage

### Create a new project locally with a virtual environment and Docker

```bash
python src/cli.py init --name my-project
```
Generates:
```
my-project/
├── src/
│ ├── _init_.py
│ └── main.py
├── tests/
│ └── test_basic.py
├── .github/
│ └── workflows/
│ └── ci.yml
├── Dockerfile
├── pyproject.toml
├── conftest.py
└── .gitignore
```


### Create a project, initialize Git and push to GitHub

```bash
python src/main.py setup-git --name my-project
```

### Set up Git for an existing project

```bash
python src/main.py setup-git --path /path/to/existing-project
```

## Running tests

```bash
pytest
```

## Tech stack

| Tool | Purpose |
|---|---|
| `argparse` | CLI interface |
| `subprocess` | System automation (git, docker, gh) |
| `pathlib` | File system operations |
| `logging` | Structured application logs |
| `pytest` | Testing |
| GitHub Actions | CI/CD pipeline |
| Docker | Containerization |

## Roadmap

- [ ] LLM-assisted README generation (OpenAI / Ollama integration)
- [ ] Support for `uv` as alternative package manager
- [ ] Interactive project setup wizard (`--interactive` flag)
- [ ] Templates system — choose between basic, data-science, web-api scaffolds
- [ ] `scaffy doctor` command to verify environment (git, docker, gh installed)