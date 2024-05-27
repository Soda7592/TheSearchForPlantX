import socket
import random

def ServerInit() :
    s = socket.socket()
    h = b"PlantX"
    port = 33450 + random.randint(0, 9)
    s.bind((h, port))
    return (s, host, port)

if __name__ == "__main__" :
    s = socket.socket()
    h = socket.gethostname()
    port = 33450 + random.randint(0, 9)
    print((h, port))
    s.bind((h, port))
    s.listen(4)
    ac = 0
    print(f"Game room is : {h}, {port}")
    playerlist = []
    while ac < 4 :
        connect, addr = s.accept()
        playerlist.append([connect, addr])
        print(f"Player : {addr} joined !")
        connect.send(b"Wellcome, joined game room : {h}, {p}")
        ac += 1
    s.sendall(b"Game Start!")
    while True:
        (msg, addr) = s.recvfrom()
        print(f"{addr} says: {msg}")
    
