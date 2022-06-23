from typing import Tuple


def main(s: str, t: str) -> bool:
    if set(s) == set(t):
        return True
    else:
        return False


def get_inputs() -> Tuple[str]:
    s = input()
    t = input()
    return s, t


def print_result():
    pass


def test() -> None:
    pass


if __name__ == "__main__":
    print(main(*get_inputs()))
