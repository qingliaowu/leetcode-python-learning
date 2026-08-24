"""Validate repository organization and run every executable example."""

from pathlib import Path
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parent
BASIC_STEM_PATTERN = re.compile(r"\d{2}_[a-z0-9_]+")
PROBLEM_STEM_PATTERN = re.compile(r"\d{4}_[a-z0-9_]+")
SYSTEM_DESIGN_STEM_PATTERN = re.compile(r"[a-z0-9_]+")
COURSE_SECTIONS = (
    (
        "Python Basics",
        "python_basics",
        BASIC_STEM_PATTERN,
        (
            "01_first_program",
            "02_variables_and_values",
            "03_strings",
            "04_lists_and_tuples",
            "05_dictionaries_and_sets",
            "06_conditions_and_loops",
            "07_functions",
            "08_classes_and_objects",
            "09_recursion",
            "10_python_for_leetcode",
            "11_time_and_space_complexity",
        ),
    ),
    (
        "Arrays, Strings, and Hash Maps",
        "arrays_strings",
        PROBLEM_STEM_PATTERN,
        (
            "0001_two_sum",
            "0049_group_anagrams",
            "0003_longest_substring_without_repeating_characters",
        ),
    ),
    (
        "Stacks and Queues",
        "stacks_queues",
        PROBLEM_STEM_PATTERN,
        ("0394_decode_string",),
    ),
    (
        "Intervals and Binary Search",
        "intervals_search",
        PROBLEM_STEM_PATTERN,
        (
            "0056_merge_intervals",
            "0253_meeting_rooms_ii",
            "0704_binary_search",
            "0033_search_in_rotated_sorted_array",
        ),
    ),
    (
        "Data Structure Design",
        "design_data_structures",
        PROBLEM_STEM_PATTERN,
        (
            "0981_time_based_key_value_store",
            "0146_lru_cache",
        ),
    ),
    (
        "Trees and Graphs",
        "trees_graphs",
        PROBLEM_STEM_PATTERN,
        (
            "0200_number_of_islands",
            "0133_clone_graph",
            "0207_course_schedule",
        ),
    ),
    (
        "Heaps and Top-K",
        "heaps",
        PROBLEM_STEM_PATTERN,
        (
            "0215_kth_largest_element",
            "0347_top_k_frequent_elements",
            "0023_merge_k_sorted_lists",
        ),
    ),
    (
        "Prefix Sums and Backtracking",
        "prefix_recursion",
        PROBLEM_STEM_PATTERN,
        (
            "0560_subarray_sum_equals_k",
            "0079_word_search",
        ),
    ),
    (
        "Trie",
        "trie",
        PROBLEM_STEM_PATTERN,
        (
            "0208_implement_trie",
            "1268_search_suggestions_system",
            "0211_design_add_and_search_words",
            "0648_replace_words",
            "0677_map_sum_pairs",
        ),
    ),
    (
        "Dynamic Programming",
        "dynamic_programming",
        PROBLEM_STEM_PATTERN,
        (
            "0198_house_robber",
            "0322_coin_change",
            "0300_longest_increasing_subsequence",
        ),
    ),
)
SYSTEM_DESIGN_SECTIONS = (
    (
        "System Design",
        "system_design",
        ("image_generation_platform",),
    ),
)
REQUIRED_ROOT_FILES = (
    ".gitignore",
    "INTERVIEW_PLAYBOOK.md",
    "INTERVIEW_STUDY_PLANS.md",
    "PROGRESS_TRACKER.md",
    "README.md",
    "verify_solutions.py",
)


def inspect_structure():
    """Return examples in learning order and any organization errors."""
    examples_by_section = []
    errors = []

    for root_file in REQUIRED_ROOT_FILES:
        if not (ROOT / root_file).is_file():
            errors.append(f"missing root file: {root_file}")

    for section_name, folder_name, stem_pattern, ordered_stems in COURSE_SECTIONS:
        folder = ROOT / folder_name

        if not folder.is_dir():
            errors.append(f"missing course folder: {folder_name}")
            examples_by_section.append((section_name, []))
            continue

        if not (folder / "README.md").is_file():
            errors.append(f"missing topic guide: {folder_name}/README.md")

        discovered_example_files = sorted(folder.glob("*.py"))
        lesson_files = sorted(
            path for path in folder.glob("*.md") if path.name != "README.md"
        )
        example_stems = {path.stem for path in discovered_example_files}
        lesson_stems = {path.stem for path in lesson_files}
        discovered_stems = example_stems | lesson_stems
        expected_stems = set(ordered_stems)

        if len(expected_stems) != len(ordered_stems):
            errors.append(f"duplicate curriculum entry in: {folder_name}")

        for stem in sorted(lesson_stems - example_stems):
            errors.append(f"missing Python solution: {folder_name}/{stem}.py")

        for stem in sorted(example_stems - lesson_stems):
            errors.append(f"missing Markdown lesson: {folder_name}/{stem}.md")

        for stem in sorted(expected_stems - discovered_stems):
            errors.append(f"missing curriculum lesson: {folder_name}/{stem}")

        for stem in sorted(discovered_stems - expected_stems):
            errors.append(f"unlisted curriculum lesson: {folder_name}/{stem}")

        for stem in sorted(discovered_stems):
            if stem_pattern.fullmatch(stem) is None:
                errors.append(f"invalid lesson filename: {folder_name}/{stem}")

        example_files = [folder / f"{stem}.py" for stem in ordered_stems]
        examples_by_section.append((section_name, example_files))

    for section_name, folder_name, ordered_stems in SYSTEM_DESIGN_SECTIONS:
        folder = ROOT / folder_name

        if not folder.is_dir():
            errors.append(f"missing course folder: {folder_name}")
            continue

        if not (folder / "README.md").is_file():
            errors.append(f"missing topic guide: {folder_name}/README.md")

        discovered_stems = {
            path.stem
            for path in folder.glob("*.md")
            if path.name != "README.md"
        }
        expected_stems = set(ordered_stems)

        if len(expected_stems) != len(ordered_stems):
            errors.append(f"duplicate curriculum entry in: {folder_name}")

        for stem in sorted(expected_stems - discovered_stems):
            errors.append(f"missing system design case: {folder_name}/{stem}.md")

        for stem in sorted(discovered_stems - expected_stems):
            errors.append(f"unlisted system design case: {folder_name}/{stem}.md")

        for stem in sorted(discovered_stems):
            if SYSTEM_DESIGN_STEM_PATTERN.fullmatch(stem) is None:
                errors.append(f"invalid system design filename: {folder_name}/{stem}")

    return examples_by_section, errors


def main() -> int:
    """Check structure, then run each Python example in a fresh process."""
    examples_by_section, structure_errors = inspect_structure()

    if structure_errors:
        print("Repository structure errors:")
        for error in structure_errors:
            print(f"- {error}")
        return 1

    total_examples = sum(len(files) for _, files in examples_by_section)
    total_design_cases = sum(
        len(ordered_stems)
        for _, _, ordered_stems in SYSTEM_DESIGN_SECTIONS
    )
    design_case_label = (
        "case study" if total_design_cases == 1 else "case studies"
    )
    print(
        "PASS repository structure "
        f"({total_examples} lesson/solution pairs; "
        f"{total_design_cases} system design {design_case_label})."
    )

    failures = []

    for section_name, example_files in examples_by_section:
        print(f"\n== {section_name} ==")

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

    passed = total_examples - len(failures)
    print(f"\n{passed}/{total_examples} Python files passed.")

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
