# -*- coding: utf-8 -*-

from ..py_project import PyProjectMetadata


def main() -> PyProjectMetadata:
    """
    Display Python project metadata (values and paths) from pyproject.toml.

    Usage::

        shai-py project-info
    """
    py_project_metadata = PyProjectMetadata.new()
    py_project_metadata.print()
    return py_project_metadata


if __name__ == "__main__":
    main()
