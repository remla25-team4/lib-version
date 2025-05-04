# lib-version

[![GitHub Actions Workflow Status](https://github.com/remla25-team4/lib-version/actions/workflows/release.yml/badge.svg)](https://github.com/remla25-team4/lib-version/actions/workflows/release.yml)

## Overview

`lib-version` is a utility library created as part of the REMLA `Restaurant Sentiment Analysis` application (Assignment 1: Versions, Releases, and Containerization).

Its primary purpose is to provide a reliable way for other components, specifically the `app-service`, to retrieve the current version of the library itself. This version information can be useful for logging, monitoring, or displaying in application information endpoints.

## How it Works

This library uses [`setuptools_scm`](https://github.com/pypa/setuptools_scm/) to automatically determine its version based on Git tags during the package build process.

-   When a release tag (e.g., `v1.0.0`) is pushed to GitHub, a workflow automatically builds the package, embedding the correct version (e.g., `1.0.0`).
-   For development commits between tags, it generates development versions (e.g., `1.0.0.post1+gHASH` or `1.0.1.dev1+gHASH`).
-   The library provides a simple function `get_version()` to access this automatically determined version string.

## Installation

This library is published to the **GitHub Packages registry** associated with this repository's organization. It is **not** published to the public PyPI.

To install this library as a dependency in another component (like `app-service`):

1.  **Configure Pip:** You need to tell `pip` to look in the GitHub Packages registry. Use `--extra-index-url` (recommended if you also use PyPI) or `--index-url`.

    ```bash
    # Example using --extra-index-url:
    pip install \
      --extra-index-url [https://pypi.pkg.github.com/remla25-team4/](https://pypi.pkg.github.com/remla25-team4/) \
      remla-lib-version==<version-tag> # e.g., remla-lib-version==0.1.0

    # Example for requirements.txt:
    # --extra-index-url [https://pypi.pkg.github.com/remla25-team4/](https://pypi.pkg.github.com/remla25-team4/)
    # remla-lib-version==0.1.0
    # other-package-from-pypi
    ```
    *(Replace `<version-tag>` with the desired released version number, e.g., `0.1.0`)*

2.  **Alternative: Install directly from Git Tag:**
    As allowed by the assignment for Python, you can also install directly from a Git tag without using GitHub Packages:
    ```bash
    pip install git+[https://github.com/remla25-team4/lib-version.git](https://github.com/remla25-team4/lib-version.git)@<tag_name>
    # e.g., pip install git+[https://github.com/remla25-team4/lib-version.git@v0.1.0](https://github.com/remla25-team4/lib-version.git@v0.1.0)
    ```
    *(Replace `<tag_name>` with the actual tag)*

## Usage

Once installed, you can easily get the version string in your Python code:

```python
from lib_version import get_version

try:
    # Get the version string provided by the library
    library_version = get_version()
    print(f"Using lib-version: {library_version}")

    # You can now use this version string, e.g., in an info endpoint:
    # return {"service": "app-service", "version": library_version}

except ImportError:
    print("Error: lib_version is not installed correctly.")
    library_version = "unknown"