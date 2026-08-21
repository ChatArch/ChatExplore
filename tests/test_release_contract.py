from pathlib import Path


def _read(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


def test_package_metadata_uses_bounded_shared_cli_runtime():
    pyproject = _read("pyproject.toml")

    assert 'chatexplore = "chatexplore.cli:main"' in pyproject
    assert '"click>=8.0,<9.0"' in pyproject
    assert '"chatstyle>=0.2.0,<0.3.0"' in pyproject
    assert "chatenv" not in pyproject


def test_ci_checks_installed_cli_and_distribution_contract():
    workflow = _read(".github/workflows/ci.yml")

    assert 'python -m pip install -e ".[dev]"' in workflow
    assert "python -m pytest -q" in workflow
    assert "chatexplore --version" in workflow
    assert "chatexplore --tree" in workflow
    assert "chatexplore --tree-brief" in workflow
    assert "python -m build" in workflow
    assert "python -m twine check dist/*" in workflow


def test_docs_record_shared_tree_and_release_contracts():
    for path in ("README.md", "docs/README.md", "DEVELOP.md"):
        text = _read(path)
        assert "chatexplore --tree" in text
        assert "chatexplore --tree-brief" in text
        assert "chatstyle" in text.lower()

    changelog = _read("CHANGELOG.md")
    assert "## 0.0.2 - 2026-08-21" in changelog
    assert "trusted publishing" in changelog


def test_publish_workflow_uses_oidc_with_release_guards():
    workflow = _read(".github/workflows/publish.yml")

    assert "id-token: write" in workflow
    assert "pypa/gh-action-pypi-publish@release/v1" in workflow
    assert "Check tag matches package version" in workflow
    assert "Check release commit is on default branch" in workflow
    assert "git fetch --no-tags origin main:refs/remotes/origin/main" in workflow
    assert 'git merge-base --is-ancestor "${GITHUB_SHA}" refs/remotes/origin/main' in workflow
    assert "Check PyPI version" in workflow
    assert "environment: pypi" not in workflow
    assert "PYPI_API_TOKEN" not in workflow
    assert "TWINE_PASSWORD" not in workflow
