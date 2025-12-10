project-info
==============================================================================
Display Python project metadata (values and paths) from ``pyproject.toml``.

This command detects the project root by locating ``pyproject.toml`` and outputs key information about the project structure.


Usage
------------------------------------------------------------------------------
.. code-block:: bash

    shai-py project-info


Output Fields
------------------------------------------------------------------------------
**Values:**

- Package name from ``pyproject.toml``
- Package version from ``pyproject.toml``

**Paths:**

- Git Repo directory
- Main package directory
- virtualenv Python interpreter (``.venv/bin/python``)
- virtualenv Pip package manager (``.venv/bin/pip``)
- virtualenv Pytest test runner (``.venv/bin/pytest``)
- Unit tests directory (``tests/``)
- Documentation source directory (``docs/source/``)
- Sphinx config file (``conf.py``)
- mise.toml for ``mise run XYZ`` commands


Example Output
------------------------------------------------------------------------------
.. code-block:: text

    === Python Project Metadata ===
    Package name from pyproject.toml = shai-py
    Package version pyproject.toml = 0.1.1
    Git Repo directory = /Users/dev/shai_py-project
    Main package directory = /Users/dev/shai_py-project/shai_py
    virtualenv Python interpreter = /Users/dev/shai_py-project/.venv/bin/python
    virtualenv Pip package manager = /Users/dev/shai_py-project/.venv/bin/pip
    virtualenv Pytest test runner = /Users/dev/shai_py-project/.venv/bin/pytest
    Unit tests directory = /Users/dev/shai_py-project/tests
    Documentation source = /Users/dev/shai_py-project/docs/source
    Sphinx config file = /Users/dev/shai_py-project/docs/source/conf.py
    'mise run XYZ' Commands for environment, testing, docs, and releases = /Users/dev/shai_py-project/mise.toml
