nome=input("Qual seu nome? ")
idade=int(input("Qual e a sua idade? "))
if idade >= 65:
    print("O paciente ", nome ," possui atendimento prioritário")
else:
    print("O paciente ", nome, " possui atendimento normal")

print("Fim do programa")