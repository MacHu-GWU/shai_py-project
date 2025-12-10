# -*- coding: utf-8 -*-

import fire
import shai_py.subcmd.detect_python_project_metadata
import shai_py.subcmd.locate_test_file


class Cli:
    def detect_python_project_metadata(self):
        return shai_py.subcmd.detect_python_project_metadata.main()

    detect_python_project_metadata.__doc__ = (
        shai_py.subcmd.detect_python_project_metadata.__doc__
    )

    def locate_test_file(
        self,
        source_file: str,
    ):
        return shai_py.subcmd.locate_test_file.main(source_file)

    locate_test_file.__doc__ = shai_py.subcmd.locate_test_file.__doc__


def run():
    fire.Fire(Cli())


if __name__ == "__main__":
    run()
