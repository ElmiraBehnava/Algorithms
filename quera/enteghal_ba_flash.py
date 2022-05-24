n, c = map(int, input().split())
files = list(map(int, input().split()))


# def nextfit(files, c):
#     res = 0
#     rem = c
#     for _ in range(len(files)):
#         if sum(files) <= rem:
#             res += 1
#         if rem >= files[_]:
#             rem = rem - files[_]
#         else:
#             res += 1
#             rem = c - files[_]
#     return res


def firstFit(weight, n, c):

    # Initialize result (Count of bins)
    res = 0

    # Create an array to store remaining space in bins
    # there can be at most n bins
    bin_rem = [0] * n

    # Place items one by one
    for i in range(n):

        # Find the first bin that can accommodate
        # weight[i]
        j = 0
        while j < res:
            if bin_rem[j] >= weight[i]:
                bin_rem[j] = bin_rem[j] - weight[i]
                break
            j += 1

        # If no bin could accommodate weight[i]
        if j == res:
            bin_rem[res] = c - weight[i]
            res = res + 1
    return res


res = firstFit(files, n, c)
print(res)
