from ex0 import FlameFactory, AquaFactory
from typing import Protocol


class FactoryProtocol(Protocol):
    def create_base(self): ...
    def create_evolved(self): ...


def test_factory(factory: FactoryProtocol) -> None:
    print("Testing factory")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())


def test_battle(factory1: FactoryProtocol, factory2: FactoryProtocol) -> None:
    print("Testing battle")
    c1 = factory1.create_base()
    c2 = factory2.create_base()
    print(c1.describe())
    print("vs.")
    print(c2.describe())
    print("fight!")
    print(c1.attack())
    print(c2.attack())


if __name__ == "__main__":
    flame = FlameFactory()
    aqua = AquaFactory()

    test_factory(flame)
    print()
    test_factory(aqua)
    print()
    test_battle(flame, aqua)
