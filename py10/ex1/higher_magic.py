from collections.abc import Callable


def fireball(target: str, power: int) -> str:
    return f"Fireball engulfs {target} for {power} damage"


def frost_bolt(target: str, power: int) -> str:
    return f"Frost bolt freezes {target} dealing {power} cold damage"


def life_drain(target: str, power: int) -> str:
    return f"Life drain siphons {power} HP from {target}"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(
    condition: Callable, spell: Callable
) -> Callable:
    def guarded(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return guarded


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> list[str]:
        return [s(target, power) for s in spells]
    return sequence


def main() -> None:
    target = "Dragon"
    base_power = 10

    print("Testing spell combiner...")
    duo = spell_combiner(fireball, frost_bolt)
    r1, r2 = duo(target, base_power)
    print(f"Combined spell result: {r1}, {r2}")

    print("\nTesting power amplifier...")
    mega = power_amplifier(fireball, 3)
    print(f"Original: {base_power}, Amplified: {base_power * 3}")
    print(f"Result: {mega(target, base_power)}")

    print("\nTesting conditional caster...")
    high_power_only = conditional_caster(
        lambda t, p: p >= 20,
        life_drain
    )
    print(f"Power 10 -> {high_power_only(target, 10)}")
    print(f"Power 25 -> {high_power_only(target, 25)}")

    print("\nTesting spell sequence...")
    combo = spell_sequence([fireball, frost_bolt, life_drain])
    results = combo(target, base_power)
    for r in results:
        print(f"  {r}")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"Higher Realm error: {exc}")
