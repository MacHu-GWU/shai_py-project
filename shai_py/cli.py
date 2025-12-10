# -*- coding: utf-8 -*-

import fire
import shai_py.subcmd.detect_python_project_metadata
import shai_py.subcmd.locate_test_file


class Cli:
    """
    CLI tools for Sanhe-styled Python project development workflows.

    Provides utilities for project introspection, test file location,
    and other automation tasks following Sanhe's Python conventions.
    """

    def project_info(self):
        shai_py.subcmd.detect_python_project_metadata.main()

    project_info.__doc__ = shai_py.subcmd.detect_python_project_metadata.main.__doc__

    def test_path(
        self,
        source_file: str,
    ):
        shai_py.subcmd.locate_test_file.main(source_file)

    test_path.__doc__ = shai_py.subcmd.locate_test_file.main.__doc__


def run():
    fire.Fire(Cli())


if __name__ == "__main__":
    run()
