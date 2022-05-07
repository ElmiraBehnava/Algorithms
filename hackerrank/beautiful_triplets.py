n, d = map(int, input().split())
arr = list(map(int, input().split()))
c = 0
for item in arr:
    n = item + d
    if n in arr and n + d in arr:
        c += 1
print(c)
