import os
from collections import Counter


def lonelyinteger(a):
    counted = Counter(a).items()
    for item in counted:
        if item[1] == 1:
            return item[0]


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + "\n")

    fptr.close()
