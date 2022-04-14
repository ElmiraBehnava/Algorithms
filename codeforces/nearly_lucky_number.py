n = input()
number_of_lucky = n.count("7") + n.count("4")
if number_of_lucky == 4 or number_of_lucky == 7:
    print("YES")
else:
    print("NO")
