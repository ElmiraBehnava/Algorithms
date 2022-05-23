s = input()
a, b = s.find("AB"), s.rfind("AB")
c, d = s.find("BA"), s.rfind("BA")
print("YES" if a != -1 and c != -1 and (abs(a - d) > 1 or abs(b - c) > 1) else "NO")
