def ft_count_harvest_recursive() -> None:
    days_until = int(input("Days until harvest: "))

    def _print_day(day: int) -> None:
        if day > days_until:
            print("Harvest time!")
            return
        print(f"Day {day}")
        _print_day(day + 1)

    _print_day(1)
