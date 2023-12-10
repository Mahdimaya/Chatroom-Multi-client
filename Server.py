import socket
import threading

# Configuration du serveur
HOST = '127.0.0.5'
PORT = 55555

# Création du socket serveur
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

# Liste pour stocker les connexions clients
clients = []

def broadcast(message, sender):
    for client in clients:
        if client != sender:
            try:
                client.send(message)
            except:
                # En cas d'erreur, retire le client de la liste
                clients.remove(client)

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            if message:
                print(message.decode('utf-8'))
                broadcast(message, client)
            else:
                # En cas de déconnexion, retire le client de la liste
                clients.remove(client)
        except:
            break

# Écoute des connexions entrantes
server.listen()

print(f"Serveur en écoute sur {HOST}:{PORT}")

while True:
    # Accepte une connexion
    client, address = server.accept()
    print(f"Connexion établie avec {str(address)}")

    # Ajoute le client à la liste
    clients.append(client)

    # Crée un thread pour gérer le client
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()