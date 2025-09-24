#!/bin/bash
# #########################
# Install dev environment
# #########################

# Install Poetry, a dependency management and packaging tool for Python.
brew install poetry

# Install pyenv, a version management tool for Python.
brew install pyenv

# Install Python version 3.10.0 using pyenv.
# This downloads and builds the specified Python version.
pyenv install 3.10.0

# Set the Python version locally to 3.10.0 for the current directory/project.
# This creates a `.python-version` file, locking the project to Python 3.10.0.
pyenv local 3.10.0


# Configure Poetry to create the venv in the project
poetry config virtualenvs.in-project true --local

# Ensure dependencies are installed
poetry install
