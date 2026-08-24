"""Run every executable course and solution example in this repository."""

from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).parent
EXAMPLE_FOLDERS = (
    "arrays_strings",
    "dynamic_programming",
    "heaps",
    "intervals_search",
    "prefix_recursion",
    "python_basics",
    "trees_graphs",
    "trie",
)


def main() -> int:
    """Run each Python example in a fresh process and report failures."""
    example_files = []

    for folder_name in EXAMPLE_FOLDERS:
        folder = ROOT / folder_name
        example_files.extend(sorted(folder.glob("*.py")))

    failures = []

    for example_file in example_files:
        relative_path = example_file.relative_to(ROOT)
        result = subprocess.run(
            [sys.executable, str(example_file)],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )

        if result.returncode == 0:
            print(f"PASS {relative_path}")
        else:
            failures.append(relative_path)
            print(f"FAIL {relative_path}")
            if result.stdout:
                print(result.stdout.rstrip())
            if result.stderr:
                print(result.stderr.rstrip())

    passed = len(example_files) - len(failures)
    print(f"\n{passed}/{len(example_files)} Python files passed.")

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
