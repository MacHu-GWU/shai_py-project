# -*- coding: utf-8 -*-

from shai_py.subcmd.detect_python_project_metadata import main


def test_main():
    main()


if __name__ == "__main__":
    from shai_py.tests import run_cov_test

    run_cov_test(
        __file__,
        "shai_py.subcmd.detect_python_project_metadata",
        preview=False,
    )
