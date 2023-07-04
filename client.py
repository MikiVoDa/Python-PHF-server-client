import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)      #conectam clientul la server
client.connect(("localhost", 1234))

done = False
while not done:     #loop pentru a mentine clientul in functiune

    mesaj = client.recv(1024).decode()
    if mesaj == "quit":
        done = True         #un cod simplu de client ce trimite si primeste mesaje
    else:
        print(mesaj)
        client.send(input("Client: ").encode())


client.close()
