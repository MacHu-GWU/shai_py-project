# -*- coding: utf-8 -*-

import typing as T

import fire
import shai_py.subcmd.detect_python_project_metadata


class Cli:
    def detect_python_project_metadata(self):
        return shai_py.subcmd.detect_python_project_metadata.main()

    detect_python_project_metadata.__doc__ = (
        shai_py.subcmd.detect_python_project_metadata.__doc__
    )


def run():
    fire.Fire(Cli())


if __name__ == "__main__":
    run()
