"""Lesson 0: check Python, locate the repository, and run a tiny test."""

from pathlib import Path
import sys


MINIMUM_PYTHON = (3, 10)
REPOSITORY_ROOT = Path(__file__).resolve().parent.parent


def version_is_supported(version):
    """Return True when a major/minor version can run every course file."""
    return tuple(version[:2]) >= MINIMUM_PYTHON


if __name__ == "__main__":
    detected = sys.version_info[:2]
    detected_text = f"{detected[0]}.{detected[1]}"

    print(f"Python {detected_text} detected.")

    if not version_is_supported(detected):
        print("This course needs Python 3.10 or newer.")
        print("Install a newer Python version, then run this file again.")
        raise SystemExit(1)

    assert version_is_supported((3, 10)) is True
    assert version_is_supported((3, 9)) is False
    assert (REPOSITORY_ROOT / "README.md").is_file()
    assert (REPOSITORY_ROOT / "verify_solutions.py").is_file()
    assert 2 + 3 == 5

    print("Repository files found.")
    print("Tiny assertion passed.")
    print("Setup is ready. Continue to Lesson 1.")
