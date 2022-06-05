s, f, l, x = map(int, input().split())

if x < s:
    print("exam did not started!")
elif x >= f:
    print("exam finished!")
else:
    if l < x:
        remaining_time = f - x
        print(remaining_time)
    else:
        print("exam finished!")
