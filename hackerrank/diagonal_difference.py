n = int(input())

mat = [list(map(int, input().split())) for _ in range(n)]

diagonal_1 = []
diagonal_2 = []

for i in range(n):
    diagonal_1.append(mat[i][i])
    diagonal_2.append(mat[i][n - i - 1])

print(abs(sum(diagonal_1) - sum(diagonal_2)))
