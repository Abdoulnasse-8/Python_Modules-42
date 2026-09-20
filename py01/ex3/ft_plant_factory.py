"""Create several Plant instances and display their initial state."""


class Plant:

    """Represent a plant produced by the factory script."""

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def __str__(self) -> str:
        return f"{self.name} ({self.height}cm, {self.age} days)"


if __name__ == "__main__":
    plants = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120),
    ]

    print("=== Plant Factory Output ===")
    for plant in plants:
        print(f"Created: {plant}")
    print(f"Total plants created: {len(plants)}")
