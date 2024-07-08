from setuptools import setup, find_packages

VERSION = "0.0.1"
DESCRIPTION = "Sample Math Operations"
LONG_DESCRIPTION = "It is just demonstration of how to create python package"

# Setting up
setup(
    name="zmath",
    version=VERSION,
    author="Bhushan Kishore Vaiude",
    author_email="bkvaiude@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=["python", "math"],
    classifiers=[
        "mathematics",
    ],
)
