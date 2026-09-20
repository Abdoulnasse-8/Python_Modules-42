from typing import List, Tuple, Any
from ex0 import FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
    BattleStrategy,
)


Opponent = Tuple[Any, BattleStrategy]


def battle(opponents: List[Opponent]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            factory1, strategy1 = opponents[i]
            factory2, strategy2 = opponents[j]

            c1 = factory1.create_base()
            c2 = factory2.create_base()

            print()
            print("* Battle *")
            print(c1.describe())
            print("vs.")
            print(c2.describe())
            print("now fight!")

            if not strategy1.is_valid(c1):
                print(
                    "Battle error, aborting tournament: "
                    f"invalid strategy for {c1.name}"
                )
                return

            if not strategy2.is_valid(c2):
                print(
                    "Battle error, aborting tournament: "
                    f"invalid strategy for {c2.name}"
                )
                return

            strategy1.act(c1)
            strategy2.act(c2)


if __name__ == "__main__":
    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    flame = FlameFactory()
    aqua = AquaFactory()
    healing = HealingCreatureFactory()
    transform = TransformCreatureFactory()

    print("Tournament 0 (basic)")
    print(" [ (Flameling+Normal), (Healing+Defensive) ]")
    battle([(flame, normal), (healing, defensive)])

    print()
    print("Tournament 1 (error)")
    print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle([(flame, aggressive), (healing, defensive)])

    print()
    print("Tournament 2 (multiple)")
    print(
        " [ (Aquabub+Normal), (Healing+Defensive), "
        "(Transform+Aggressive) ]"
    )
    battle([(aqua, normal), (healing, defensive), (transform, aggressive)])
