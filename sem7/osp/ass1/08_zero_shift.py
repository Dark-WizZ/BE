l = list(map(int, input("Enter values to the list: ").split()))

for i in l:
    if not i:
        l.remove(i)
        l.append(i)

print(l)
