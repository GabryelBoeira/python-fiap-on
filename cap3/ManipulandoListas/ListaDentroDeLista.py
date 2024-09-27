#from VariaveisListas.Lista import invetario

inventario=[]
resposta="S"

while resposta=="S":
    equipamento=[
        input("Equipamento: "),
        float(input("Valor: ")),
        int(input("Número Serial: ")),
        input("Departamento: ")]
    inventario.append(equipamento)
    resposta=input("Digite \"S\" para continuar: ").upper()

for elemento in inventario:
    print("\n Nome.........: ", elemento[0])
    print("Valor........: ", elemento[1])
    print("Serial.......: ", elemento[2])
    print("Departamento.: ", elemento[3])

busca=input("\nDigite o nome do equipamento que deseja buscar: ")
for elemento in inventario:
    if busca==elemento[0]:
        print("Valor..: ", elemento[1])
        print("Serial.:", elemento[2])

depreciacao=input("\nDigite o nome do equipamento que será depreciado: ")
for elemento in inventario:
    if depreciacao==elemento[0]:
        print("Valor antigo: ", elemento[1])
        elemento[1] = elemento[1] * 0.9
        print("Novo valor: ", elemento[1])

serial=int(input("\nDigite o serial do equipamento que deseja excluir: "))
for elemento in inventario:
    if serial==elemento[2]:
        inventario.remove(elemento)
        print("Equipamento excluido com sucesso")

for elemento in inventario:
    print("Nome.........: ", elemento[0])
    print("Valor........: ", elemento[1])
    print("Serial.......: ", elemento[2])
    print("Departamento.: ", elemento[3])
