from collections import Counter
from typing import Iterable


def main(numbers: Iterable[int]) -> str:
    count_of_each_element = Counter(numbers)

    if any(count >= 2 for count in count_of_each_element.values()):
        return "true"
    else:
        return "false"


def get_inputs() -> Iterable[int]:
    return list(map(int, input().strip().split()))


def print_result(result: str) -> None:
    print(result)


def test() -> None:
    assert main("1 2 3 1") == "true"


if __name__ == "__main__":
    test()
    print_result(main(get_inputs()))
