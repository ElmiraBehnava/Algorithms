a = input().strip()
dp = [0, 0]
for i in range(1, len(a)):
    if a[i] == a[i - 1]:
        dp.append(dp[i] + 1)
    else:
        dp.append(dp[i])
n = int(input())
for _ in range(n):
    i, j = map(int, input().split())
    print(dp[j] - dp[i])

"""
    dp[i] = dp[i - 1] + 1 if a[i] == a[i - 1] else dp[i]
"""
