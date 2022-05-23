n = int(input())
grid = []
for i in range(n):
    grid.append(list(map(int, list(input()))))

indexes = []
for i in range(n):
    for j in range(n):
        if i != 0 and i != n - 1 and j != 0 and j != n - 1:
            m = i
            k = j
            target = grid[i][j]
            up = grid[i - 1][j]
            down = grid[i + 1][j]
            right = grid[i][j + 1]
            left = grid[i][j - 1]
            if (
                target > up
                and target > down
                and target > right
                and target > left
            ):
                indexes.append((m, k))

for index in indexes:
    grid[index[0]][index[1]] = "X"

to_show = ["".join(list(map(str, list(item)))) for item in grid]

for _ in to_show:
    print(_)
