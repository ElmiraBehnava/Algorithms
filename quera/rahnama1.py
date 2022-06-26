from typing import Iterable, Tuple


def find_all_divisors(num: int) -> Iterable[int]:
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def main(n: int) -> Tuple[int, int]:
    all_divisors = []
    number_of_divisors, sum_of_divisors = 0, 0
    for i in range(1, n + 1):
        all_divisors.append(find_all_divisors(i))

    for item in all_divisors:
        number_of_divisors += len(item)
        sum_of_divisors += sum(item)

    return number_of_divisors, sum_of_divisors


def get_inputs() -> int:
    return int(input())


def print_input(result: Tuple[int, int]) -> None:
    print(result[0], result[1])


if __name__ == "__main__":
    print_input(main(get_inputs()))
