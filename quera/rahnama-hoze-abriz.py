from typing import Iterable


def main(aquariums: Iterable[int], operations: Iterable[int]) -> None:

    max_capacity = sum(aquariums[1 : len(aquariums) - 1])
    if max_capacity == len(operations):
        return len(operations)
    if max_capacity < len(operations):
        return max_capacity + 1
    else:
        return "No Answer"


def get_inputs():
    n, q = map(int, input().split())
    aquariums = list(map(int, input().split()))
    operations = []
    for _ in range(q):
        operations.append(int(input()))
    return (aquariums, operations)


if __name__ == "__main__":
    print(main(*get_inputs()))
