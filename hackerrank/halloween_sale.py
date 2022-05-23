p, d, m, s = map(int, input().strip().split())


def how_many_games(p, d, m, s):
    res = 0

    while s > 0:
        res += 1
        s -= p
        p = max(p - d, m)

    if s != 0:
        res -= 1

    return res


print(how_many_games(p, d, m, s))
