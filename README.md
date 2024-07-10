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
1. `git submodule update --remote --merge` to fetch latest changes from main
1. https://stackoverflow.com/questions/1260748/how-do-i-remove-a-submodule#:~:text=Run%20git%20rm%20%3Cpath%2Dto,entry%20in%20the%20.gitmodules%20file.
1. Build service skeleton using boilerplate template (suggestion for future)
1. Approach with .gitmodules
    1. Checkout to zyrous service repo
    1. add necesaary modules using following command `git submodule add https://github.com/bkvaiude/zmathsquare.git zmath/zmathsquare`
    1. `git submodule update --remote --merge` to fetch latest changes from main, still need to figure out a way for tag version or commit
    1. git add and commit those packages that leads new version release of zyrous service
    1. use the zyrous service version in your app or service development
    1. this inforce monorepo kind of implementation with tight coupling and no optional packages
    1. there are way to make it optional packges but not efficient solution like maintaining env variable or dotenv file
    1. tedious process to remove a submodule, as above approach only help to skip but installation will happen and it will impact on storage space
    1. setup.py of main.pkg only works if the submodule exists on the disk, else it will fail
    1. tried experimenting with setup.py with custom install command but that d'dn't work with pip install, need more time for investigation
1. Git module cleanup
    1. rm -rf zmathsquare
    1. rm -rf .git/modules/zmathsquare
    1. git rm --cached zmathsquare

Why Use Git Submodules?
Version Control: Keep specific versions of submodules tied to specific versions of the main project.
Development: Allow development on both the main project and submodules simultaneously.
Consistency: Ensure that all developers are using the exact same versions of submodules.

You are correct that using pip install <repo_url>@<tag_version> allows you to install packages from a specific repository URL and tag/version, which can achieve similar benefits in terms of version control and consistency. However, there are some key differences and considerations between using Git submodules and using pip install with repository URLs.

Differences and Considerations
Git Submodules
Tight Integration with Main Repo:

Submodules are tightly integrated with the main repository. They are version-controlled together, ensuring that specific versions of the submodules are always in sync with the main project.
You can commit and push changes to both the main repository and submodules in a single workflow.
Development Workflow:

Allows seamless development across the main project and its submodules. You can make changes in submodules and commit them along with changes in the main project.
Useful for situations where you need to frequently modify and test submodules alongside the main project.
Repository Structure:

Keeps all the code (main project and submodules) in one directory structure. This can be more convenient for managing and navigating the codebase.
Offline Access:

You have the full source code of the submodules available locally, which can be beneficial for offline development and inspection.
Consistency and Reproducibility:

Ensures that anyone cloning the main repository and updating submodules gets the exact same versions of the submodules.
pip install <repo_url>@<tag_version>
Simpler Dependency Management:

Simplifies dependency management by treating submodules as external dependencies, similar to other Python packages.
More straightforward for users who are used to managing dependencies via pip.
Separation of Concerns:

Keeps the main project repository cleaner and smaller by not including the submodule code directly.
Submodules can be maintained and versioned independently, which can be advantageous for large projects or projects with multiple consumers.
Installation Flexibility:

You can specify exact versions or tags for dependencies, ensuring consistency.
Easy to install and update specific versions without needing to initialize and update submodules manually.
CI/CD and Deployment:

Works well with Continuous Integration/Continuous Deployment (CI/CD) pipelines where dependencies are specified in a requirements file or setup script.
Easier to handle in automated environments since it doesn’t require submodule-specific Git commands.

Problem Statements

- Naming conventions
- Code separation and it benefits like testcases, integration testing
- Auto load capabilities if module found then factory class will automatically load classes or throws the error on use of service.

Approach 1

python setup.py install

Approach 2

pip install dist/zmath-0.0.1.tar.gz


Idea

/zmath
    /setup.py
  
        /__init__.py
        /add.py
        /extras
            /subtract.py
            /__init__.py
    /zmathsquare ------------------> as gitmodule
        /__init__.py
        /square.py
        /extras
            /__init__.py
            /square_root.py
    /zmathplus ------------------> as package
        /__init__.py
        /multiply.py 
        /extras
            /__init__.py
            /divide.py

Demo 1
Install zmath 
Perform needful ops to install gitmodule
Install plus pkg 
Write test cases and validate

Demo 2
Install zmath 
Skip - Perform needful ops to install gitmodule
Install plus pkg 
Write test cases and validate

Demo 3
Install zmath 
Perform needful ops to install gitmodule
Install plus pkg 
add module has dependancies on plus pkg
Write test cases and validate

Demo 4
Install zmath 
Perform needful ops to install gitmodule
Skip - Install plus pkg 
add module has dependancies on plus pkg
Write test cases and validate