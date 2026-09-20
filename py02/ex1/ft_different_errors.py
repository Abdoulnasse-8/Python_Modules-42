"""Exercise 1: demonstrate catching common Python exceptions."""


def garden_operations() -> None:
    """Show how different exception types can be caught separately."""
    try:
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")

    try:
        _ = 1 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")

    try:
        handle = open("missing.txt", "r", encoding="utf-8")
        handle.close()
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")

    try:
        plants = {"rose": 25}
        _ = plants["missing_plant"]
    except KeyError:
        print("Caught KeyError: 'missing_plant'")


def test_error_types() -> None:
    """Run each error scenario and show the program keeps running."""
    print("=== Garden Error Types Demo ===")

    try:
        print("Testing ValueError...")
        int("abc")
    except ValueError as err:
        print(f"Caught ValueError: {err}")

    try:
        print("Testing ZeroDivisionError...")
        _ = 1 / 0
    except ZeroDivisionError as err:
        print(f"Caught ZeroDivisionError: {err}")

    try:
        print("Testing FileNotFoundError...")
        handle = open("missing.txt", "r", encoding="utf-8")
        handle.close()
    except FileNotFoundError as err:
        print(f"Caught FileNotFoundError: {err}")

    try:
        print("Testing KeyError...")
        plants = {"rose": 25}
        _ = plants["missing_plant"]
    except KeyError as err:
        print(f"Caught KeyError: {err}")

    print("Testing multiple errors together...")
    try:
        int("abc")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
