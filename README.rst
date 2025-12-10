
.. image:: https://readthedocs.org/projects/shai-py/badge/?version=latest
    :target: https://shai-py.readthedocs.io/en/latest/
    :alt: Documentation Status

.. image:: https://github.com/MacHu-GWU/shai_py-project/actions/workflows/main.yml/badge.svg
    :target: https://github.com/MacHu-GWU/shai_py-project/actions?query=workflow:CI

.. image:: https://codecov.io/gh/MacHu-GWU/shai_py-project/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/MacHu-GWU/shai_py-project

.. image:: https://img.shields.io/pypi/v/shai-py.svg
    :target: https://pypi.python.org/pypi/shai-py

.. image:: https://img.shields.io/pypi/l/shai-py.svg
    :target: https://pypi.python.org/pypi/shai-py

.. image:: https://img.shields.io/pypi/pyversions/shai-py.svg
    :target: https://pypi.python.org/pypi/shai-py

.. image:: https://img.shields.io/badge/✍️_Release_History!--None.svg?style=social&logo=github
    :target: https://github.com/MacHu-GWU/shai_py-project/blob/main/release-history.rst

.. image:: https://img.shields.io/badge/⭐_Star_me_on_GitHub!--None.svg?style=social&logo=github
    :target: https://github.com/MacHu-GWU/shai_py-project

------

.. image:: https://img.shields.io/badge/Link-API-blue.svg
    :target: https://shai-py.readthedocs.io/en/latest/py-modindex.html

.. image:: https://img.shields.io/badge/Link-Install-blue.svg
    :target: `install`_

.. image:: https://img.shields.io/badge/Link-GitHub-blue.svg
    :target: https://github.com/MacHu-GWU/shai_py-project

.. image:: https://img.shields.io/badge/Link-Submit_Issue-blue.svg
    :target: https://github.com/MacHu-GWU/shai_py-project/issues

.. image:: https://img.shields.io/badge/Link-Request_Feature-blue.svg
    :target: https://github.com/MacHu-GWU/shai_py-project/issues

.. image:: https://img.shields.io/badge/Link-Download-blue.svg
    :target: https://pypi.org/pypi/shai-py#files


Welcome to ``shai_py`` Documentation
==============================================================================
.. image:: https://shai-py.readthedocs.io/en/latest/_static/shai_py-logo.png
    :target: https://shai-py.readthedocs.io/en/latest/

In the AI-driven development era, tools must be designed for machine consumption first. ``shai-py`` (Sanhe AI Python tools) embraces this philosophy by packaging Python development utilities as a CLI-first library, making it effortless for AI agents like Claude Code to invoke sophisticated workflows. Instead of writing one-off scripts scattered across agent skills, we consolidate battle-tested logic into a versioned Python package that AI can invoke with a single uvx command—no installation, no environment pollution, just instant execution.

This approach solves the fundamental challenge of AI tool integration: how to provide powerful, testable, and maintainable utilities without cluttering agent contexts with implementation details. By exposing functionality through clean CLI interfaces (``uvx shai-py detect-metadata``, ``uvx shai-py locate-test``), AI agents can focus on orchestration while developers maintain business logic in a single, version-controlled codebase. The result is elegant, reproducible, and scales beautifully from simple project introspection to complex development automation.


.. _install:

Install
------------------------------------------------------------------------------

``shai_py`` is released on PyPI, so all you need is to:

.. code-block:: console

    $ pip install shai-py

To upgrade to latest version:

.. code-block:: console

    $ pip install --upgrade shai-py
