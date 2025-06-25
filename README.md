# lib-version

[![GitHub Actions Workflow Status](https://github.com/remla25-team4/lib-version/actions/workflows/release.yml/badge.svg)](https://github.com/remla25-team4/lib-version/actions/workflows/release.yml)

## Overview

`lib-version` is a utility library created as part of the REMLA `Restaurant Sentiment Analysis` application (Assignment 1: Versions, Releases, and Containerization).

Its primary purpose is to provide a reliable way for other components, specifically the `app-service`, to retrieve the current version of the library itself. This version information can be useful for logging, monitoring, or displaying in application information endpoints.

## How it Works

This library uses [`setuptools_scm`](https://github.com/pypa/setuptools_scm/) to automatically determine its version based on Git tags during the package build process.

-   When a release tag (e.g., `v1.0.0`) is pushed to GitHub, a workflow automatically builds the package, embedding the correct version (e.g., `1.0.0`).
-   The library provides a simple function `get_version()` to access this automatically determined version string.

## Installation

This library is intended to be installed directly from its Git tag using `pip`. It is **not** published to any public package registries like PyPI.

To install a specific version (e.g., `v1.0.0`) as a dependency in another component:

```bash
pip install https://github.com/remla25-team4/lib-version/releases/download/v1.0.0/lib_version-1.0.0-py3-none-any.whl

# Or
lib_version @ https://github.com/remla25-team4/lib-version/releases/download/v1.0.0/lib_version-1.0.0-py3-none-any.whl
# You can add this line to the requirements.txt file of your project.
```

## Usage

Once installed, you can easily get the version string in your Python code:

```python
from lib_version import *

vu = VersionUtil()
library_version = vu.get_package_version()
print(f"Using lib-version: {library_version}")
