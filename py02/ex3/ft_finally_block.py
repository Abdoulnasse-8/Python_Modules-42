"""Exercise 3: demonstrate try/except/finally cleanup."""


def water_plants(plant_list: list[str | None]) -> None:
    """Water each plant, always closing the system in a finally block."""
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None or plant == "":
                raise ValueError("Cannot water None - invalid plant!")
            print(f"Watering {plant}")
    except ValueError as err:
        print(f"Error: {err}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    """Run normal and error scenarios to show cleanup always happens."""
    print("=== Garden Watering System ===")

    print("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print("Watering completed successfully!")

    print("Testing with error...")
    water_plants(["tomato", None, "carrots"])
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
