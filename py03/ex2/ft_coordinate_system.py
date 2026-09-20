"""Exercise 2: work with 3D coordinates using tuples."""

import math
import sys


def distance_3d(
    p1: tuple[float, float, float],
    p2: tuple[float, float, float],
) -> float:
    """Return Euclidean distance between two 3D points."""
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def parse_position(raw: str) -> tuple[int, int, int]:
    """Parse a coordinate string like '3,4,0' into a 3D integer tuple."""
    parts = raw.split(",")
    if len(parts) != 3:
        raise ValueError("Expected 3 comma-separated values")
    x_str, y_str, z_str = parts
    return (int(x_str), int(y_str), int(z_str))


def main(argv: list[str]) -> None:
    """Demonstrate tuple creation, parsing, distance, and unpacking."""
    print("=== Game Coordinate System ===")

    position = (10, 20, 5)
    print(f"Position created: {position}")
    origin = (0.0, 0.0, 0.0)
    pos_f = (float(position[0]), float(position[1]), float(position[2]))
    dist = distance_3d(origin, pos_f)
    print(f"Distance between (0, 0, 0) and {position}: {dist:.2f}")

    raw = argv[1] if len(argv) > 1 else "3,4,0"
    print(f'Parsing coordinates: "{raw}"')
    try:
        parsed = parse_position(raw)
        print(f"Parsed position: {parsed}")
        parsed_f = (float(parsed[0]), float(parsed[1]), float(parsed[2]))
        dist2 = distance_3d(origin, parsed_f)
        print(f"Distance between (0, 0, 0) and {parsed}: {dist2}")
    except Exception as err:
        print(f"Error parsing coordinates: {err}")
        print(f"Error details- Type: {type(err).__name__}, Args: {err.args}")

    print("Unpacking demonstration:")
    try:
        x, y, z = parse_position("3,4,0")
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")
    except ValueError as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    main(sys.argv)
