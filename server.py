import socket
import random

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)          #creeam socketul si il connectam clientul
server.bind(("localhost", 1234))
server.listen()
client, addr = server.accept()

alegeri = ["P", "F", "H"]       #alegerile posibile si o variabila care are sa devinarandom mai tarziu
alegere = ""

done = False
while not done:
    puncte_server = 0
    puncte_player = 0

    client.send("Scrie 'START' pentru a incepe!".encode())      #scriem 'START' pentru a incepe
    mesaj = client.recv(1024).decode()

    if mesaj == "quit":         #un simplu loop pentru a tine serverul in viata
        done = True

    if mesaj == "START":
        game_done = False
        while not game_done:        #un al loop pentru jocul propriu zis de piatra foarfece hartie

            if puncte_player == 2:
                client.send(f"Ai castigat din {puncte_server+puncte_player} incercari!\n"
                            f"Scrie ceva pentru a continua.".encode())
                mesaj = client.recv(1024).decode()      #workaround-ul meu de a putea continua dialogul dintre server-client
                game_done = True                        #analog pentru orice linie de cod dupa ce trimit ceva clientului
                break
            elif puncte_server == 2:
                client.send("Serverul a castigat!\nScrie ceva pentru a continua.".encode())
                mesaj = client.recv(1024).decode()
                game_done = True
                break
            else:
                client.send("Alege!\n(P, F, H):".encode())
                mesaj = client.recv(1024).decode()
                alegere = random.choice(alegeri)

            if mesaj == "P":
                if alegere == "F":
                    client.send("Ai castigat!\nScrie ceva pentru a continua.".encode())
                    puncte_player += 1
                    mesaj = client.recv(1024).decode()
                else:
                    client.send("Ai pierdut!\nScrie ceva pentru a continua.".encode())
                    puncte_server += 1
                    mesaj = client.recv(1024).decode()
            elif mesaj == "F":
                if alegere == "H":
                    client.send("Ai castigat!\nScrie ceva pentru a continua.".encode())
                    puncte_player += 1
                    mesaj = client.recv(1024).decode()
                else:
                    client.send("Ai pierdut!\nScrie ceva pentru a continua.".encode())
                    puncte_server += 1
                    mesaj = client.recv(1024).decode()
            elif mesaj == "H":
                if alegere == "P":
                    client.send("Ai castigat!\nScrie ceva pentru a continua.".encode())
                    puncte_player += 1
                    mesaj = client.recv(1024).decode()
                else:
                    client.send("Ai pierdut!\nScrie ceva pentru a continua.".encode())
                    puncte_server += 1
                    mesaj = client.recv(1024).decode()
            else:
                client.send("Nu există o astfel de variantă. Verificați și introduceți din nou.\n"
                            "Scrie ceva pentru a continua.".encode())
                mesaj = client.recv(1024).decode()

client.close()      #dupa ce se incheie loop-ul inchidem serverul si clientul
server.close()
