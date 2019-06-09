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
    name="datasette-bplist",
    description="Datasette plugin for working with Apple's binary plist format",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    url="https://github.com/simonw/datasette-bplist",
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["datasette_bplist"],
    entry_points={"datasette": ["bplist = datasette_bplist"]},
    install_requires=["datasette", "bpylist"],
    extras_require={"test": ["pytest"]},
    tests_require=["datasette-bplist[test]"],
)
