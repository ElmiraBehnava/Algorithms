from collections import defaultdict

k = int(input())
n = list(map(int, input().split(" ")))
d = defaultdict(int)
dp = [0]
for i in n:
    d[i] += 1
for i in range(1, max(n) + 1):
    dp.append(max(dp[i - 1], (i * d[i]) + dp[i - 2]))
print(dp[max(n)])

"""
    dp[i] = max(dp[i-1], (i*d[i]) + dp[i-2])
"""
