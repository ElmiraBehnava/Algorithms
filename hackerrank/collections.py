from collections import Counter

x = int(input())
shoes_list = Counter(list(map(int, input().split())))
y = int(input())
f = []
for _ in range(y):
    f.append(list(map(int, input().split())))

price = 0
for item in f:
    if shoes_list[item[0]] != 0:
        price += item[1]
        shoes_list[item[0]] -= 1
print(price)
