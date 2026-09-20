"""Exercise 5: process data with generators (streaming, constant memory)."""

from __future__ import annotations

from typing import Generator


def game_event_stream(count: int) -> Generator[dict[str, object], None, None]:
    """Yield synthetic game events one by one."""
    players = ["alice", "bob", "charlie", "diana"]
    event_types = ["killed monster", "found treasure", "leveled up"]
    levels = [5, 12, 8, 15]

    for i in range(count):
        idx = i % len(players)
        yield {
            "id": i + 1,
            "player": players[idx],
            "level": levels[idx],
            "type": event_types[i % len(event_types)],
        }


def fibonacci() -> Generator[int, None, None]:
    """Generate the infinite Fibonacci sequence."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def is_prime(n: int) -> bool:
    """Return True if n is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def prime_numbers() -> Generator[int, None, None]:
    """Generate the infinite prime number sequence."""
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1


def main() -> None:
    """Demonstrate event streaming analytics and generator examples."""
    print("=== Game Data Stream Processor ===")

    total_events = 1000
    print(f"Processing {total_events} game events...")

    processed = 0
    high_level = 0
    treasure_events = 0
    level_up_events = 0

    for event in game_event_stream(total_events):
        processed += 1

        player = str(event.get("player"))
        level = int(event.get("level", 0))
        event_type = str(event.get("type"))

        if processed <= 3:
            print(
                f"Event {processed}: Player {player} (level {level}) "
                f"{event_type}"
            )
        if processed == 4:
            print("...")

        if level >= 10:
            high_level += 1
        if event_type == "found treasure":
            treasure_events += 1
        if event_type == "leveled up":
            level_up_events += 1

    print("=== Stream Analytics ===")
    print(f"Total events processed: {processed}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {level_up_events}")
    print("Memory usage: Constant (streaming)")

    print("=== Generator Demonstration ===")
    fib = fibonacci()
    first_10_fib = [str(next(fib)) for _ in range(10)]
    print(f"Fibonacci sequence (first 10): {', '.join(first_10_fib)}")

    primes = prime_numbers()
    first_5_primes = [str(next(primes)) for _ in range(5)]
    print(f"Prime numbers (first 5): {', '.join(first_5_primes)}")


if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        print(f"Error: {err}")
