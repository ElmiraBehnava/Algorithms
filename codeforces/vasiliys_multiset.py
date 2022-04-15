class Node:
    def __init__(self):
        self.children = {}
        self.count = 0

    def insert(self, num):
        if len(num) == 0:
            self.count += 1
            return

        if num[0] not in self.children:
            self.children[num[0]] = Node()
        self.children[num[0]].insert(num[1:])

    def delete(self, num):
        if len(num) == 0:
            self.count -= 1
            return self.count == 0

        if self.children[num[0]].delete(num[1:]):
            self.children.pop(num[0])
            return len(self.children) == 0

    def find_max(self, num, result=0):
        if len(num) == 0:
            return result

        if 1 - num[0] in self.children:
            return self.children[1 - num[0]].find_max(num[1:], result * 2 + 1)
        else:
            return self.children[num[0]].find_max(num[1:], result * 2 + 0)


tree = Node()
q = int(input().strip())
for _ in range(q):
    op, num = input().split()
    num = int(num)
    a = []
    for _ in range(30):
        a.append(num % 2)
        num //= 2
    if op == "+":
        tree.insert(a[::-1])
    if op == "-":
        tree.delete(a[::-1])
    if op == "?":
        print(tree.find_max(a[::-1]))
