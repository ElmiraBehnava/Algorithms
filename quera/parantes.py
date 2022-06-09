open_list = ["[", "{", "("]
close_list = ["]", "}", ")"]

stack = []


def find_valid(string):
    for i in string:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if (len(stack) > 0) and open_list[pos] == stack[len(stack) - 1]:
                stack.pop()
            else:
                return "Invalid"
    if len(stack) == 0:
        return "Valid"
    else:
        return "Invalid"
