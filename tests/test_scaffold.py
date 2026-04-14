from src.scaffold import create_project_structure
from src.docker import create_dockerfile
from src.github_tools import create_CICD

def test_creates_expected_files(tmp_path):
    create_project_structure("testproject", base_dir=tmp_path)
    project = tmp_path / "testproject"
    assert (project / "README.md").exists()
    assert (project / "requirements.txt").exists()
    assert (project / "src" / "main.py").exists()
    assert (project / "tests" / "test_basic.py").exists()

def test_readme_contains_project_name(tmp_path):
    create_project_structure("myapp", base_dir=tmp_path)
    content = (tmp_path / "myapp" / "README.md").read_text()
    assert "myapp" in content

def test_dockerfile_created(tmp_path):
    create_dockerfile(tmp_path)
    assert (tmp_path / "Dockerfile").exists()

def test_dockerfile_has_no_space_in_workdir(tmp_path):
    create_dockerfile(tmp_path)
    content = (tmp_path / "Dockerfile").read_text()
    assert "WORKDIR /usr/src/app" in content

def test_cicd_workflow_created(tmp_path):
    create_CICD(tmp_path)
    assert (tmp_path / ".github" / "workflows" / "ci.yml").exists()

def test_cicd_contains_pytest(tmp_path):
    create_CICD(tmp_path)
    content = (tmp_path / ".github" / "workflows" / "ci.yml").read_text()
    assert "pytest" in content
