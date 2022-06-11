n, m = map(int, input().split(" "))
mat = [list(map(int, input().split())) for _ in range(n)]
row_dp = [
    [0 if i != 0 and i != 1 and n != 1 else 1 for i in range(m)]
    for _ in range(n)
]

col_dp = [
    [1 if _ == 0 or _ == 1 or m == 1 else 0 for i in range(m)]
    for _ in range(n)
]

c = [[0 for i in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if row_dp[i][j] != 1 and j > 2:
            if (mat[i][j - 1]) ** 2 == mat[i][j] * mat[i][j - 2]:
                row_dp[i][j] = 1
            else:
                continue
        if col_dp[i][j] != 1 and i > 2:
            if (mat[i - 1][j]) ** 2 == mat[i][j] * mat[i - 2][j]:
                col_dp[i][j] = 1
            else:
                continue
        if row_dp[i][j] == 1 and col_dp[i][j] == 1:
            c[i][j] = 1


def resetMatrix(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] != 0:
                mat[i][j] = 1


# columns is allowed
def findMaxRectArea(mat):

    # base case
    if not mat or not len(mat):
        return 0

    # `M × N` matrix
    M = len(mat)
    N = len(mat[0])

    for j in range(N):
        # process each column from bottom to top
        for i in reversed(range(0, M - 1)):
            if mat[i][j] == 1:
                mat[i][j] = mat[i + 1][j] + 1

    # keep track of the largest rectangle of 1's found so far
    maxArea = 0

    # traverse each row in the modified matrix to find the maximum area
    for i in range(M):

        # create a count array for each row `i`
        count = [0] * (M + 1)

        # process row `i`
        for j in range(N):

            if mat[i][j] > 0:

                # increment value in the count array using the current element
                # as an index
                count[mat[i][j]] += 1

                # the area can be calculated by multiplying the current
                # element `mat[i][j]` with the corresponding value in the
                # count array `count[mat[i][j]]`

                maxArea = max(maxArea, mat[i][j] * count[mat[i][j]])

    # reset matrix before returning
    resetMatrix(mat)

    return maxArea


print(findMaxRectArea(c))
