n, k = map(int, input().split(" "))
a = list(map(int, input().split(" ")))
m = sum(a[0:k])
l = [m]
for i in range(0, n - k):
    m = m - a[i] + a[i + k]
    l.append(m)
print(l.index(min(l)) + 1)
