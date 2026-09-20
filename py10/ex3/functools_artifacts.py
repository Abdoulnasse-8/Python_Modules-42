import functools
import operator
from collections.abc import Callable
from typing import Any


def base_enchant(power: int, element: str, target: str) -> str:
    return f"{target} receives a {element} enchantment of strength {power}"


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    ops: dict[str, Callable] = {
        "add":      operator.add,
        "multiply": operator.mul,
        "max":      max,
        "min":      min,
    }

    if operation not in ops:
        raise ValueError(f"Unknown operation: '{operation}'")

    return functools.reduce(ops[operation], spells)


def partial_enchanter(
    base_enchantment: Callable
) -> dict[str, Callable]:
    preset_power = 50
    return {
        "fire":  functools.partial(base_enchantment, preset_power, "fire"),
        "frost": functools.partial(base_enchantment, preset_power, "frost"),
        "storm": functools.partial(base_enchantment, preset_power, "storm"),
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def cast(spell: Any) -> str:
        return "Unknown spell type"

    @cast.register(int)
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @cast.register(str)
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @cast.register(list)
    def _(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return cast


def main() -> None:
    values = [10, 20, 30, 40]

    print("Testing spell reducer...")
    print(f"Sum: {spell_reducer(values, 'add')}")
    print(f"Product: {spell_reducer(values, 'multiply')}")
    print(f"Max: {spell_reducer(values, 'max')}")

    print("\nTesting partial enchanter...")
    variants = partial_enchanter(base_enchant)
    print(variants["fire"]("Excalibur"))
    print(variants["frost"]("Tower Shield"))
    print(variants["storm"]("Longbow"))

    print("\nTesting memoized fibonacci...")
    for idx in (0, 1, 10, 15):
        print(f"Fib({idx}): {memoized_fibonacci(idx)}")
    print(f"Cache info: {memoized_fibonacci.cache_info()}")

    print("\nTesting spell dispatcher...")
    dispatch = spell_dispatcher()
    print(dispatch(42))
    print(dispatch("fireball"))
    print(dispatch(["fire", "ice", "bolt"]))
    print(dispatch(3.14))


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"Ancient Library error: {exc}")
