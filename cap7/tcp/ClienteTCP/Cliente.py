from socket import *

servidor = "127.0.0.1"
porta = 5000

msg = bytes(input("Digite a mensagem: "), "utf-8")

obj_socket = socket(AF_INET, SOCK_STREAM)
obj_socket.connect((servidor, porta))
obj_socket.send(msg)

msg_recebida = obj_socket.recv(1024)
print("Enviado: ", msg.decode("utf-8"))
print("Recebido: ", msg_recebida.decode("utf-8"))

obj_socket.close()