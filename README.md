# [Demo](https://github.com/bkvaiude/zmath/blob/main/docs/zmath.md)

## Overview

This documentation covers the process and considerations for setting up and managing the `zmath` package with optional submodules, providing insights into both the benefits and challenges of different approaches.

---

## Installation Approaches

### Approach 1: Using `.gitmodules`

1. **Checkout Service Repository**:
   - Navigate to your main repository directory.
   
2. **Add Necessary Submodules**:
   - Use the command: `git submodule add https://github.com/bkvaiude/zmathsquare.git zmath/zmathsquare`.
   
3. **Update Submodules**:
   - Fetch the latest changes using: `git submodule update --remote --merge`.
   
4. **Commit Changes**:
   - Commit the added submodules and any other changes: `git add . && git commit -m "Add zmathsquare submodule"`.
   
5. **Use Updated Version**:
   - Incorporate the new version of the service in your app or service development.

6. **Monorepo Implementation**:
   - This approach enforces a monorepo structure with tight coupling, making it difficult to manage optional packages efficiently.
   
7. **Make Packages Optional (Inefficient)**:
   - Use environment variables or dotenv files to manage optional packages.

8. **Tedious Removal Process**:
   - Removing a submodule requires multiple steps and can impact storage space.
   
9. **Dependency Handling**:
   - Ensure `setup.py` works only if submodules exist on disk, else it will fail.

10. **Custom Install Command**:
    - Experiment with custom install commands in `setup.py`, but they may not work seamlessly with `pip install`.

### Git Module Cleanup

1. Remove the submodule directory:
   - `rm -rf zmathsquare`
   
2. Remove the submodule reference:
   - `rm -rf .git/modules/zmathsquare`
   
3. Remove from Git cache:
   - `git rm --cached zmathsquare`

### How to install main package

1. **Install Main Package**:
   - Use the command: `pip install --no-clean git+https://github.com/bkvaiude/zmath.git@main`.
   - The `--no-clean` option prevents the temporary folder from being deleted.
   
2. **Folder Creation**:
   - During installation, a new folder is created in `/tmp` for cloning the repository with gitmodules.
   
3. **Issue with Temporary Folder Deletion**:
   - On successful installation, the `/tmp` folder is deleted, causing errors during optional package installation.
   
4. **Solution**:
   - Use the `--no-clean` option to avoid the deletion of the `/tmp` folder.

---

## Learnings and Notes

1. Clean up is required if naming conventions cause import issues.
2. Reinstalling and cleaning the virtual environment can resolve issues.
3. Followed the approach of installing the package with pip command and tar.gz file.
4. Ensure the `extras` folder has necessary imports in the `__init__.py` file.
5. Use the full path for imports if `__init__.py` lacks them.
6. Git submodules need to be added with commands like `git submodule add --name zmathsquare https://github.com/bkvaiude/zmathsquare.git zmathsquare`.
7. Use `git submodule update --remote --merge` to fetch the latest changes.
8. Refer to [StackOverflow](https://stackoverflow.com/questions/1260748/how-do-i-remove-a-submodule) for submodule removal steps.
9. Build service skeletons using boilerplate templates for future projects.

---

## Pros and Cons of Approaches

### Why Use Git Submodules?

- **Version Control**: Keep specific versions of submodules tied to specific versions of the main project.
- **Development**: Allow development on both the main project and submodules simultaneously.
- **Consistency**: Ensure all developers use the exact same versions of submodules.

### Differences and Considerations

#### Git Submodules

- **Tight Integration**: Version-controlled together with the main project.
- **Development Workflow**: Seamless development across the main project and submodules.
- **Repository Structure**: Convenient for managing and navigating the codebase.
- **Offline Access**: Full source code available locally.
- **Consistency and Reproducibility**: Ensures the same versions for everyone cloning the repository.

#### `pip install <repo_url>@<tag_version>`

- **Simpler Dependency Management**: Treats submodules as external dependencies.
- **Separation of Concerns**: Keeps the main project repository cleaner.
- **Installation Flexibility**: Specify exact versions or tags for dependencies.
- **CI/CD and Deployment**: Works well with CI/CD pipelines, handling dependencies efficiently in automated environments.

---

## Problem Statements

- **Naming Conventions**: Ensure consistent naming to avoid import issues.
- **Code Separation**: Benefits include easier test case management and integration testing.
- **Auto Load Capabilities**: Factory classes should automatically load classes or throw errors if a service is accessed but not installed.

---