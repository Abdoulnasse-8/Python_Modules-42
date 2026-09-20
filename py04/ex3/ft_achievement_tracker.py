"""Exercise 3: track unique achievements using sets and set operations."""


def print_set(label: str, values: set[str]) -> None:
    """Print a set with a label."""
    print(f"{label}: {values}")


def rare_achievements(players: dict[str, set[str]]) -> set[str]:
    """Return achievements owned by exactly one player."""
    counts: dict[str, int] = {}
    for ach_set in players.values():
        for ach in ach_set:
            counts[ach] = counts.get(ach, 0) + 1
    return {ach for ach, count in counts.items() if count == 1}


def main() -> None:
    """Demonstrate set deduplication and analytics with set operations."""
    print("=== Achievement Tracker System ===")

    players: dict[str, set[str]] = {
        "alice": {"first_kill", "level_10", "treasure_hunter", "speed_demon"},
        "bob": {"first_kill", "level_10", "boss_slayer", "collector"},
        "charlie": {
            "level_10",
            "treasure_hunter",
            "boss_slayer",
            "speed_demon",
            "perfectionist",
        },
    }

    for name, ach in players.items():
        print_set(f"Player {name} achievements", ach)

    print("=== Achievement Analytics ===")

    all_unique: set[str] = set()
    for ach in players.values():
        all_unique = all_unique.union(ach)
    print_set("All unique achievements", all_unique)
    print(f"Total unique achievements: {len(all_unique)}")

    common_to_all = (
        players["alice"]
        .intersection(players["bob"])
        .intersection(players["charlie"])
    )
    print_set("Common to all players", common_to_all)

    rare = rare_achievements(players)
    print_set("Rare achievements (1 player)", rare)

    alice_bob_common = players["alice"].intersection(players["bob"])
    print_set("Alice vs Bob common", alice_bob_common)

    alice_unique = players["alice"].difference(players["bob"])
    print_set("Alice unique", alice_unique)

    bob_unique = players["bob"].difference(players["alice"])
    print_set("Bob unique", bob_unique)


if __name__ == "__main__":
    main()
