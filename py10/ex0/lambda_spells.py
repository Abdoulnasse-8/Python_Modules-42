def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda a: a["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda m: m["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    powers = list(map(lambda m: m["power"], mages))
    return {
        "max_power": max(powers),
        "min_power": min(powers),
        "avg_power": round(sum(powers) / len(powers), 2),
    }


def main() -> None:
    artifacts = [
        {"name": "Fire Staff", "power": 92, "type": "weapon"},
        {"name": "Crystal Orb", "power": 85, "type": "relic"},
        {"name": "Iron Shield", "power": 40, "type": "armor"},
        {"name": "Thunder Bow", "power": 77, "type": "weapon"},
    ]

    mages = [
        {"name": "Aldric", "power": 55, "element": "earth"},
        {"name": "Seraphine", "power": 88, "element": "fire"},
        {"name": "Kael", "power": 72, "element": "wind"},
        {"name": "Thessaly", "power": 91, "element": "water"},
        {"name": "Dorian", "power": 63, "element": "shadow"},
    ]

    spells = ["fireball", "heal", "shield"]

    print("Testing artifact sorter...")
    ranked = artifact_sorter(artifacts)
    first, second = ranked[0], ranked[1]
    print(
        f"{first['name']} ({first['power']} power)"
        f" comes before {second['name']} ({second['power']} power)"
    )

    print("\nTesting power filter...")
    elite = power_filter(mages, 70)
    names = list(map(lambda m: m["name"], elite))
    print("Mages with power >= 70:", ", ".join(names))

    print("\nTesting spell transformer...")
    print(" ".join(spell_transformer(spells)))

    print("\nTesting mage stats...")
    stats = mage_stats(mages)
    print(
        f"max={stats['max_power']}"
        f"  min={stats['min_power']}"
        f"  avg={stats['avg_power']}"
    )


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"Sanctum error: {exc}")
