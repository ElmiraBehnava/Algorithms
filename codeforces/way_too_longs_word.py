b = int(input())
n = []
for _ in range(b):
    string = input()
    if len(string) <= 10:
        n.append(string)
    else:
        n.append(string[0] + str(len(string) - 2) + string[-1])
print(*n, sep="\n")
