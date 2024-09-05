j = input("enter: ")

vowels = "aeiouAEIOU"
n = ""
i = 0
while i < len(j):
    if i + 2 < len(j) and j[i] in vowels and j[i + 1] in vowels and j[i + 2] in vowels:
        n += "*"
        i += 3
    else:
        n += j[i]
        i += 1

print(n)
