"""Validate repository organization and run every executable example."""

from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parent
BASIC_STEM_PATTERN = re.compile(r"\d{2}_[a-z0-9_]+")
PROBLEM_STEM_PATTERN = re.compile(r"\d{4}_[a-z0-9_]+")
DOCUMENT_STEM_PATTERN = re.compile(r"[a-z0-9_]+")
SELF_CHECK_PATTERN = re.compile(r"^### Question [12]:", re.MULTILINE)
MARKDOWN_LINK_PATTERN = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
MARKDOWN_HEADING_PATTERN = re.compile(
    r"^#{1,6}\s+(.+?)\s*#*\s*$",
    re.MULTILINE,
)
REQUIRED_PROBLEM_HEADINGS = (
    "## Python Used Here",
    "## Why It Is Correct",
    "## Complexity",
    "## Assumptions to Say Aloud",
    "## Edge Cases",
    "## Possible Follow-up Questions",
    "## Test Aloud",
    "## Check Your Understanding",
)
COURSE_SECTIONS = (
    (
        "Python Basics",
        "python_basics",
        BASIC_STEM_PATTERN,
        (
            "00_setup_and_errors",
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
            "0015_3sum",
        ),
    ),
    (
        "Stacks and Queues",
        "stacks_queues",
        PROBLEM_STEM_PATTERN,
        (
            "0394_decode_string",
            "0739_daily_temperatures",
        ),
    ),
    (
        "Linked Lists",
        "linked_lists",
        PROBLEM_STEM_PATTERN,
        ("0206_reverse_linked_list",),
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
            "0875_koko_eating_bananas",
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
            "0102_binary_tree_level_order_traversal",
            "0200_number_of_islands",
            "0994_rotting_oranges",
            "0133_clone_graph",
            "0684_redundant_connection",
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
DOCUMENTATION_SECTIONS = (
    (
        "System Design",
        "system_design",
        (
            "foundational_patterns",
            "rate_limiter",
            "url_shortener",
            "image_generation_platform",
        ),
    ),
    (
        "FDE Interview",
        "fde_interview",
        (
            "01_role_and_interview_map",
            "02_customer_discovery_and_solutioning",
            "03_cloud_architecture_fundamentals",
            "04_behavioral_story_workbook",
            "05_enterprise_ai_adoption",
        ),
    ),
    (
        "AI Engineering",
        "ai_engineering",
        (
            "01_llm_product_fundamentals",
            "02_rag_systems",
            "03_model_delivery_and_evaluation",
        ),
    ),
)
REQUIRED_ROOT_FILES = (
    ".gitignore",
    "ALGORITHM_PATTERN_MAP.md",
    "INTERVIEW_PLAYBOOK.md",
    "INTERVIEW_STUDY_PLANS.md",
    "PROGRESS_TRACKER.md",
    "PYTHON_CHEAT_SHEET.md",
    "README.md",
    "verify_solutions.py",
)


def markdown_anchors(text):
    """Return the GitHub-style anchors created by Markdown headings."""
    anchors = set()
    occurrences = {}
    inside_code_fence = False

    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            inside_code_fence = not inside_code_fence
            continue
        if inside_code_fence:
            continue

        match = MARKDOWN_HEADING_PATTERN.fullmatch(line)
        if match is None:
            continue

        heading = re.sub(r"<[^>]+>", "", match.group(1))
        base = re.sub(r"[^\w\s-]", "", heading.lower())
        base = re.sub(r"\s+", "-", base.strip())
        duplicate_number = occurrences.get(base, 0)
        anchor = base if duplicate_number == 0 else f"{base}-{duplicate_number}"
        occurrences[base] = duplicate_number + 1
        anchors.add(anchor)

    return anchors


def markdown_table_cells(line):
    """Split one pipe table row while ignoring pipes inside inline code."""
    stripped = line.strip()
    if not (stripped.startswith("|") and stripped.endswith("|")):
        return None

    cells = []
    current = []
    inside_inline_code = False
    escaped = False

    for character in stripped[1:-1]:
        if escaped:
            current.append(character)
            escaped = False
        elif character == "\\":
            current.append(character)
            escaped = True
        elif character == "`":
            current.append(character)
            inside_inline_code = not inside_inline_code
        elif character == "|" and not inside_inline_code:
            cells.append("".join(current).strip())
            current = []
        else:
            current.append(character)

    cells.append("".join(current).strip())
    return cells


def inspect_markdown():
    """Return errors for broken local links and unbalanced Markdown blocks."""
    errors = []
    markdown_files = sorted(ROOT.rglob("*.md"))
    anchor_cache = {}

    for markdown_file in markdown_files:
        text = markdown_file.read_text(encoding="utf-8")
        relative_file = markdown_file.relative_to(ROOT)
        fence_count = len(re.findall(r"^\s*```", text, re.MULTILINE))

        if fence_count % 2 != 0:
            errors.append(f"unbalanced code fence in: {relative_file}")
        if text.count("<details>") != text.count("</details>"):
            errors.append(f"unbalanced details block in: {relative_file}")
        if text.count("<summary>") != text.count("</summary>"):
            errors.append(f"unbalanced summary block in: {relative_file}")

        expected_table_columns = None
        inside_code_fence = False
        for line_number, line in enumerate(text.splitlines(), start=1):
            if line.lstrip().startswith("```"):
                inside_code_fence = not inside_code_fence
                expected_table_columns = None
                continue
            if inside_code_fence:
                continue

            cells = markdown_table_cells(line)
            if cells is None:
                expected_table_columns = None
            elif expected_table_columns is None:
                expected_table_columns = len(cells)
            elif len(cells) != expected_table_columns:
                errors.append(
                    f"inconsistent table columns in {relative_file}:"
                    f"{line_number}"
                )

        for raw_target in MARKDOWN_LINK_PATTERN.findall(text):
            target = raw_target.strip()
            if target.startswith(("http://", "https://", "mailto:")):
                continue

            if target.startswith("<") and target.endswith(">"):
                target = target[1:-1]

            target = unquote(target)
            path_part, separator, fragment = target.partition("#")
            destination = (
                markdown_file
                if not path_part
                else markdown_file.parent / path_part
            )

            if destination.is_dir():
                destination = destination / "README.md"
            if not destination.exists():
                errors.append(
                    f"broken local link in {relative_file}: {raw_target}"
                )
                continue

            if separator and fragment and destination.suffix.lower() == ".md":
                destination = destination.resolve()
                if destination not in anchor_cache:
                    destination_text = destination.read_text(encoding="utf-8")
                    anchor_cache[destination] = markdown_anchors(destination_text)
                if fragment.lower() not in anchor_cache[destination]:
                    errors.append(
                        f"broken heading link in {relative_file}: {raw_target}"
                    )

    return errors


def inspect_structure():
    """Return examples in learning order and any organization errors."""
    examples_by_section = []
    errors = []
    root_readme = ROOT / "README.md"
    progress_tracker = ROOT / "PROGRESS_TRACKER.md"
    pattern_map = ROOT / "ALGORITHM_PATTERN_MAP.md"
    root_index = (
        root_readme.read_text(encoding="utf-8")
        if root_readme.is_file()
        else ""
    )
    tracker_index = (
        progress_tracker.read_text(encoding="utf-8")
        if progress_tracker.is_file()
        else ""
    )
    pattern_index = (
        pattern_map.read_text(encoding="utf-8")
        if pattern_map.is_file()
        else ""
    )

    for root_file in REQUIRED_ROOT_FILES:
        if not (ROOT / root_file).is_file():
            errors.append(f"missing root file: {root_file}")

    for section_name, folder_name, stem_pattern, ordered_stems in COURSE_SECTIONS:
        folder = ROOT / folder_name

        if not folder.is_dir():
            errors.append(f"missing course folder: {folder_name}")
            examples_by_section.append((section_name, []))
            continue

        guide_file = folder / "README.md"
        if not guide_file.is_file():
            errors.append(f"missing topic guide: {folder_name}/README.md")
            guide_index = ""
        else:
            guide_index = guide_file.read_text(encoding="utf-8")

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

        paired_stems = expected_stems & lesson_stems & example_stems

        if stem_pattern is BASIC_STEM_PATTERN:
            for position, stem in enumerate(ordered_stems):
                if stem not in paired_stems:
                    continue

                lesson_file = folder / f"{stem}.md"
                lesson_text = lesson_file.read_text(encoding="utf-8")
                solution_file = folder / f"{stem}.py"
                solution_text = solution_file.read_text(encoding="utf-8")
                relative_lesson = f"{folder_name}/{stem}.md"

                if "## Goal" not in lesson_text:
                    errors.append(f"missing Goal section in: {relative_lesson}")
                if "[Run this lesson]" not in lesson_text:
                    errors.append(f"missing run link in: {relative_lesson}")
                if "<details>" not in lesson_text:
                    errors.append(
                        f"missing hidden practice answer in: {relative_lesson}"
                    )
                if position > 0 and "Previous:" not in lesson_text:
                    errors.append(
                        f"missing previous navigation in: {relative_lesson}"
                    )
                if "Next:" not in lesson_text:
                    errors.append(f"missing next navigation in: {relative_lesson}")
                if "assert " not in solution_text:
                    errors.append(
                        f"expected a runnable assertion in: "
                        f"{folder_name}/{stem}.py"
                    )

        if stem_pattern is PROBLEM_STEM_PATTERN:
            for stem in sorted(paired_stems):
                lesson_file = folder / f"{stem}.md"
                lesson_text = lesson_file.read_text(encoding="utf-8")
                solution_file = folder / f"{stem}.py"
                solution_text = solution_file.read_text(encoding="utf-8")
                relative_lesson = f"{folder_name}/{stem}.md"

                for heading in REQUIRED_PROBLEM_HEADINGS:
                    if heading not in lesson_text:
                        errors.append(
                            f"missing lesson section in {relative_lesson}: "
                            f"{heading[3:]}"
                        )

                self_checks = SELF_CHECK_PATTERN.findall(lesson_text)
                if len(self_checks) != 2:
                    errors.append(
                        f"expected two self-checks in: {relative_lesson}"
                    )

                if "https://leetcode.com/problems/" not in lesson_text:
                    errors.append(
                        f"missing official problem link in: {relative_lesson}"
                    )

                if solution_text.count("assert ") < 3:
                    errors.append(
                        f"expected at least three assertions in: "
                        f"{folder_name}/{stem}.py"
                    )

                if f"./{relative_lesson}" not in root_index:
                    errors.append(f"lesson missing from root index: {relative_lesson}")
                if f"./{relative_lesson}" not in tracker_index:
                    errors.append(
                        f"lesson missing from progress tracker: {relative_lesson}"
                    )
                if f"./{stem}.md" not in guide_index:
                    errors.append(
                        f"lesson missing from topic guide: {relative_lesson}"
                    )
                if f"./{relative_lesson}" not in pattern_index:
                    errors.append(
                        f"lesson missing from pattern map: {relative_lesson}"
                    )

        example_files = [folder / f"{stem}.py" for stem in ordered_stems]
        examples_by_section.append((section_name, example_files))

    for section_name, folder_name, ordered_stems in DOCUMENTATION_SECTIONS:
        folder = ROOT / folder_name

        if not folder.is_dir():
            errors.append(f"missing course folder: {folder_name}")
            continue

        guide_file = folder / "README.md"
        if not guide_file.is_file():
            errors.append(f"missing topic guide: {folder_name}/README.md")
            guide_index = ""
        else:
            guide_index = guide_file.read_text(encoding="utf-8")

        discovered_stems = {
            path.stem
            for path in folder.glob("*.md")
            if path.name != "README.md"
        }
        expected_stems = set(ordered_stems)

        if len(expected_stems) != len(ordered_stems):
            errors.append(f"duplicate curriculum entry in: {folder_name}")

        for stem in sorted(expected_stems - discovered_stems):
            errors.append(f"missing documentation lesson: {folder_name}/{stem}.md")

        for stem in sorted(discovered_stems - expected_stems):
            errors.append(f"unlisted documentation lesson: {folder_name}/{stem}.md")

        for stem in sorted(discovered_stems):
            if DOCUMENT_STEM_PATTERN.fullmatch(stem) is None:
                errors.append(f"invalid documentation filename: {folder_name}/{stem}")

        for stem in sorted(expected_stems & discovered_stems):
            lesson_file = folder / f"{stem}.md"
            lesson_text = lesson_file.read_text(encoding="utf-8")
            relative_lesson = f"{folder_name}/{stem}.md"

            if len(SELF_CHECK_PATTERN.findall(lesson_text)) != 2:
                errors.append(
                    f"expected two self-checks in: {relative_lesson}"
                )

            if f"./{relative_lesson}" not in root_index:
                errors.append(f"lesson missing from root index: {relative_lesson}")
            if f"./{relative_lesson}" not in tracker_index:
                errors.append(
                    f"lesson missing from progress tracker: {relative_lesson}"
                )
            if f"./{stem}.md" not in guide_index:
                errors.append(
                    f"lesson missing from topic guide: {relative_lesson}"
                )

    errors.extend(inspect_markdown())

    return examples_by_section, errors


def main() -> int:
    """Check structure, then run each Python example in a fresh process."""
    if sys.version_info < (3, 10):
        detected = f"{sys.version_info.major}.{sys.version_info.minor}"
        print(
            f"Python {detected} detected; this repository needs Python 3.10+.",
            file=sys.stderr,
        )
        return 1

    examples_by_section, structure_errors = inspect_structure()

    if structure_errors:
        print("Repository structure errors:")
        for error in structure_errors:
            print(f"- {error}")
        return 1

    total_examples = sum(len(files) for _, files in examples_by_section)
    total_document_lessons = sum(
        len(ordered_stems)
        for _, _, ordered_stems in DOCUMENTATION_SECTIONS
    )
    print(
        "PASS repository structure "
        f"({total_examples} lesson/solution pairs; "
        f"{total_document_lessons} FDE/AI/system design lessons)."
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
