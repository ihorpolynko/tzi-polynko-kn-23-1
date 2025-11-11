from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import os

# Функція шифрування у режимі OFB
def des_encrypt_ofb(key, plaintext):
    iv = os.urandom(8)

    cipher = DES.new(key, DES.MODE_OFB, iv)

    padded_text = pad(plaintext.encode('utf-8'), 8)

    ciphertext = cipher.encrypt(padded_text)

    return iv, ciphertext


# Функція дешифрування у режимі OFB
def des_decrypt_ofb(key, iv, ciphertext):
    cipher = DES.new(key, DES.MODE_OFB, iv)

    decrypted_padded = cipher.decrypt(ciphertext)

    decrypted = unpad(decrypted_padded, 8)

    return decrypted.decode('utf-8')


key = b'12345678'

plaintext = "Це тестовий текст для шифрування DES OFB"

print("Вихідний текст:", plaintext)

# Шифрування
iv, ciphertext = des_encrypt_ofb(key, plaintext)
print("IV:", iv.hex())
print("Шифротекст:", ciphertext.hex())

# Дешифрування
decrypted_text = des_decrypt_ofb(key, iv, ciphertext)
print("Розшифрований текст:", decrypted_text)