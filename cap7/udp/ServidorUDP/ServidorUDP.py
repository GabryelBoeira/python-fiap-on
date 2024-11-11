from socket import *

servidor = 'localhost'
porta = 5000

obj_socket = socket(AF_INET, SOCK_DGRAM)
obj_socket.bind((servidor, porta))
print("Servidor pronto.......")

while True:

    dados, origem = obj_socket.recvfrom(65535)
    print('Origem: ', origem)
    print('Recebemos: ', dados.decode())
    resposta = input("Digite a Resposta: ")
    obj_socket.sendto(resposta.encode(), origem)

obj_socket.close()