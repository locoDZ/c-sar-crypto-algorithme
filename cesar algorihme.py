import random

def cesar_encrypt(text, shift):
    encrypted = ""

    for c in text:
        if c.isalpha():

            ascii_offset = 65 if c.isupper() else 97
            encrypted_char = chr((ord(c)- ascii_offset + shift) % 26 +ascii_offset)
            encrypted += encrypted_char
        else:
            encrypted += c

    return encrypted

def cesar_decrypt(text, shift) :
    decrypted = ""
    for c in text:
        if c.isalpha():
            ascii_offset = 65 if c.isupper() else 97
            decrypted_char = chr((ord(c)- ascii_offset - shift) % 26 +ascii_offset)
            decrypted += decrypted_char
        else:
            decrypted += c

    return decrypted

def main():
    while True:
        print("\n=== Caesar Cipher Menu ===")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Encrypt and Decrypt with random shift")
        print("4. Exit")

        choice = input("\nEnter your choice (1-4): ")

        if choice == '1':
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value (1-25): "))
            encrypted = cesar_encrypt(message, shift)
            print(f"\nEncrypted message: {encrypted}")

        elif choice == '2':
            message = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value (1-25): "))
            decrypted = cesar_decrypt(message, shift)
            print(f"\nDecrypted message: {decrypted}")

        elif choice == '3':
            message = input("Enter the message to encrypt: ")
            shift = random.randint(1, 25)
            encrypted = cesar_encrypt(message, shift)
            decrypted = cesar_decrypt(encrypted, shift)
            print(f"\nEncrypted message: {encrypted}")
            print(f"Decrypted message: {decrypted}")
            print(f"Random shift used: {shift} (keep this to decrypt later)")

        elif choice == '4':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()