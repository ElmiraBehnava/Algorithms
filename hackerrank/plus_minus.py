n = int(input())
l = list(map(int, input().split()))
positives = [item for item in l if item > 0]
zeros = [item for item in l if item == 0]
negetives = [item for item in l if item < 0]


print("{:.6f}".format(len(positives) / n))
print("{:.6f}".format(len(negetives) / n))
print("{:.6f}".format(len(zeros) / n))
