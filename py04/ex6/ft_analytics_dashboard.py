"""Exercise 6: demonstrate comprehensions for analytics transformations."""


def main() -> None:
    """Print examples of list/dict/set comprehensions and simple analytics."""
    print("=== Game Analytics Dashboard ===")

    players = ["alice", "bob", "charlie", "diana"]
    scores = {"alice": 2300, "bob": 1800, "charlie": 2150, "diana": 2050}
    active = {"alice", "bob", "charlie"}
    regions = {
        "alice": "north",
        "bob": "east",
        "charlie": "central",
        "diana": "east",
    }
    achievements = {
        "alice": {
            "first_kill",
            "level_10",
            "boss_slayer",
            "collector",
            "speed_demon",
        },
        "bob": {"first_kill", "level_10", "collector"},
        "charlie": {
            "first_kill",
            "level_10",
            "boss_slayer",
            "treasure_hunter",
            "perfectionist",
            "speed_demon",
            "speed_runner",
        },
        "diana": {"first_kill", "level_10"},
    }

    print("=== List Comprehension Examples ===")
    high_scorers = [p for p, s in scores.items() if s > 2000]
    print(f"High scorers (>2000): {high_scorers}")

    scores_doubled = [s * 2 for s in scores.values()]
    print(f"Scores doubled: {scores_doubled}")

    active_players = [p for p in players if p in active]
    print(f"Active players: {active_players}")

    print("=== Dict Comprehension Examples ===")
    player_scores = {p: scores[p] for p in players if p in scores}
    print(f"Player scores: {player_scores}")

    score_categories = {
        "high": len([s for s in scores.values() if s > 2000]),
        "medium": len([s for s in scores.values() if 1500 <= s <= 2000]),
        "low": len([s for s in scores.values() if s < 1500]),
    }
    print(f"Score categories: {score_categories}")

    achievement_counts = {p: len(a) for p, a in achievements.items()}
    print(f"Achievement counts: {achievement_counts}")

    print("=== Set Comprehension Examples ===")
    unique_players = {p for p in players}
    print(f"Unique players: {unique_players}")

    unique_achievements = {a for ach in achievements.values() for a in ach}
    print(f"Unique achievements: {unique_achievements}")

    active_regions = {regions[p] for p in active if p in regions}
    print(f"Active regions: {active_regions}")

    print("=== Combined Analysis ===")
    total_players = len(players)
    total_unique_ach = len(unique_achievements)
    average_score = sum(scores.values()) / len(scores) if scores else 0.0
    top_player = max(scores, key=lambda p: scores[p])
    top_score = scores[top_player]
    top_ach = achievement_counts.get(top_player, 0)

    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {total_unique_ach}")
    print(f"Average score: {average_score}")
    print(
        f"Top performer: {top_player} ({top_score} points, "
        f"{top_ach} achievements)"
    )


if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        print(f"Error: {err}")
