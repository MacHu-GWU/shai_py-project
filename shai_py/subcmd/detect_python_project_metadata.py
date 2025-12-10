# -*- coding: utf-8 -*-

from ..py_project import PyProjectMetadata


def main() -> PyProjectMetadata:
    """
    Detect and display Python project metadata from pyproject.toml.

    Outputs project name, version, Python version, and key absolute paths including
    virtual environment (.venv/bin/python, .venv/bin/pip), source directory,
    and test directory.
    """
    py_project_metadata = PyProjectMetadata.new()
    py_project_metadata.print()
    return py_project_metadata


if __name__ == "__main__":
    main()
