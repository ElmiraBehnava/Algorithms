from typing import Iterable


def main(matrix: Iterable[Iterable[int]]) -> int:
    matrix = list(map(list, matrix))
    result = 0
    for reference_index in range(len(matrix)):
        number_on_main_diagonal = matrix[reference_index][reference_index]
        if number_on_main_diagonal % 3 == 1:
            result += number_on_main_diagonal

        number_on_anti_diagonal = matrix[reference_index][
            len(matrix) - reference_index - 1
        ]
        if number_on_anti_diagonal % 3 == 1:
            result += number_on_anti_diagonal

    return result


def get_inputs() -> Iterable[Iterable[int]]:
    rows = int(input())
    return [map(int, input().split()) for _ in range(rows)]


def print_result(number: int) -> None:
    print(number)


def test() -> None:
    assert main([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 8


if __name__ == "__main__":
    print_result(main(get_inputs()))
