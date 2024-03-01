import socket
import threading
from AES import AES

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
            message = client.recv(1024)
            decrypted_message = cipher.decrypt_text(message)
            print(f"Decrypted message: {decrypted_message}")
        except:
            print("An error occurred!")
            client.close()
            break

def write():
    while True:
        message = f'{nickname}: {input("")}'
        encrypted_message = cipher.encrypt_text(message)
        print(f"Encrypted message: {encrypted_message}")
        client.send(encrypted_message)

threading.Thread(target=receive).start()
threading.Thread(target=write).start()
