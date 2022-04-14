n = list(map(int, input()))
m = list(map(int, input()))
a = []
for i in range(len(m)):
    b = n[i] + m[i]
    if b == 2:
        a.append(str(0))
    else:
        a.append(str(b))

print("".join(a))
