n = int(input("Enter n: "))

for i in range(1, n + 1):
    s = i
    for j in range(1, i + 1):
        print(s, end=" ")
        s *= s
    print()
