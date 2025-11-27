import struct

def mul(a, b):
    return (a * b) % 0x10001 if a != 0 else (b % 0x10001)

def add(a, b):
    return (a + b) % 0x10000

def step1_to_4(X1, X2, X3, X4, K1, K2, K3, K4):
    Y1 = mul(X1, K1)
    Y2 = add(X2, K2)
    Y3 = add(X3, K3)
    Y4 = mul(X4, K4)
    return Y1, Y2, Y3, Y4

def step5_to_9(Y1, Y2, Y3, Y4, K5, K6):
    Z1 = Y1 ^ Y3
    Z2 = Y2 ^ Y4
    Z3 = mul(Z1, K5)
    Z4 = add(Z2, Z3)
    Z5 = mul(Z4, K6)
    Z6 = add(Z3, Z5)
    return Z3, Z4, Z5, Z6

def step10_to_14(Y1, Y2, Y3, Y4, Z3, Z4, Z5, Z6):
    X1_new = Y1 ^ Z5
    X2_new = Y3 ^ Z5
    X3_new = Y2 ^ Z6
    X4_new = Y4 ^ Z6
    return X1_new, X2_new, X3_new, X4_new

def final_transformation(X1, X2, X3, X4, K1, K2, K3, K4):
    Y1 = mul(X1, K1)
    Y2 = add(X2, K2)
    Y3 = add(X3, K3)
    Y4 = mul(X4, K4)
    return Y1, Y2, Y3, Y4

# --- IDEA шифрування одного блока ---
def IDEA_encrypt(block, round_keys):
    X1, X2, X3, X4 = block
    for i in range(8):
        K1, K2, K3, K4, K5, K6 = round_keys[i*6:(i+1)*6]
        Y1, Y2, Y3, Y4 = step1_to_4(X1, X2, X3, X4, K1, K2, K3, K4)
        Z3, Z4, Z5, Z6 = step5_to_9(Y1, Y2, Y3, Y4, K5, K6)
        X1, X2, X3, X4 = step10_to_14(Y1, Y2, Y3, Y4, Z3, Z4, Z5, Z6)
        if i != 7:
            X2, X3 = X3, X2
    Kf = round_keys[48:52]
    return final_transformation(X1, X2, X3, X4, *Kf)

# --- Генерація простого набору підключів (для тесту, без циклічного зсуву) ---
def generate_round_keys(key128):
    #  Приймаємо 128-бітний ключ як список 8 чисел по 16 біт
    round_keys = []
    for i in range(8):  # 8 раундів
        # беремо по 6 підключів на раунд, просто повторюючи ключові числа
        round_keys.extend([key128[(i+j)%8] for j in range(6)])
    # 4 ключі для фінального перетворення
    round_keys.extend(key128[:4])
    return round_keys

# --- Робота з файлами ---
def read_message_file(filename):
    with open(filename, "r") as f:
        text = f.read().strip()
    # перетворюємо символи на числа (0-9)
    return [int(c) for c in text]

def write_block_file(filename, blocks):
    with open(filename, "w") as f:
        for block in blocks:
            f.write(" ".join(str(x) for x in block) + "\n")

def main():
    message = read_message_file("message.txt")  # повідомлення у цифрах 0-9
    key128 = [0x1234,0x2345,0x3456,0x4567,0x5678,0x6789,0x7890,0x8901]  # приклад ключа
    round_keys = generate_round_keys(key128)

    # розбиваємо повідомлення на блоки по 4 числа
    blocks = []
    for i in range(0, len(message), 4):
        block = message[i:i+4]
        while len(block) < 4:
            block.append(0)  # доповнення нулями
        blocks.append(tuple(block))

    # шифрування
    encrypted_blocks = [IDEA_encrypt(b, round_keys) for b in blocks]

    write_block_file("cipher.txt", encrypted_blocks)
    print("Шифрування завершено, результат у cipher.txt")

if __name__ == "__main__":
    main()
