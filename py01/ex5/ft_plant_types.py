"""Define specialized plant types derived from a common Plant base."""


class Plant:

    """Base class shared by all plant types."""

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):

    """Flower with a color and a bloom action."""
    def __init__(
        self, name: str, height: int, age: int, color: str
    ) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):

    """Tree with a trunk diameter and shade computation."""
    def __init__(
        self, name: str, height: int, age: int, trunk_diameter: int
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> float:
        area = (self.trunk_diameter * self.height) / 10000 * 31.2
        area = round(area)
        print(f"{self.name} provides {area} square meters of shade")
        return float(area)


class Vegetable(Plant):

    """Vegetable with harvest season and nutritional value information."""
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        harvest_season: str,
        nutritional_value: str,
    ) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def __str__(self) -> str:
        return (
            f"{self.name} is rich in {self.nutritional_value}"
        )


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    flowers = [
        Flower("Rose", 25, 30, "red"),
        Flower("Tulip", 20, 15, "yellow"),
    ]
    for f in flowers:
        print(
            f"{f.name} (Flower): {f.height}cm, {f.age} days, {f.color} color"
        )
        f.bloom()

    trees = [
        Tree("Oak", 500, 1825, 50),
        Tree("Maple", 400, 730, 40),
    ]
    for t in trees:
        print(
            f"{t.name} (Tree): {t.height}cm, {t.age} days, "
            f"{t.trunk_diameter}cm diameter"
        )
        t.produce_shade()

    vegetables = [
        Vegetable("Tomato", 80, 90, "summer", "vitamin C"),
        Vegetable("Carrot", 30, 60, "fall", "vitamin A"),
    ]
    for v in vegetables:
        print(
            f"{v.name} (Vegetable): {v.height}cm, {v.age} days, "
            f"{v.harvest_season} harvest"
        )
        print(v)
