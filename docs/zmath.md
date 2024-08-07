# Python Package - Proof of Concept

## Description

This Proof of Concept (POC) demonstrates various packages and scenarios in a modular Python project.

### Packages

- **zmath**: The main package providing basic functionality like addition and subtraction.
- **zmathsquare**: A submodule of the zmath package, added using the `.gitmodules` approach. It provides square and square root functionality. This is an optional package, installed with `pip install zmath[square]`.
- **zmathplus**: Another package related to zmath, but maintained as an external package in a separate repository.It provides multiplication and division functionality. This is also an optional package, installed with `pip install zmath[plus]`.

### POC Scenarios

1. **Scenario 1**: Main package holds all optional packages as git submodules.
2. **Scenario 2**: Main package holds all optional packages as external dependencies.
3. **Scenario 3**: Dynamically identify installed optional packages and load them in the main package environment. If an attempt is made to access a package that is not installed, an exception is thrown.

## Folder Structure

### Git Repository Structure

**[ZMATH Repository](https://github.com/bkvaiude/zmath)**

```
zmath/
│   ├── setup.py
│   ├── __init__.py
│   ├── add.py
│   └── extras/
│       ├── __init__.py
│       └── subtract.py
```

**[ZMATH SQUARE Repository](https://github.com/bkvaiude/zmathsquare)**

```
zmathsquare/ ------------------> as git submodule
└── src/
    └── zmath/
        ├── __init__.py
        └── zmathsquare/
            ├── __init__.py
            ├── square.py
            └── extras/
                ├── __init__.py
                └── square_root.py
```

**[ZMATH PLUS Repository](https://github.com/bkvaiude/zmathplus)**

```
zmathplus/ ------------------> as external package
└── src/
    └── zmath/
        ├── __init__.py
        └── zmathplus/
            ├── __init__.py
            ├── divide.py
            └── extras/
                ├── __init__.py
                └── multiply.py
```

### Site-Packages Directory Structure After Installation

After installing all packages, the directory structure in `site-packages` will look like this:

```
om@MSI:~/.local/share/virtualenvs/demo-UVQjeUvo/lib/python3.10/site-packages$ tree zmath -I "__pycache__"
zmath
├── __init__.py
├── add.py
├── extras
│   ├── __init__.py
│   └── subtract.py
├── zmathplus
│   ├── __init__.py
│   ├── divide.py
│   └── extras
│       ├── __init__.py
│       └── multiply.py
└── zmathsquare
    ├── __init__.py
    ├── extras
    │   ├── __init__.py
    │   └── square_root.py
    └── square.py
```

## Installation

Install the `zmath` main package

```
pip install --no-clean git+https://github.com/bkvaiude/zmath.git@main
```

Install the optional packages like `zmathsquare` and `zmathplus`

```
pip install zmath[square]

pip install zmath[plus]

pip install zmath[square,plus]
```

Take note [setup.py](https://github.com/bkvaiude/zmath/blob/main/setup.py) file and extra_requires parameter to get more understanding.
