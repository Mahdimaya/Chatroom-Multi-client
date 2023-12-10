import socket
import threading

# Configuration du client
HOST = '127.0.0.5'
PORT = 55555

# Création du socket client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            print(message)
        except:
            # En cas d'erreur, quitte le programme
            print("Erreur de connexion au serveur.")
            client.close()
            break

def write():
    while True:
        message = input('')
        client.send(message.encode('utf-8'))

# Crée deux threads pour recevoir et envoyer des messages
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
