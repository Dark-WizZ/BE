def encrypt(string, shift):
    cipher=''
    for char in string:
        if char == ' ':
            cipher += char
        elif char.isupper():
            cipher += chr((ord(char) + shift - ord('A')) % 26 + ord('A'))
        else:
            cipher += chr((ord(char) + shift - ord('a')) % 26 + ord('a'))
    return cipher

msg = input("Enter message to encrypt: ")
shift = int(input("Shift value: "))
print("Encripted message: ",encrypt(msg,shift))