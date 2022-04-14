t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split(" ")))
    dp = [0 for x in range(n + 1)]
    dp[0] = set([0])
    for i in range(1, n + 1):
        dp[i] = dp[i - 1].union({item + a[i - 1] for item in dp[i - 1]})
    sum_of = sum(a)
    if sum_of % 2 == 0 and sum_of / 2 in dp[n]:
        print("YES")
    else:
        print("NO")
