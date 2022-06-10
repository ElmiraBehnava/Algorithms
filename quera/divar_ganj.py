from typing import Iterable


def main(matrix: Iterable[Iterable[int]]) -> int:
    matrix = list(map(list, matrix))

    def sum_of_adjacent_elements(m: int, matrix: Iterable[Iterable[int]]):
        sum_adjacents_element_matrix = [[0] * m for _ in range(m)]
        for i in range(m):
            for j in range(m):
                if i != 0 and i != m - 1 and j != 0 and j != m - 1:
                    target = matrix[i][j]
                    up = matrix[i - 1][j]
                    down = matrix[i + 1][j]
                    right = matrix[i][j + 1]
                    left = matrix[i][j - 1]
                    sum_adjacents_element_matrix[i][j] = (
                        target + up + down + left + right
                    )
                elif i == 0 and j == 0:
                    sum_adjacents_element_matrix[i][j] = (
                        matrix[i][j] + matrix[i + 1][j] + matrix[i][j + 1]
                    )
                elif i == 0 and j == m - 1:
                    sum_adjacents_element_matrix[i][j] = (
                        matrix[i][j] + matrix[i][j - 1] + matrix[i + 1][j]
                    )
                elif i == m - 1 and j == 0:
                    sum_adjacents_element_matrix[i][j] = (
                        matrix[i][j] + matrix[i][j + 1] + matrix[i - 1][j]
                    )
                elif i == m - 1 and j == m - 1:
                    sum_adjacents_element_matrix[i][j] = (
                        matrix[i][j] + matrix[i - 1][j] + matrix[i][j - 1]
                    )
        return sum_adjacents_element_matrix

    new_matrix = sum_of_adjacent_elements(len(matrix), matrix)
    max_of_rows = []
    for row in new_matrix:
        max_of_rows.append(max(row))
    return max(max_of_rows)


def get_inputs() -> Iterable[Iterable[int]]:
    rows = int(input())
    return [map(int, input().split()) for _ in range(rows)]


if __name__ == "__main__":
    print(main(get_inputs()))
