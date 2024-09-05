l = list(map(int, input("Enter elements of list: ").split()))
r = [(x, x**3) for x in l]
print(r)
