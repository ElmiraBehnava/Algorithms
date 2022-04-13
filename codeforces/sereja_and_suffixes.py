n, m = map(int, input().split(" "))
a = list(map(int, input().split(" ")))
s = set()
dp = [0]

for i, item in zip(range(len(a)), a[::-1]):
    if item in s:
        dp.append(dp[i])
    else:
        dp.append(dp[i] + 1)
    s.add(item)

for i in range(m):
    k = int(input())
    print(dp[n + 1 - k])

"""
    dp[i] = dp[i - 1] + 1 if a[i] not in s else dp[i - 1]
"""
