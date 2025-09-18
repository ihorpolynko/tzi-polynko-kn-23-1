# функція шифрування
def encrypt(text, key):
    # Довжина блоку (4 символи)
    block_size = len(key)
    # Доповнення пробілами, якщо не ділиться
    while len(text) % block_size != 0:
        text += " "
    result = ""
    # Обробка блоками
    for i in range(0, len(text), block_size):
        block = text[i:i+block_size]
        new_block = [""] * block_size
        for j, pos in enumerate(key):
            new_block[j] = block[pos-1]
        result += "".join(new_block)
    return result


text = input("Введіть текст для шифрування: ")
key_input = input("Введіть ключ довжиною в 4 символи (наприклад: 3 1 4 2): ")

# перетворюємо рядок ключа у список
key = list(map(int, key_input.split()))

# перевірка, щоб ключ не був довший за 4
if len(key) > 4:
    print("Помилка: довжина ключа не може бути більше 4!")
else:
    encrypted = encrypt(text, key)
    print("Вхідний текст: ", text)
    print("Зашифрований: ", encrypted)