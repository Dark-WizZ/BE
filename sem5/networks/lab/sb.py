def encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            if char.islower():
                encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        elif char.isdigit():
            encrypted_char = str((int(char) + shift) % 10)
        else:
            encrypted_char = char  # Leave other characters unchanged
        encrypted_message += encrypted_char
    return encrypted_message

def decrypt(encrypted_message, shift):
    decrypted_message = ""
    for char in encrypted_message:
        if char.isalpha():
            if char.islower():
                decrypted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            else:
                decrypted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
        elif char.isdigit():
            decrypted_char = str((int(char) - shift) % 10)
        else:
            decrypted_char = char  # Leave other characters unchanged
        decrypted_message += decrypted_char
    return decrypted_message

# Example usage:
message = "Khoor456"
shift = 3
encrypted = encrypt(message, shift)
print("Encrypted:", encrypted)

decrypted = decrypt(message, shift)
print("Decrypted:", decrypted)
