input()
list_of = sorted(map(int, input().split()))
s = c = 0
while s <= sum(list_of):
    s += list_of.pop()
    c += 1
print(c)
