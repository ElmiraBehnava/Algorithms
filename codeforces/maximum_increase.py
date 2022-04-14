n = int(input())
a = list(map(int, input().split(" ")))
c = 1
ans = 1
for i in range(n - 1):
    if a[i] < a[i + 1]:
        c += 1
        ans = max(ans, c)
    else:

        c = 1
print(max(ans, c))
