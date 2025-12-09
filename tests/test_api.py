# -*- coding: utf-8 -*-

from shai_py import api


def test():
    _ = api


if __name__ == "__main__":
    from shai_py.tests import run_cov_test

    run_cov_test(
        __file__,
        "shai_py.api",
        preview=False,
    )
