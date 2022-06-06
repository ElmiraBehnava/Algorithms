import os


def countingSort(arr):
    a = [0] * (max(arr) + 1)
    for digit in arr:
        a[digit] += 1

    return a


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(" ".join(map(str, result)))
    fptr.write("\n")

    fptr.close()
