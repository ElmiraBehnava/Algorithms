n, v = map(int, input().split())
cost = 0
if v >= n:
    cost = n - 1
else:
    cost = v + (n - v - 1) * (n - v + 2) / 2
print(int(cost))
