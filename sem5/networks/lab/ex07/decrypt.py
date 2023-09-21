def decrypt(string, shift):
    cipher=''
    for char in string:
        if char == ' ':
            cipher += char
        elif char.isupper():
            cipher += chr((ord(char) - shift - ord('A')) % 26 + ord('A'))
        elif char.isdigit():
            print("char -> ",char)
            print(str((int(char) - shift) % 10))
            cipher += str((int(char) - shift) % 10)
        else:
            cipher += chr((ord(char) - shift - ord('a')) % 26 + ord('a'))
    return cipher

msg = input("Enter message to decrypt: ")
shift = int(input("Shift value: "))
print("Decrypted message: ",decrypt(msg,shift))