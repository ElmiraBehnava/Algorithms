l1 = set(list(map(int, input().split())))
l2 = set(list(map(int, input().split())))

common_elements = l1.intersection(l2)
print(len(common_elements))
print(" ".join(map(str, sorted(common_elements))))
