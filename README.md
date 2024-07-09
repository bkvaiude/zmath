# Sample Python Package Demo

# Learnings

1. Need to do clean up, as z-math naming convention didn't work with import statement
1. Reinstalling didn't work, venv clean up it started working
1. Then followed Approch 2 to install packge with pip commond and tar.gz file
1. `extras` folder doesn't have any imports in `__init__` file, in that cases you need to mentioned full path like `from zmath.extras.multiply import multiply`
1. `from` accepts the chain of folders like `from zmath.extras.multiply` but you can't do following `zmath.extras.multiply.multiply(1, 2)`
1. In order to work with submodules, you need to add them as `git submodule add https://github.com/bkvaiude/zmathsquare.git zmathsquare`
python setup.py sdist bdist_wheel
1. `git submodule add --name zmathsquare https://github.com/bkvaiude/zmathsquare.git zmathsquare`

Approach 1

python setup.py install

Approach 2

pip install dist/zmath-0.0.1.tar.gz
