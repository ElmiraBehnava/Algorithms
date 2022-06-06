k, n, w = map(int, input().split())


costs = []
for i in range(1, w + 1):
    costs.append(k * i)

if sum(costs) < n:
    print(0)
else:
    print(sum(costs) - n)
