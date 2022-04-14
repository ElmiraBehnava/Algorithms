t = int(input())
dp = [[0 for x in range(100)] for x in range(100)]
dp[0][0] = set([0])
for i in range(100):
    for j in range(100):
        if i == 0 and j != 0:
            dp[0][j] = {item + i + 1 for item in dp[i][j - 1]}
        if j == 0 and i != 0:
            dp[i][0] = {item + j + 1 for item in dp[i - 1][j]}
        if i != 0 and j != 0:
            dp[i][j] = {item + j + 1 for item in dp[i - 1][j]}.union(
                {item + i + 1 for item in dp[i][j - 1]}
            )
for i in range(t):
    n, m, k = list(map(int, input().split(" ")))
    if k in dp[n - 1][m - 1]:
        print("YES")
    else:
        print("NO")
