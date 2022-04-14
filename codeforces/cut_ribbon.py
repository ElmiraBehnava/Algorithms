n, a, b, c = map(int, input().split(" "))
m = [0]
for i in range(1, n + 1):
    x = -1
    if i - a >= 0:
        x = max(x, m[i - a])
    if i - b >= 0:
        x = max(x, m[i - b])
    if i - c >= 0:
        x = max(x, m[i - c])
    if x == -1:
        m.append(-1)
    else:
        m.append(x + 1)

print(m[n])
