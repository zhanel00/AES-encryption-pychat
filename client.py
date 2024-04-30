import socket
import threading
from AES import AES
from sha256 import sha256

HOST = '127.0.0.1'
PORT = 65432
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
nickname = input("Choose your nickname: ")
password = input("Please write your secret password between your friends")

cipher = AES(password, 128)

def receive():
    while True:
        try:
            data = client.recv(1024)  # предполагаем, что это достаточно для получения одного сообщения и хэша
            encrypted_message = data[:-64]  # Всё кроме последних 64 символов - зашифрованное сообщение
            hash_received = data[-64:].decode()
            decrypted_message = cipher.decrypt_text(encrypted_message)
            print(f"Decrypted message: {decrypted_message}")

            recalculated_hash = sha256(encrypted_message)
            print(f"recalc: {recalculated_hash.hex()}")
            if recalculated_hash.hex() == hash_received:
                print("The message is authentic and untampered.")
            else:
                print("Warning: The message might have been tampered with!")
        except:
            print("An error occurred!")
            client.close()
            break

def write():
    while True:
        message = f'{nickname}: {input("")}'
        encrypted_message = cipher.encrypt_text(message)
        hashed_message = sha256(encrypted_message)
        hashed_message_hex = hashed_message.hex()  # Преобразование хэша в шестнадцатеричное представление

        data_to_send = encrypted_message + hashed_message_hex.encode()  # Объединяем и кодируем хэш в шестнадцатеричный вид
        print(f"Encrypted message: {encrypted_message.hex()}")
        print(f"Hashed message: {hashed_message_hex}")

        client.send(data_to_send)

threading.Thread(target=receive).start()
threading.Thread(target=write).start()
