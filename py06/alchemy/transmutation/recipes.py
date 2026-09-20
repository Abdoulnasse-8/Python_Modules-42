import elements as root_elements
from ..potions import strength_potion
from ..elements import create_air


def lead_to_gold() -> str:
    return (
        f"Recipe transmuting Lead to Gold: brew '{create_air()}'"
        f" and '{strength_potion()}'"
        f" mixed with '{root_elements.create_fire()}'"
    )
