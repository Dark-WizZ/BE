s1 = list(input("Enter first string: "))
s2 = list(input("Enter second string: "))

s1.sort()
s2.sort()

if s1 == s2:
    print("It's an anagram")
else:
    print("It's not an anagram")
