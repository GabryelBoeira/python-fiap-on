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

print("-"*30)
depreciacao=input("\nDigite o nome do equipamento que será depreciado: ")
for indice in range(0, len(equipamentos)):
    if depreciacao==equipamentos[indice]:
        print("Valor antigo: ", valores[indice])
        valores[indice] = valores[indice] * 0.9
        print("Novo valor: ", valores[indice])

print("-" * 30)
for indice in range(0, len(equipamentos)):
    print(f"\nEquipamento..: {indice + 1}")
    print(f"Nome.........: {equipamentos[indice]}")
    print(f"Valor........: {valores[indice]}")
    print("Serial.......: ", seriais[indice])
    print(f"Departamento.: {departamentos[indice]}")
