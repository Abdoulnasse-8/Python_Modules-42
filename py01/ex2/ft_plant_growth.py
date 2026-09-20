"""Simulate plant growth and aging over several consecutive days."""


class Plant:

    """Model a plant that can grow and age day by day."""

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self, cm: int) -> None:
        self.height += cm

    def age_days(self, days: int) -> None:
        self.age += days

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age} days old"


if __name__ == "__main__":
    plants = [
        Plant("Rose", 25, 30),
    ]

    print("=== Day 1 ===")
    for plant in plants:
        print(plant.get_info())

    for plant in plants:
        plant.grow(6)
        plant.age_days(6)

    print("=== Day 7 ===")
    for plant in plants:
        print(plant.get_info())
    print("Growth this week: +6cm")
