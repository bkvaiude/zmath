import os, pathlib
from setuptools import setup, find_packages
from subprocess import check_call

VERSION = "0.0.1"
DESCRIPTION = "Sample Math Operations"
LONG_DESCRIPTION = "It is just demonstration of how to create python package"


def local_package_path(package_name):
    return "file://localhost/" + os.path.abspath(package_name)


# Setting up
setup(
    name="zmath",
    version=VERSION,
    author="Bhushan Kishore Vaiude",
    author_email="bkvaiude@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    keywords=["python", "math"],
    extras_require={
        "plus": ["zmathplus @ git+https://github.com/bkvaiude/zmathplus.git"],
        "square": [f'zmathsquare @ {local_package_path("zmathsquare")}'],
    },
    classifiers=[
        "mathematics",
    ],
    entry_points={"zmath_plugins": ["zmath = zmath"]},
)
