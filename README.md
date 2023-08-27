# cv-find

[![PyPI](https://img.shields.io/pypi/v/cv-find.svg)](https://pypi.org/project/cv-find/)
[![Changelog](https://img.shields.io/github/v/release/irthomasthomas/cv-find?include_prereleases&label=changelog)](https://github.com/irthomasthomas/cv-find/releases)
[![Tests](https://github.com/irthomasthomas/cv-find/workflows/Test/badge.svg)](https://github.com/irthomasthomas/cv-find/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/irthomasthomas/cv-find/blob/master/LICENSE)

Use computer vision algorithms to find stuff in a video

## Installation

Install this tool using `pip`:

    pip install cv-find

## Usage

For help, run:

    cv-find --help

You can also use:

    python -m cv_find --help

## Development

To contribute to this tool, first checkout the code. Then create a new virtual environment:

    cd cv-find
    python -m venv venv
    source venv/bin/activate

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest
