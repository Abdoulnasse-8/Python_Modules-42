"""Exercise 5: integrate robust error handling in a GardenManager."""

from __future__ import annotations


class GardenError(Exception):
    """Base exception for garden management errors."""


class PlantError(GardenError):
    """Exception raised for plant-related errors."""


class WaterError(GardenError):
    """Exception raised for watering-related errors."""


class GardenManager:
    """A small garden management system with resilient operations."""

    def __init__(self) -> None:
        self._plants: dict[str, dict[str, int]] = {}
        self._water_in_tank: int = 10

    def add_plant(self, plant_name: str) -> None:
        if plant_name == "":
            raise PlantError("Plant name cannot be empty!")
        if plant_name in self._plants:
            raise PlantError(f"Plant '{plant_name}' already exists!")
        self._plants[plant_name] = {"water_level": 5, "sunlight_hours": 8}

    def refill_tank(self, amount: int) -> None:
        if amount <= 0:
            raise WaterError("Refill amount must be positive")
        self._water_in_tank += amount

    def water_plants(self) -> None:
        print("Opening watering system")
        try:
            for plant_name in self._plants:
                self.water_plant(plant_name, amount=1)
                print(f"Watering {plant_name} - success")
        finally:
            print("Closing watering system (cleanup)")

    def water_plant(self, plant_name: str, amount: int) -> None:
        if plant_name not in self._plants:
            raise PlantError(f"Unknown plant '{plant_name}'")
        if amount <= 0:
            raise WaterError("Water amount must be positive")
        if self._water_in_tank < amount:
            raise WaterError("Not enough water in tank")

        self._water_in_tank -= amount
        self._plants[plant_name]["water_level"] += amount

    def check_plant_health(
        self,
        plant_name: str,
        water_level: int | None = None,
        sunlight_hours: int | None = None,
    ) -> str:
        if plant_name == "":
            raise PlantError("Plant name cannot be empty!")
        if plant_name not in self._plants:
            raise PlantError(f"Unknown plant '{plant_name}'")

        if water_level is None:
            water_level = self._plants[plant_name]["water_level"]
        if sunlight_hours is None:
            sunlight_hours = self._plants[plant_name]["sunlight_hours"]

        if water_level < 1:
            raise WaterError(f"Water level {water_level} is too low (min 1)")
        if water_level > 10:
            raise WaterError(f"Water level {water_level} is too high (max 10)")
        if sunlight_hours < 2:
            raise PlantError(
                f"Sunlight hours {sunlight_hours} is too low (min 2)"
            )
        if sunlight_hours > 12:
            raise PlantError(
                f"Sunlight hours {sunlight_hours} is too high (max 12)"
            )

        return (
            f"{plant_name}: healthy (water: {water_level}, "
            f"sun: {sunlight_hours})"
        )


def test_garden_management() -> None:
    """Demonstrate a resilient garden management workflow."""
    manager = GardenManager()
    print("=== Garden Management System ===")

    print("Adding plants to garden...")
    for name in ("tomato", "lettuce", ""):
        try:
            manager.add_plant(name)
            print(f"Added {name} successfully")
        except PlantError as err:
            print(f"Error adding plant: {err}")

    print("Watering plants...")
    try:
        manager.water_plants()
    except GardenError as err:
        print(f"Caught GardenError during watering: {err}")

    print("Checking plant health...")
    try:
        print(manager.check_plant_health("tomato"))
    except GardenError as err:
        print(f"Error checking tomato: {err}")

    try:
        print(
            manager.check_plant_health(
                "lettuce", water_level=15, sunlight_hours=8
            )
        )
    except GardenError as err:
        print(f"Error checking lettuce: {err}")

    print("Testing error recovery...")
    try:
        manager.water_plant("tomato", amount=999)
    except GardenError as err:
        print(f"Caught GardenError: {err}")
        print("System recovered and continuing...")

    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
