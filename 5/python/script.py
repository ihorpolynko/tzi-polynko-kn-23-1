import random

# Параметри мультиплікативного датчика
a = 7
m = 256
x0 = 5

def multiplicative_generator(length, a, m, x0):
    gamma = []
    x = x0
    for _ in range(length):
        x = (a * x) % m
        gamma.append(x)
    return gamma

def encrypt_bytes(data, gamma):
    encrypted = bytearray()
    for i, byte in enumerate(data):
        encrypted.append((byte * gamma[i % len(gamma)]) % m)
    return bytes(encrypted)

with open("Source.txt", "r", encoding="utf-8") as f:
    source_text = f.read()

source_bytes = source_text.encode("utf-8")
gamma = multiplicative_generator(len(source_bytes), a, m, x0)

encrypted_bytes = encrypt_bytes(source_bytes, gamma)
with open("Coded.txt", "wb") as f:
    f.write(encrypted_bytes)

print("Шифрування завершено.")