[n, k] = list(map(int, input("Enter n and k: ").split()))
l = [1 if x % 2 == 0 else 0 for x in range(n)]

if k % 2:
    l.append(l.pop(0))
print(l)
