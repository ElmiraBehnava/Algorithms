t = int(input())


def find_max_subarray(a, size):
    max_so_far = a[0]
    current_max = a[0]
    for i in range(1, size):
        current_max = max(a[i], current_max + a[i])
        max_so_far = max(max_so_far, current_max)
    return max_so_far


def find_max_subseq(a, size):
    c = 0
    b = []
    for i in range(size):
        if a[i] > 0:
            c += a[i]
        if a[i] < 0:
            b.append(a[i])
    if c == 0:
        return max(a)
    return c


for i in range(t):
    array_size = int(input())
    array = list(map(int, input().split()))
    print(
        str(find_max_subarray(array, array_size))
        + " "
        + str(find_max_subseq(array, array_size))
    )
