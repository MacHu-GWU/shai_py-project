# -*- coding: utf-8 -*-

import typing as T

import fire


class Cli:
    def detect_python_project_metadata(self):
        from .subcmd.detect_python_project_metadata import main

        main()


def run():
    fire.Fire(Cli())


if __name__ == "__main__":
    run()
