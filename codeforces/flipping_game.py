n = int(input())
a = list(map(int, input().split(" ")))
c = [0]

for i in range(n):
    if a[i] == 0:
        c.append(c[i] + 1)
    else:
        c.append(max(0, c[i] - 1))

if sum(a) == n:
    print(n - 1)
else:
    print(max(c) + sum(a))
