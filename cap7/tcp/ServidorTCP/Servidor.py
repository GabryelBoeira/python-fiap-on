from socket import *

servidor = "127.0.0.1"
porta = 5000

obj_socket = socket(AF_INET, SOCK_STREAM)

obj_socket.bind((servidor, porta))
obj_socket.listen(5)

print("Servidor aguardando conexão...")

while True:
    con, cliente = obj_socket.accept()
    print("Conectado com: ", cliente)
    while True:
        msg_recebida = str(con.recv(1024))
        print("Recebido: ", msg_recebida)
        msg_enviada = b'Ola cliente'
        con.send(msg_enviada)
        break
    con.close()