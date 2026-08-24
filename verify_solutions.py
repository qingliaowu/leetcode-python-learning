"""Run every executable solution example in this repository."""

from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).parent
TOPIC_FOLDERS = (
    "arrays_strings",
    "heaps",
    "intervals_search",
    "prefix_recursion",
    "trees_graphs",
    "trie",
)


def main() -> int:
    """Run each solution in a fresh Python process and report failures."""
    solution_files = []

    for folder_name in TOPIC_FOLDERS:
        folder = ROOT / folder_name
        solution_files.extend(sorted(folder.glob("*.py")))

    failures = []

    for solution_file in solution_files:
        relative_path = solution_file.relative_to(ROOT)
        result = subprocess.run(
            [sys.executable, str(solution_file)],
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

    passed = len(solution_files) - len(failures)
    print(f"\n{passed}/{len(solution_files)} solution files passed.")

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
