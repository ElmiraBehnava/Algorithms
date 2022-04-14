s = input()
sub_string = "QAQ"


def count_subs(s, sub_string, n, m):
    if (n == 0 and m == 0) or m == 0:
        return 1
    if n == 0:
        return 0
    if s[n - 1] == sub_string[m - 1]:
        return count_subs(s, sub_string, n - 1, m - 1) + count_subs(
            s, sub_string, n - 1, m
        )
    else:
        return count_subs(s, sub_string, n - 1, m)


print(count_subs(s, sub_string, len(s), len(sub_string)))
