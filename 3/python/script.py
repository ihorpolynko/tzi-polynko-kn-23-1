import random

KEY_LENGTH = 17
key = [random.randint(0, 255) for _ in range(KEY_LENGTH)]
print("Згенерований ключ (17 елементів):", key)

plaintext = input("Введи текст для шифрування: ")

plain_bytes = plaintext.encode("utf-8")

cipher_bytes = bytearray()
for i, byte in enumerate(plain_bytes):
    cipher_byte = byte ^ key[i % KEY_LENGTH]
    cipher_bytes.append(cipher_byte)

cipher_hex = cipher_bytes.hex()
print("\nШифртекст (у hex):", cipher_hex)