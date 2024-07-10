import os, pathlib
from setuptools.command.develop import develop
from setuptools.command.install import install
from setuptools.command.sdist import sdist
from setuptools import setup, find_packages
from subprocess import check_call
import shutil
from subprocess import run

VERSION = "0.0.1"
DESCRIPTION = "Sample Math Operations"
LONG_DESCRIPTION = "It is just demonstration of how to create python package"


def local_package_path(package_name):
    return "file://localhost" + os.path.abspath(package_name)


def gitcmd_update_submodules():
    """Check if the package is being deployed as a git repository. If so, recursively
    update all dependencies.

    @returns True if the package is a git repository and the modules were updated.
            False otherwise.
    """

    if os.path.exists(os.path.join(pathlib.Path(__file__).parent, ".git")):
        check_call(["git", "submodule", "update", "--init", "--recursive"])
        check_call(["git", "submodule", "update", "--remote", "--merge"])
        return True


class gitcmd_develop(develop):
    """Specialized packaging class that runs git submodule update --init --recursive
    as part of the update/install procedure.
    """

    def run(self):
        gitcmd_update_submodules()
        develop.run(self)


class gitcmd_install(install):
    """Specialized packaging class that runs git submodule update --init --recursive
    as part of the update/install procedure.
    """

    def run(self):
        gitcmd_update_submodules()
        install.run(self)


class gitcmd_sdist(sdist):
    """Specialized packaging class that runs git submodule update --init --recursive
    as part of the update/install procedure;.
    """

    def run(self):
        gitcmd_update_submodules()
        sdist.run(self)


# Setting up
setup(
    cmdclass={
        "develop": gitcmd_develop,
        "install": gitcmd_install,
        "sdist": gitcmd_sdist,
    },
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
