from Crypto.Cipher import DES
import os

def bytes_to_bits(b: bytes) -> list:
    bits = []
    for byte in b:
        bits.extend([ (byte >> i) & 1 for i in range(7, -1, -1) ])
    return bits

def bits_to_bytes(bits: list) -> bytes:
    if len(bits) % 8 != 0:
        bits = bits + [0] * (8 - (len(bits) % 8))
    out = bytearray()
    for i in range(0, len(bits), 8):
        byte = 0
        for bit in bits[i:i+8]:
            byte = (byte << 1) | bit
        out.append(byte)
    return bytes(out)

def string_to_bits(s: str) -> list:
    return bytes_to_bits(s.encode('utf-8'))

def bits_to_string(bits: list) -> str:
    b = bits_to_bytes(bits)
    return b.decode('utf-8', errors='replace')

def xor_bits(a: list, b: list) -> list:
    n = min(len(a), len(b))
    return [ (a[i] ^ b[i]) for i in range(n) ]

def simple_des_block_encrypt(block_bits: list, key: bytes) -> list:
    block_bytes = bits_to_bytes(block_bits[:64])
    cipher = DES.new(key, DES.MODE_ECB)
    encrypted_bytes = cipher.encrypt(block_bytes)
    return bytes_to_bits(encrypted_bytes)

def des_ofb_encrypt(plaintext: str, key: bytes, iv: bytes) -> (bytes, bytes):
    pt_bits = string_to_bits(plaintext)
    B = 64
    prev = bytes_to_bits(iv)
    cipher_bits = []

    for i in range(0, len(pt_bits), B):
        block = pt_bits[i:i+B]
        keystream = simple_des_block_encrypt(prev, key)
        ks_slice = keystream[:len(block)]
        cipher_block = xor_bits(block, ks_slice)
        cipher_bits.extend(cipher_block)
        prev = keystream

    cipher_bytes = bits_to_bytes(cipher_bits)
    return iv, cipher_bytes

def des_ofb_decrypt(cipher_bytes: bytes, key: bytes, iv: bytes) -> str:
    cipher_bits = bytes_to_bits(cipher_bytes)
    B = 64
    prev = bytes_to_bits(iv)
    plain_bits = []

    for i in range(0, len(cipher_bits), B):
        block = cipher_bits[i:i+B]
        keystream = simple_des_block_encrypt(prev, key)
        ks_slice = keystream[:len(block)]
        plain_block = xor_bits(block, ks_slice)
        plain_bits.extend(plain_block)
        prev = keystream

    return bits_to_string(plain_bits)

if __name__ == "__main__":
    key = b'12345678'
    iv = os.urandom(8)

    plaintext = "Це тестовий текст для шифрування DES OFB"

    print("Вихідний текст:", plaintext)
    iv_out, ciphertext = des_ofb_encrypt(plaintext, key, iv)
    print("IV (hex):", iv_out.hex())
    print("Шифротекст (hex):", ciphertext.hex())

    recovered = des_ofb_decrypt(ciphertext, key, iv_out)
    print("Розшифрований текст:", recovered)