# -*- coding: utf-8 -*-

import json
import tomllib
import subprocess
import dataclasses
from pathlib import Path


def locate_git_repo(dir_cwd: Path) -> Path | None:
    """
    Locate the git repository root directory by searching for the .git folder.
    """
    for _ in range(10):
        if dir_cwd.joinpath(".git").exists():
            return dir_cwd
        dir_cwd = dir_cwd.parent
    return None


def locate_pyproject_toml(dir_cwd: Path) -> Path | None:
    """
    Locate the pyproject.toml file by searching upwards in the directory tree.
    """
    for _ in range(10):
        if dir_cwd.joinpath("pyproject.toml").exists():
            return dir_cwd.joinpath("pyproject.toml")
        dir_cwd = dir_cwd.parent
    return None


def locate_venv_bin_python(dir_cwd: Path) -> Path | None:
    """
    Locate the virtual environment directory by searching for the .venv folder.
    """
    for _ in range(10):
        path_venv_bin_python = dir_cwd.joinpath(".venv", "bin", "python")
        if path_venv_bin_python.exists():
            return path_venv_bin_python
        dir_cwd = dir_cwd.parent
    return None


def get_python_version(path_venv_bin_python: Path) -> tuple[int, int, int]:
    """
    Get the Python version of the specified python executable.
    """
    args = [
        f"{path_venv_bin_python}",
        "--version",
    ]
    res = subprocess.run(args, capture_output=True)
    text = res.stdout.decode("utf-8").strip()
    parts = text.split()[1].split(".")
    return int(parts[0]), int(parts[1]), int(parts[2])


@dataclasses.dataclass
class Info:
    key: str
    value: str


@dataclasses.dataclass
class PyProjectMetadata:
    infos: list[Info]

    @classmethod
    def new(cls):
        infos = []
        dir_here = Path.cwd()
        path_pyproject_toml = locate_pyproject_toml(dir_here)
        data = tomllib.loads(path_pyproject_toml.read_text(encoding="utf-8"))

        package_name = data["project"]["name"]
        package_version = data["project"]["version"]

        infos.append(Info(key="Package name from pyproject.toml", value=package_name))
        infos.append(Info(key="Package version pyproject.toml", value=package_version))

        dir_project_root = path_pyproject_toml.parent
        dir_package = dir_project_root / package_name
        dir_venv = dir_project_root / ".venv"
        path_venv_bin_python = dir_venv / "bin" / "python"
        path_venv_bin_pip = dir_venv / "bin" / "pip"
        path_venv_bin_pytest = dir_venv / "bin" / "pytest"
        dir_unit_tests = dir_project_root / "tests"
        dir_docs_source = dir_project_root / "docs" / "source"
        path_sphinx_conf_py = dir_docs_source / "conf.py"
        path_mise = dir_project_root / "mise.toml"

        # fmt: off
        infos.append(Info(key="Git Repo directory", value=str(dir_project_root)))
        infos.append(Info(key="Main package directory", value=str(dir_package)))
        infos.append(Info(key="virtualenv Python interpreter", value=str(path_venv_bin_python)))
        infos.append(Info(key="virtualenv Pip package manager", value=str(path_venv_bin_pip)))
        infos.append(Info(key="virtualenv Pytest test runner", value=str(path_venv_bin_pytest)))
        infos.append(Info(key="Unit tests directory", value=str(dir_unit_tests)))
        infos.append(Info(key="Documentation source", value=str(dir_docs_source)))
        infos.append(Info(key="Sphinx config file", value=str(path_sphinx_conf_py)))
        infos.append(Info(key="'mise run XYZ' Commands for environment, testing, docs, and releases", value=str(path_mise)))
        # fmt: on
        return PyProjectMetadata(infos=infos)

    def print(self):
        print("=== Python Project Metadata ===")
        for info in self.infos:
            print(f"{info.key} = {info.value}")
