a = input()
c = [
    a,
]


def shiftall(s, n):
    n %= len(s)
    return s[n:] + s[:n]


for i in range(1, len(a)):
    n = shiftall(a, i)
    if n < min(c):
        c.append(n)
    c = [min(c)]

print(min(c))
