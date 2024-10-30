usuarios = {}
emails = ["m0x1M@example.com", "XvM2x@example.com", "XvM2x@example.com", "5f3iP@example.com", "XvM2x@example.com"]

tuplas = list(enumerate(emails))

#criando os dados
for chave in range(0, len(tuplas)):
    print("Email: ", tuplas[chave][1])
    usuarios[tuplas[chave]] = [
        input("Digite o Nome: "),
        input("Digite a Senha: ")]

#mostrando os dados
for chave, dado in usuarios.items():
    print("_______\n")
    print("Usuario: ", chave[0])
    print("Email: ", chave[1])
    print("Nome: ", dado[0])
    print("Senha: ", dado[1])