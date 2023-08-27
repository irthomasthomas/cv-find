from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="cv-find",
    description="Use computer vision algorithms to find stuff in a video",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="THOMAS_THOMAS",
    url="https://github.com/irthomasthomas/cv-find",
    project_urls={
        "Issues": "https://github.com/irthomasthomas/cv-find/issues",
        "CI": "https://github.com/irthomasthomas/cv-find/actions",
        "Changelog": "https://github.com/irthomasthomas/cv-find/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["cv_find"],
    entry_points="""
        [console_scripts]
        cv-find=cv_find.cli:cli
    """,
    install_requires=["click"],
    extras_require={
        "test": ["pytest"]
    },
    python_requires=">=3.7",
)
