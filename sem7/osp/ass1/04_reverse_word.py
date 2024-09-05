s = input("Give a sentence: ").split()
res = list(map(lambda x: x[::-1], s))
print(" ".join(res))
