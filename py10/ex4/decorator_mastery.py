import time
import functools
from collections.abc import Callable
from typing import Any


def spell_timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start = time.perf_counter()
        outcome = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"Spell completed in {elapsed:.3f} seconds")
        return outcome
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            lvl = next(
                (a for a in args if isinstance(a, int)), None
            )
            if lvl is None or lvl < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            f"Spell failed, retrying..."
                            f" (attempt {attempt}/{max_attempts})"
                        )
            return (
                f"Spell casting failed after {max_attempts} attempts"
            )
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return (
            isinstance(name, str)
            and len(name) >= 3
            and all(ch.isalpha() or ch.isspace() for ch in name)
        )

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


@spell_timer
def invoke_lightning() -> str:
    time.sleep(0.101)
    return "Lightning summoned!"


@retry_spell(max_attempts=3)
def unstable_portal(stable: bool) -> str:
    if not stable:
        raise RuntimeError("Portal collapsed")
    return "Waaaaaaagh spelled !"


@power_validator(min_power=25)
def arcane_blast(power: int, target: str) -> str:
    return f"Arcane blast hits {target} for {power} damage"


def main() -> None:
    print("Testing spell timer...")
    result = invoke_lightning()
    print(f"Result: {result}")

    print("\nTesting retrying spell...")
    print(unstable_portal(False))
    print(unstable_portal(True))

    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name("Aldric"))
    print(MageGuild.validate_mage_name("X9"))
    guild = MageGuild()
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 5))

    print("\nTesting power validator standalone...")
    print(arcane_blast(30, "Wraith"))
    print(arcane_blast(10, "Wraith"))


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"Master Tower error: {exc}")
