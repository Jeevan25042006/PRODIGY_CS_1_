def encrypt_caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted_char = chr(((ord(char.lower()) - 97 + shift) % 26) + 97)
            if char.isupper():
                shifted_char = shifted_char.upper()
        else:
            shifted_char = char
        encrypted_text += shifted_char
    return encrypted_text


def decrypt_caesar_cipher(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            shifted_char = chr(((ord(char.lower()) - 97 - shift) % 26) + 97)
            if char.isupper():
                shifted_char = shifted_char.upper()
        else:
            shifted_char = char
        decrypted_text += shifted_char
    return decrypted_text


if __name__ == "__main__":
    print("Caesar Cipher Encryption and Decryption")

    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))

    encrypted_message = encrypt_caesar_cipher(message, shift)
    print(f"Encrypted message: {encrypted_message}")

    decrypted_message = decrypt_caesar_cipher(encrypted_message, shift)
    print(f"Decrypted message: {decrypted_message}")


