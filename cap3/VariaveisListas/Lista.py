invetario=[]
resposta="S"

while resposta=="S":
    invetario.append(input("Equipamento: "))
    invetario.append(float(input("Valor: ")))
    invetario.append(int(input("Número Serial: ")))
    invetario.append(input("Departamento: "))
    resposta=input("Digite \"S\" para continuar: ").upper()

print("-"*30)
for elemento in invetario:
    print(elemento)