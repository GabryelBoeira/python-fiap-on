equipamentos=[]
valores=[]
seriais=[]
departamentos=[]

resposta="S"
while resposta=="S":
    equipamentos.append(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Número Serial: ")))
    departamentos.append(input("Departamento: "))
    resposta = input("Digite \"S\" para continuar: ").upper()

print("\n","-" * 30)

buscar=input("\nDigite o nome do equipamento que deseja buscar: ")
for indice in range(0, len(equipamentos)):
    if (buscar == equipamentos[indice]):
        print(f"Valor........: {valores[indice]}")
        print("Serial.......: ", seriais[indice])
