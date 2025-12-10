# -*- coding: utf-8 -*-

from ..py_project import PyProjectMetadata


def main() -> PyProjectMetadata:
    py_project_metadata = PyProjectMetadata.new()
    py_project_metadata.print()
    return py_project_metadata


if __name__ == "__main__":
    main()
