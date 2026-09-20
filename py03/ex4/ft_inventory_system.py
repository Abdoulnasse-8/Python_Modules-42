"""Exercise 4: analyze an RPG inventory using dictionaries."""

import sys


def parse_inventory(argv: list[str]) -> dict[str, int]:
    """Parse items like 'potion:5' into a dict of item -> quantity."""
    inventory: dict[str, int] = {}
    for raw in argv:
        if ":" not in raw:
            print(f"Skipping invalid item format: {raw}")
            continue
        name, qty_str = raw.split(":", 1)
        if name == "":
            print(f"Skipping invalid item name: {raw}")
            continue
        try:
            qty = int(qty_str)
        except ValueError:
            print(f"Skipping invalid quantity: {raw}")
            continue
        if qty < 0:
            print(f"Skipping negative quantity: {raw}")
            continue

        current = inventory.get(name, 0)
        inventory.update({name: current + qty})
    return inventory


def categorize_items(inventory: dict[str, int]) -> dict[str, dict[str, int]]:
    """Group items by abundance category using a nested dict."""
    categories: dict[str, dict[str, int]] = {"Moderate": {}, "Scarce": {}}
    for name, qty in inventory.items():
        if qty >= 5:
            categories["Moderate"][name] = qty
        else:
            categories["Scarce"][name] = qty
    return categories


def print_inventory_report(inventory: dict[str, int]) -> None:
    """Print an inventory analysis using dict methods."""
    print("=== Inventory System Analysis ===")
    total_units = sum(inventory.values()) if inventory else 0
    print(f"Total items in inventory: {total_units}")
    print(f"Unique item types: {len(inventory)}")

    print("=== Current Inventory ===")
    if total_units == 0:
        print("Inventory is empty.")
    else:
        sorted_items = sorted(
            inventory.items(),
            key=lambda it: it[1],
            reverse=True,
        )
        for name, qty in sorted_items:
            percent = (qty / total_units) * 100
            print(f"{name}: {qty} units ({percent:.1f}%)")

    print("=== Inventory Statistics ===")
    if inventory:
        most_name = max(inventory, key=lambda k: inventory[k])
        least_name = min(inventory, key=lambda k: inventory[k])
        print(f"Most abundant: {most_name} ({inventory[most_name]} units)")
        print(f"Least abundant: {least_name} ({inventory[least_name]} units)")
    else:
        print("Most abundant: N/A")
        print("Least abundant: N/A")

    print("=== Item Categories ===")
    categories = categorize_items(inventory)
    print(f"Moderate: {categories.get('Moderate')}")
    print(f"Scarce: {categories.get('Scarce')}")

    print("=== Management Suggestions ===")
    restock = [name for name, qty in inventory.items() if qty <= 1]
    if restock:
        print(f"Restock needed: {', '.join(restock)}")
    else:
        print("Restock needed: none")

    print("=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {', '.join(inventory.keys())}")
    values_str = ", ".join(str(v) for v in inventory.values())
    print(f"Dictionary values: {values_str}")
    sample = "sword"
    exists = inventory.get(sample) is not None
    print(f"Sample lookup- '{sample}' in inventory: {exists}")


def main(argv: list[str]) -> None:
    """Entry point for inventory analytics."""
    inventory = parse_inventory(argv[1:])
    print_inventory_report(inventory)


if __name__ == "__main__":
    main(sys.argv)
