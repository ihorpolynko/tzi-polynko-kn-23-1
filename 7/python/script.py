P = 5
Q = 7
e = 5
d = 5

n = P * Q # модуль
phi = (P - 1) * (Q - 1)

# Функція шифрування одного символу (цифри)
def encrypt_digit(m):
    return pow(m, e, n)

# Функція дешифрування одного числа
def decrypt_digit(c):
    return pow(c, d, n)

# Зчитуємо повідомлення з файлу
with open("input.txt", "r") as f:
    message = f.read().strip()

# Перевірка цифр
if not message.isdigit():
    raise ValueError("Повідомлення повинно містити тільки цифри 0-9.")

# Шифрування
cipher = [encrypt_digit(int(ch)) for ch in message]

# Запис криптограми у файл
with open("cipher.txt", "w") as f:
    f.write(" ".join(map(str, cipher)))

# Дешифрування
restored_digits = [decrypt_digit(int(x)) for x in cipher]
restored_message = "".join(str(x) for x in restored_digits)

# Запис відновленого повідомлення
with open("output.txt", "w") as f:
    f.write(restored_message)

print("Вихідне:", message)
print("Криптограма:", cipher)
print("Розшифровано:", restored_message)