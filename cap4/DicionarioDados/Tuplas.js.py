ips = {}
resp = "S"

while resp == "S":
    ips[(input("Digite os dois primeiros octetos: "),
         input("Digite os dois últimos octetos: "))] = input("Nome da máquina: ")

    resp = input("Digite <S> para continuar: ").upper()

print("\n Exibindo ip ́s: ")
for ip in ips.keys():
    print("IP : ", ip[0] + "." + ip[1])

# exibindo máquinas com o mesmo endereço
print("Exibindo máquinas com o mesmo endereço: ")
pesquisa = input("Digite os dois últimos octetos: ")
for ip, nome in ips.items():
    print("Máquinas no mesmo endereço (redes diferentes)")
    if (ip[1] == pesquisa):
        print(nome)

# exibindo as máquinas que compõem uma mesma rede
print("Exibindo as máquinas que compõem uma mesma rede: ")
rede = input("Digite os dois primeiros octetos: ")
for ip, nome in ips.items():
    print("Máquinas na mesma rede")
    if (ip[0] == rede):
        print(nome)
