sentence = input("Enter sentence: ")
s = sentence.lower()
print("The given sentence is", end=" ")
for i in range(ord("a"), ord("z")):
    if chr(i) not in s:
        print("not", end=" ")
        break
print("panagram")
