def preencherInventario(lista):
    resposta = "S"
    while resposta == "S":
        equipamento = [
            input("Equipamento: "),
            float(input("Valor: ")),
            int(input("Número Serial: ")),
            input("Departamento: ")]
        lista.append(equipamento)
        resposta = input("Digite \"S\" para continuar: ").upper()

#
def exibirInventario(lista):
    for elemento in lista:
        print("\nNome.........: ", elemento[0])
        print("Valor........: ", elemento[1])
        print("Serial.......: ", elemento[2])
        print("Departamento.: ", elemento[3])

#
def localizarPorNome(lista):
    busca = input("\nDigite o nome do equipamento que deseja buscar: ")
    for elemento in lista:
        if busca == elemento[0]:
            print("Valor..: ", elemento[1])
            print("Serial.:", elemento[2])

#
def depreciarPorNome(lista, porcentagem):
    equipamento = input("\nDigite o nome do equipamento que será depreciado: ")
    for elemento in lista:
        if equipamento == elemento[0]:
            print("Valor antigo: ", elemento[1])
            elemento[1] = elemento[1] * (1 - porcentagem/100)
            print("Novo valor: ", elemento[1])

#
def excluirPorSerial(lista):
    try:
        serial = int(input("\nDigite o serial do equipamento que deseja excluir: "))
        for elemento in lista:
            if serial == elemento[2]:
                lista.remove(elemento)
        return "Equipamento excluido com sucesso"
    except ValueError:
        return "Equipamento não encontrado"

#
def resumirValores(lista):
    valores = []
    for elemento in lista:
        valores.append(elemento[1])
    if len(valores) > 0:
        print("\nO equipamento mais caro custa: ", max(valores))
        print("O equipamento mais barato custa: ", min(valores))
        print("O total de equipamentos e: ", sum(valores))