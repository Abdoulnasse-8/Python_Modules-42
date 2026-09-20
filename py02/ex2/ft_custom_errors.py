"""Exercise 2: custom exception types for garden problems."""


class GardenError(Exception):
    """Base exception for garden-related errors."""


class PlantError(GardenError):
    """Exception raised for plant-related issues."""


class WaterError(GardenError):
    """Exception raised for watering-related issues."""


def raise_plant_error(plant_name: str) -> None:
    """Raise a PlantError for demonstration purposes."""
    raise PlantError(f"The {plant_name} plant is wilting!")


def raise_water_error() -> None:
    """Raise a WaterError for demonstration purposes."""
    raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    """Demonstrate raising and catching custom garden exceptions."""
    print("=== Custom Garden Errors Demo ===")

    print("Testing PlantError...")
    try:
        raise_plant_error("tomato")
    except PlantError as err:
        print(f"Caught PlantError: {err}")

    print("Testing WaterError...")
    try:
        raise_water_error()
    except WaterError as err:
        print(f"Caught WaterError: {err}")

    print("Testing catching all garden errors...")
    for action in ("plant", "water"):
        try:
            if action == "plant":
                raise_plant_error("tomato")
            else:
                raise_water_error()
        except GardenError as err:
            print(f"Caught a garden error: {err}")

    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
