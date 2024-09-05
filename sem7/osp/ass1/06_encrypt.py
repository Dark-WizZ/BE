mess = input("Enter message: ")
enc = ""
for i in mess:
    if ord(i) in range(ord("A"), ord("Z") + 1):
        enc += chr((ord(i) - ord("A") - 3) % 26 + ord("A"))
    elif ord(i) in range(ord("a"), ord("z") + 1):
        enc += chr((ord(i) - ord("a") - 2) % 26 + ord("a"))
    else:
        enc += i


print("encrypted message :", enc)
