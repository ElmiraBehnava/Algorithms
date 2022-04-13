n = int(input())
m = list(map(int, input().split(" ")))
a = "NO"
for i in range(n):
    if m[m[m[m[i] - 1] - 1] - 1] == m[i]:
        a = "YES"
print(a)
