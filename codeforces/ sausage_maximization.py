class Node:
    def __init__(self):
        self.children = {}

    def insert(self, num, index, size):
        if index == size:
            return

        if num[index] not in self.children:
            self.children[num[index]] = Node()
        self.children[num[index]].insert(num, index + 1, size)

    def find_max(self, num, index, size, result=0):
        if index == size:
            return result

        if 1 - num[index] in self.children:
            return self.children[1 - num[index]].find_max(
                num, index + 1, size, result * 2 + 1
            )
        else:
            return self.children[num[index]].find_max(
                num, index + 1, size, result * 2 + 0
            )


tree = Node()
n = int(input())
a = list(map(int, input().split()))
prefix_xor = [0]
for item in a:
    prefix_xor.append(prefix_xor[-1] ^ item)

suffix_xor = [0]
for item in reversed(a):
    suffix_xor.append(suffix_xor[-1] ^ item)

result = 0
for suf, pre in zip(reversed(suffix_xor), prefix_xor):
    tmp = []
    for _ in range(40):
        tmp.append(pre % 2)
        pre //= 2

    tree.insert(tmp[::-1], 0, 40)
    tmp = []
    for _ in range(40):
        tmp.append(suf % 2)
        suf //= 2
    result = max(tree.find_max(tmp[::-1], 0, 40), result)

print(result)
