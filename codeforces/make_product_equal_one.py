k = int(input())
a = list(map(int, input().split()))
dp_plus = [abs(a[0] - 1)]
dp_m = [abs(a[0] + 1)]
for i in range(1, len(a)):
    dp_plus.append(
        min(dp_plus[i - 1] + abs(a[i] - 1), dp_m[i - 1] + abs(a[i] + 1))
    )
    dp_m.append(
        min(dp_m[i - 1] + abs(a[i] - 1), dp_plus[i - 1] + abs(a[i] + 1))
    )
print(dp_plus[-1])

"""
    dp_plus[i] = min(dp_plus[i - 1] + abs(a[i] - 1), dp_m[i - 1] + abs(a[i] + 1))
    dp_minus[i] = min(dp_minus[i - 1] + abs(a[i] + 1), dp_plus[i - 1] + abs(a[i] - 1))
    
"""
