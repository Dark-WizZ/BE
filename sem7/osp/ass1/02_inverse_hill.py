h = int(input("Enter height: "))
s = 0
c = 2 * h - 1
for i in range(h):
    print(" " * s, "*" * c)
    c -= 2
    s += 1
