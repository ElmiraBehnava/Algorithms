from typing import Iterable


def is_prime(n: int) -> bool:
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 6
    return True


def main(string: str) -> Iterable[int]:
    result = []
    index = 0

    while index < len(string) - 1:
        number_string = string[index : index + 2]
        try:
            number = int(number_string)
            if is_prime(number) and (10 < number < 100):
                result.append(number)
            index += 1
        except ValueError:
            index += 1

    return result


def get_inputs() -> str:
    return input()


def print_result(numbers: Iterable[int]) -> None:
    for number in numbers:
        print(number)


def test() -> None:
    assert main("929625948") == [29, 59]


if __name__ == "__main__":
    print_result(main(get_inputs()))
