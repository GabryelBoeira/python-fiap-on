tabuada=int(input("digite um numero para ver sua tabuada: "))
print("Tabuada do numero: ", tabuada)
for valor in range(1,11,1):
    print(str(tabuada), "x", str(valor), "=", tabuada*valor)
print("fim do programa")