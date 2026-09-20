"""Exercise 0: basic command-line argument inspection with sys.argv."""

import sys


def command_quest(argv: list[str]) -> None:
    """Display program name and received command-line arguments."""
    print("=== Command Quest ===")
    program_name = argv[0] if argv else ""
    total_args = len(argv)
    args_only = argv[1:] if len(argv) > 1 else []

    if not args_only:
        print("No arguments provided!")
        print(f"Program name: {program_name}")
        print(f"Total arguments: {total_args}")
        return

    print(f"Program name: {program_name}")
    print(f"Arguments received: {len(args_only)}")
    for idx, value in enumerate(args_only, start=1):
        print(f"Argument {idx}: {value}")
    print(f"Total arguments: {total_args}")


if __name__ == "__main__":
    command_quest(sys.argv)
