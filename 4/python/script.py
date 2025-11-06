ukr_alphabet = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ -"
message = "ШИФР – ОСНОВА ЗАХИСТУ"
key = "КЛЮЧ"

def vigenere_encrypt(text, key, alphabet):
    res = ""
    key = key.upper()
    key_index = 0
    for char in text:
        if char not in alphabet:
            res += char
            continue
        text_idx = alphabet.index(char)
        key_idx = alphabet.index(key[key_index % len(key)])
        res += alphabet[(text_idx + key_idx) % len(alphabet)]
        key_index += 1
    return res

def vigenere_decrypt(cipher, key, alphabet):
    res = ""
    key = key.upper()
    key_index = 0
    for char in cipher:
        if char not in alphabet:
            res += char
            continue
        cipher_idx = alphabet.index(char)
        key_idx = alphabet.index(key[key_index % len(key)])
        res += alphabet[(cipher_idx - key_idx) % len(alphabet)]
        key_index += 1
    return res

# Шифрування
encrypted = vigenere_encrypt(message, key, ukr_alphabet)
# Розшифрування
decrypted = vigenere_decrypt(encrypted, key, ukr_alphabet)

# Збереження у файли
with open("original.txt", "w", encoding="utf-8") as f:
    f.write(message)

with open("key.txt", "w", encoding="utf-8") as f:
    f.write(key)

with open("encrypted.txt", "w", encoding="utf-8") as f:
    f.write(encrypted)

with open("decrypted.txt", "w", encoding="utf-8") as f:
    f.write(decrypted)

print("Повідомлення:", message)
print("Ключ:", key)
print("Зашифроване:", encrypted)
print("Розшифроване:", decrypted)