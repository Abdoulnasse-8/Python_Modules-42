"""Secure plant model that validates height and age assignments."""


class SecurePlant:

    """Protect plant data using validated getters and setters."""

    def __init__(self, name: str) -> None:
        self._name = name
        self._height: int = 0
        self._age: int = 0

    def get_height(self) -> int:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, value: int) -> bool:
        if value < 0:
            print(f"Invalid operation attempted: height {value}cm [REJECTED]")
            print("Security: Negative height rejected")
            return False
        self._height = value
        print(f"Height updated: {value}cm [OK]")
        return True

    def set_age(self, value: int) -> bool:
        if value < 0:
            print(f"Invalid operation attempted: age {value} days [REJECTED]")
            print("Security: Negative age rejected")
            return False
        self._age = value
        print(f"Age updated: {value} days [OK]")
        return True

    def __str__(self) -> str:
        return f"{self._name} ({self._height}cm, {self._age} days)"


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose")
    print(f"Plant created: {plant._name}")

    plant.set_height(25)
    plant.set_age(30)
    plant.set_height(-5)
    print(f"Current plant: {plant}")
