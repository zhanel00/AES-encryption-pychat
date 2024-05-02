import random

def generate_random_bits(length):
    """Генерация списка случайных битов."""
    return [random.randint(0, 1) for _ in range(length)]

def encode_qubits(bits, bases):
    """Кодирование кубитов в соответствии с битами и базисами."""
    # В этой симуляции: 0 -> +Z (0), 1 -> +X (1)
    # +Z: 0 (|0⟩), 1 (|1⟩); +X: 0 (|+⟩), 1 (|−⟩)
    return [(bit, base) for bit, base in zip(bits, bases)]

def measure_qubits(qubits, measurement_bases):
    """Измерение кубитов с учетом выбранных базисов."""
    measured_bits = []
    for qubit, measurement_base in zip(qubits, measurement_bases):
        # Если базис совпадает, измерение точное
        if qubit[1] == measurement_base:
            measured_bits.append(qubit[0])
        else:
            # Если базисы не совпадают, результат случаен
            measured_bits.append(random.randint(0, 1))
    return measured_bits

def sift_keys(sender_bases, receiver_bases, receiver_bits):
    """Согласование ключей между отправителем и получателем."""
    return [receiver_bits[i] if sender_bases[i] == receiver_bases[i] else '-' for i in range(len(sender_bases))]


length = 20  # Длина ключа
alice_bits = generate_random_bits(length)
alice_bases = generate_random_bits(length)
bob_bases = generate_random_bits(length)

# Алиса кодирует свои кубиты
encoded_qubits = encode_qubits(alice_bits, alice_bases)

# Боб измеряет кубиты
bob_measured_bits = measure_qubits(encoded_qubits, bob_bases)

# Согласование ключа
final_key = sift_keys(alice_bases, bob_bases, bob_measured_bits)

print("Alice's bits:   ", alice_bits)
print("Alice's bases:  ", alice_bases)
print("Bob's bases:    ", bob_bases)
print("Bob's measured: ", bob_measured_bits)
print("Final key:      ", final_key)
