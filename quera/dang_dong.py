t = int(input())
l = []
for _ in range(t):
    n, s, a = map(int, input().split())
    formula = (((n - 1) * a) + s) / n
    if a >= s:
        l.append(-1)
    elif str(formula)[-1] == "0":
        l.append(int(formula - a))
    else:
        l.append(-1)
for i in range(len(l)):
    print(l[i])
