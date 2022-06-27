from collections import Counter
from typing import Iterable


def main(names: Iterable[Iterable[str]]) -> int:
    rates = dict(Counter(names))
    return max(rates.values())


def get_inputs() -> Iterable[Iterable[str]]:
    n = int(input())
    names = []
    for _ in range(n):
        names.append((input().split())[0])
    return names


def print_input(result: int) -> None:
    print(result)


if __name__ == "__main__":
    print_input(main(get_inputs()))
