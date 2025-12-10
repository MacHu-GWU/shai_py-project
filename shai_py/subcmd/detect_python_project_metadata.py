#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ..py_project import PyProjectMetadata


def main():
    py_project_metadata = PyProjectMetadata.new()
    py_project_metadata.print()


if __name__ == "__main__":
    main()
