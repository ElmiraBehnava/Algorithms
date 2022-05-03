t_0, t_1, n = map(int, input().split())
dp = [t_0, t_1]

for i in range(2, n):
    dp.append(dp[i-2] + (dp[i-1])**2)

print(dp[-1])
