# -*- coding: utf-8 -*-

from shai_py.subcmd.locate_test_file import calculate_test_file_path
from shai_py.subcmd.locate_test_file import main

from pathlib import Path

import pytest

from shai_py.paths import path_enum


def test_main():
    # Use a real source file from this project
    source_file = path_enum.dir_package / "subcmd" / "locate_test_file.py"
    main(str(source_file))


def test_main_no_pyproject_toml():
    # Test with a path that has no pyproject.toml in any parent directory
    with pytest.raises(FileNotFoundError):
        main("/tmp/nonexistent_project/package/module.py")


def test_calculate_test_file_path():
    project_root = Path("/path/to/project")

    # Test case 1: source file with subdirectories
    source_path = project_root / "my_package" / "math" / "operations" / "calculator.py"
    result = calculate_test_file_path(source_path, project_root)
    expected = (
        project_root
        / "tests"
        / "math"
        / "operations"
        / "test_math_operations_calculator.py"
    )
    assert result == expected

    # Test case 2: source file with one subdirectory
    source_path = project_root / "my_package" / "utils" / "helpers.py"
    result = calculate_test_file_path(source_path, project_root)
    expected = project_root / "tests" / "utils" / "test_utils_helpers.py"
    assert result == expected

    # Test case 3: source file at package root level
    source_path = project_root / "my_package" / "core.py"
    result = calculate_test_file_path(source_path, project_root)
    expected = project_root / "tests" / "test_core.py"
    assert result == expected


def test_calculate_test_file_path_not_in_project():
    # Test ValueError when source file is not within project root
    project_root = Path("/path/to/project")
    source_path = Path("/other/path/module.py")

    with pytest.raises(ValueError, match="is not within project root"):
        calculate_test_file_path(source_path, project_root)


if __name__ == "__main__":
    from shai_py.tests import run_cov_test

    run_cov_test(
        __file__,
        "shai_py.subcmd.locate_test_file",
        preview=False,
    )
