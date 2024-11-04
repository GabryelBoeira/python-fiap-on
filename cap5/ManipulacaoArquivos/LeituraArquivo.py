# Leitura de arquivo por completo
with open("meu_primeiro_arquivo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

print("\n==========================\n")

#leitura linha por linha
with open("meu_primeiro_arquivo.txt", "r") as arquivo:
    for linha in arquivo.readlines():
        print(linha)
