base_dados = []

with open("iris.data", "r") as arquivo:
    for registro in arquivo.readlines():
        base_dados.append(registro.split(","))

print(base_dados)
print("===============")

#lendo registro e coluna
print(base_dados[0][0])

#somando registro e coluna
print(float(base_dados[0][0]) + float(base_dados[0][1]))

