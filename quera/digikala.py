m, n, max_pack, max_weight = map(int, input().split(" "))
packs = []
for i in range(n):
    packs.append(list(map(int, input().split(" "))))

a = [0]
for i in range(0, n):
    a.append(packs[i][1] + a[i])

b = []
for i in range(n - 1):
    b.append(1 if packs[i + 1][0] != packs[i][0] else 0)

sum_b = [0]
for i in range(len(b)):
    sum_b.append(b[i] + sum_b[i])


def cost(i, j):
    if j - i > max_pack:
        return -1
    if a[j] - a[i] > max_weight:
        return -1
    return (sum_b[j - 1] - sum_b[i]) + 2


dp = [0]
for i in range(1, n + 1):
    dp.append(
        min([dp[j] + cost(j, i) for j in range(0, i) if cost(j, i) != -1])
    )
print(dp[-1])
