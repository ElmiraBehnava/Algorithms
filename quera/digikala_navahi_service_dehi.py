n = int(input())
shops_areas = []
for _ in range(n):
    a, b = map(int, input().split(" "))
    shops_areas.append(list(range(a, b + 1)))

s = int(input())
f = int(input())

flag_s, flag_f = 0, 0
for item in shops_areas:
    if s in item:
        flag_s = 1
        break

for item in shops_areas:
    if f in item:
        flag_f = 1
        break
b = []
for i in range(s, f + 1):
    for item in shops_areas:
        if i in item:
            b.append(1)
        else:
            pass

if flag_f * flag_s == 1 and 0 not in b:
    print("true")
else:
    print("false")
