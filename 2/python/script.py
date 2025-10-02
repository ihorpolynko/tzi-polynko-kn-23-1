ALPHABET = "АБВГДЕҐІЇЖЗИКЛМНОПРСТУФХЦЧШЩЬЄЮЯ "
M = len(ALPHABET)


def encrypt_gronsfeld(plain_text, key):
    cipher_text = ""
    key_digits = [int(k) for k in key]

    for i, char in enumerate(plain_text):
        if char not in ALPHABET:
            cipher_text += char
            continue
        P = ALPHABET.index(char)
        K = key_digits[i % len(key_digits)]
        C = (P + K) % M
        cipher_text += ALPHABET[C]
    return cipher_text


def main():
    plain_text = input("Введіть текст для шифрування (тільки українські літери та пробіли): ").upper()

    for c in plain_text:
        if c not in ALPHABET:
            print(f"Помилка: недопустимий символ '{c}' у тексті!")
            return

    key = input("Введіть числовий ключ: ")
    if not key.isdigit():
        print("Помилка: ключ повинен складатися лише з цифр!")
        return

    cipher_text = encrypt_gronsfeld(plain_text, key)
    print("\nЗашифрований текст:")
    print(cipher_text)


if __name__ == "__main__":
    main()