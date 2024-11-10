import socket

resp = "S"
while resp == "S":
    url=input("Digite a url: ")
    ip = socket.gethostbyname(url)
    print("O IP da url informada é: ", ip)
    resp = input("Deseja continuar? <S/N>").upper()