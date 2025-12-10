# -*- coding: utf-8 -*-

from ..py_project import PyProjectMetadata


def main() -> PyProjectMetadata:
    """
    Display Python project metadata from pyproject.toml.

    Outputs project name, version, Python version, and key absolute paths
    (virtualenv, source directory, test directory).

    Usage::

        shai-py project-info
    """
    py_project_metadata = PyProjectMetadata.new()
    py_project_metadata.print()
    return py_project_metadata


if __name__ == "__main__":
    main()
