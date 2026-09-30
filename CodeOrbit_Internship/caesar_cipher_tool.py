"""
Caesar Cipher Encryption Tool
------------------------------
Encrypts and decrypts text using the classic Caesar Cipher technique,
where each letter is shifted by a fixed number of positions (the key).

Author: <Avisha Masih>
Internship: CodeOrbit Tech - Cyber Security Internship
"""

import string


def caesar_shift(text: str, shift: int, mode: str = "encrypt") -> str:
    """
    Shift each letter in `text` by `shift` positions.
    mode = 'encrypt' shifts forward, 'decrypt' shifts backward.
    Non-alphabet characters (numbers, spaces, punctuation) are left unchanged.
    """
    if mode == "decrypt":
        shift = -shift

    result = []
    for char in text:
        if char in string.ascii_uppercase:
            new_index = (ord(char) - ord('A') + shift) % 26
            result.append(chr(new_index + ord('A')))
        elif char in string.ascii_lowercase:
            new_index = (ord(char) - ord('a') + shift) % 26
            result.append(chr(new_index + ord('a')))
        else:
            result.append(char)  # leave digits, spaces, symbols as-is

    return "".join(result)


def main():
    print("=== Caesar Cipher Encryption Tool ===\n")

    message = input("Enter your message: ")

    while True:
        try:
            key = int(input("Enter shift key (e.g., 3): "))
            break
        except ValueError:
            print("Please enter a whole number for the key.")

    encrypted = caesar_shift(message, key, mode="encrypt")
    decrypted = caesar_shift(encrypted, key, mode="decrypt")

    print("\n--- Result ---")
    print(f"Original message : {message}")
    print(f"Shift key        : {key}")
    print(f"Encrypted output : {encrypted}")
    print(f"Decrypted output : {decrypted}  (should match original)")
    print("--------------\n")


if __name__ == "__main__":
    main()