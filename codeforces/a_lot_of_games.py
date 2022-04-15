class Node:
    def __init__(self):
        self.children = {}

    def insert(self, string):
        if string == "":
            return

        if string[0] not in self.children:
            self.children[string[0]] = Node()
        self.children[string[0]].insert(string[1:])


def dfs(node, depth=0):
    for child in node.children.values():
        dfs(child, depth + 1)

    if len(node.children):
        if depth % 2 == 1:
            node.f_can_lose = all(
                [child.f_can_lose for child in node.children.values()]
            )
            node.f_can_win = all(
                [child.f_can_win for child in node.children.values()]
            )
        else:
            node.f_can_lose = any(
                [child.f_can_lose for child in node.children.values()]
            )
            node.f_can_win = any(
                [child.f_can_win for child in node.children.values()]
            )
    else:
        if depth % 2 == 1:
            node.f_can_lose = False
            node.f_can_win = True
        else:
            node.f_can_lose = True
            node.f_can_win = False


tree = Node()

n, k = map(int, input().split())
for _ in range(n):
    tree.insert(input().strip())

dfs(tree)

if not tree.f_can_win:
    print("Second")
else:
    if tree.f_can_lose:
        print("First")
    elif k % 2 == 0:
        print("Second")
    else:
        print("First")
