# -*- coding: utf-8 -*-

"""
Locate the test file path for a given Python source file.

This utility calculates where a test file should be placed for a given Python
source file, following the Python test strategy naming convention:

    Source: git-repo/<package_name>/<subpackage>/<module>.py
    Test:   tests/<subpackage>/test_<subpackage>_<module>.py

Given an absolute path to a source file, this script:

1. Finds the project root (by locating pyproject.toml)
2. Determines the relative path from project root to source file
3. Calculates the correct test file path using naming convention
4. Prints the absolute test file path

This is useful for:

- IDE integrations that need to jump from source to test file
- Build tools that generate test files in the correct location
- Pre-commit hooks that validate tests exist for changed source files
- Development workflows that automate test file creation
"""

from pathlib import Path

from ..py_project import locate_pyproject_toml


def calculate_test_file_path(
    source_file_path: Path,
    project_root: Path,
) -> Path:
    """
    Calculate the test file path for a given source file.

    Applies the naming convention:
        tests/<subpackage>/test_<subpackage>_<module>.py

    For example:
        Source: my_package/math/operations/calculator.py
        Test:   tests/math/operations/test_math_operations_calculator.py

    :param source_file_path: Absolute path to the source file.
    :param project_root: Absolute path to the project root.

    :return: Absolute path where the test file should be located.

    :raises ValueError: If source file is not within the project.
    """
    # Get relative path from project root
    try:
        relative_source = source_file_path.relative_to(project_root)
    except ValueError:
        raise ValueError(
            f"Source file {source_file_path} is not within project root {project_root}"
        )

    # Get all path parts: ['package_name', 'subpackage', 'module.py']
    parts = relative_source.parts
    skip_first = 1  # Skip the project/package name (first directory)

    # Extract subdirectory and module name
    # parts[1:-1] are subdirectories, parts[-1] is the module filename
    subdirs = parts[skip_first:-1]
    module_filename = parts[-1].replace(".py", "")

    # Build test filename
    if subdirs:
        # Has subdirectories: test_<subdir1>_<subdir2>_<module>.py
        test_filename = f"test_{'_'.join(subdirs)}_{module_filename}.py"
        test_dir = project_root / "tests" / Path(*subdirs)
    else:
        # Root level: test_<module>.py
        test_filename = f"test_{module_filename}.py"
        test_dir = project_root / "tests"

    return test_dir / test_filename


def main(source_file: str) -> str:
    """
    Locate the corresponding test file for a Python source file.

    Maps source path to test path by stripping the package name and joining
    remaining path components with underscores:

        my_pkg/a/b/c.py -> tests/a/b/test_a_b_c.py

    :param source_file: Absolute path to the Python source file.
    """
    source_path = Path(source_file)

    # Find project root
    pyproject = locate_pyproject_toml(source_path.parent)
    if not pyproject:
        raise FileNotFoundError(
            "Could not locate pyproject.toml (project root not found)"
        )

    project_root = pyproject.parent

    # Calculate and print test file path
    test_path = calculate_test_file_path(source_path, project_root)
    print(test_path)
    return test_path