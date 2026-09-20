"""Exercise 1: analyze player scores passed on the command line."""

import sys


def parse_scores(argv: list[str]) -> list[int]:
    """Parse argv strings into a list of valid integer scores."""
    scores: list[int] = []
    for raw in argv:
        try:
            scores.append(int(raw))
        except ValueError:
            print(f"Skipping invalid score: {raw}")
    return scores


def print_score_analytics(scores: list[int]) -> None:
    """Print basic statistics about a list of integer scores."""
    print("=== Player Score Analytics ===")
    if not scores:
        print(
            "No scores provided. Usage: python3 ft_score_analytics.py "
            "<score1> <score2> ..."
        )
        return

    total_players = len(scores)
    total_score = sum(scores)
    average_score = total_score / total_players
    high_score = max(scores)
    low_score = min(scores)
    score_range = high_score - low_score

    print(f"Scores processed: {scores}")
    print(f"Total players: {total_players}")
    print(f"Total score: {total_score}")
    print(f"Average score: {average_score}")
    print(f"High score: {high_score}")
    print(f"Low score: {low_score}")
    print(f"Score range: {score_range}")


def main(argv: list[str]) -> None:
    """Entry point for score analytics."""
    scores = parse_scores(argv[1:])
    print_score_analytics(scores)


if __name__ == "__main__":
    main(sys.argv)
