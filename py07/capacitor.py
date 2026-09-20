from ex1 import HealingCreatureFactory, TransformCreatureFactory


def test_healing_factory(factory) -> None:
    print("Testing Creature with healing capability")

    print("base:")
    c = factory.create_base()
    print(c.describe())
    print(c.attack())
    print(c.heal())

    print("evolved:")
    c = factory.create_evolved()
    print(c.describe())
    print(c.attack())
    print(c.heal())


def test_transform_factory(factory) -> None:
    print("Testing Creature with transform capability")

    print("base:")
    c = factory.create_base()
    print(c.describe())
    print(c.attack())
    print(c.transform())
    print(c.attack())
    print(c.revert())

    print("evolved:")
    c = factory.create_evolved()
    print(c.describe())
    print(c.attack())
    print(c.transform())
    print(c.attack())
    print(c.revert())


if __name__ == "__main__":
    test_healing_factory(HealingCreatureFactory())
    print()
    test_transform_factory(TransformCreatureFactory())
