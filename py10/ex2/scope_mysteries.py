from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable:
    tally = 0

    def increment() -> int:
        nonlocal tally
        tally += 1
        return tally

    return increment


def spell_accumulator(initial_power: int) -> Callable:
    reservoir = initial_power

    def add_power(amount: int) -> int:
        nonlocal reservoir
        reservoir += amount
        return reservoir

    return add_power


def enchantment_factory(enchantment_type: str) -> Callable:
    def apply(item: str) -> str:
        return f"{enchantment_type} {item}"

    return apply


def memory_vault() -> dict[str, Callable]:
    _records: dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        _records[key] = value

    def recall(key: str) -> Any:
        if key in _records:
            return _records[key]
        return "Memory not found"

    return {"store": store, "recall": recall}


def main() -> None:
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print("\nTesting spell accumulator...")
    pool = spell_accumulator(100)
    print(f"Base 100, add 20: {pool(20)}")
    print(f"Base 100, add 30: {pool(30)}")

    print("\nTesting enchantment factory...")
    flame = enchantment_factory("Flaming")
    ice = enchantment_factory("Frozen")
    print(flame("Sword"))
    print(ice("Shield"))

    print("\nTesting memory vault...")
    vault = memory_vault()
    vault["store"]("secret", 42)
    print("Store 'secret' = 42")
    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"Memory Depths error: {exc}")
