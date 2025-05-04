import importlib.metadata

# Use setuptools_scm generated file
# setuptools_scm will create/update _version.py during the build process
try:
    from ._version import __version__
except ImportError:
    # Fallback if package is not installed or _version.py not generated yet
    # Tries to get version from installed package metadata as a backup
    try:
        __version__ = importlib.metadata.version(__package__ or __name__)
    except importlib.metadata.PackageNotFoundError:
        __version__ = "0.0.0.dev0+unknown" # Default if not found

def get_version() -> str:
    """
    Returns the library's version string.

    The version is determined automatically from Git tags during the build process
    using setuptools_scm or read from installed package metadata.
    """
    return __version__

# Expose the function and potentially the version variable itself
__all__ = ["get_version", "__version__"]