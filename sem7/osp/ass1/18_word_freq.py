s = input("Enter a sentence: ")
d = {}
for w in s.split():
    if not w in d.keys():
        d[w] = 0
    d[w] += 1
print(d)
