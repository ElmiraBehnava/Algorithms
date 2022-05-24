numbers = list(map(int, input().split()))
numbers.sort()
print(sum(numbers[:4]), sum(numbers[-4:]), sep=" ")
