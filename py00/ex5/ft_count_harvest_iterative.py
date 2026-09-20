def ft_count_harvest_iterative() -> None:
    days_until = int(input("Days until harvest: "))
    for day in range(1, days_until + 1):
        print(f"Day {day}")
    print("Harvest time!")
