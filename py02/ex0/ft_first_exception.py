"""Exercise 0: validate temperature readings with exceptions."""


def check_temperature(temp_str: str) -> int:
    """Convert a temperature string to int and validate it for plants."""
    try:
        temp = int(temp_str)
    except ValueError as exc:
        raise ValueError(f"'{temp_str}' is not a valid number") from exc

    if temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    if temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    return temp


def test_temperature_input() -> None:
    """Demonstrate valid and invalid temperature inputs without crashing."""
    print("=== Garden Temperature Checker ===")
    tests = ["25", "abc", "100", "-50"]

    for test in tests:
        print(f"Testing temperature: {test}")
        try:
            temp = check_temperature(test)
            print(f"Temperature {temp}°C is perfect for plants!")
        except ValueError as err:
            print(f"Error: {err}")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
