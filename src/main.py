import argparse
import logging
from pathlib import Path
from scaffold import create_project_structure
from venv_tools import create_virtualenv
from git_tools import git_init
from github_tools import create_repo
from docker import create_virtual_container

def main():
    logging.basicConfig(level=logging.INFO,format="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
        datefmt="%H:%M:%S")
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest = "command")
    init_parser = subparser.add_parser("init")
    init_parser.add_argument("--name",type = str)
    init_parser.add_argument("--env",type = str, default = "venv")

    git_parser = subparser.add_parser("setup-git")
    git_parser.add_argument("--name", type = str)
    git_parser.add_argument("--path", type=str, default=None)
    args = parser.parse_args()
    if args.command == "setup-git":
        private = input("Should your repository be set to private? Y/n")
        project_dir = Path(args.path) if args.path else Path(args.name)
        git_init(project_dir)
        create_repo(project_dir, private)
    if args.command == "init":
        create_project_structure(args.name)
        create_virtualenv(Path(args.name), args.env)
        create_virtual_container(Path(args.name), args.name)
if __name__ == "__main__":
    main()