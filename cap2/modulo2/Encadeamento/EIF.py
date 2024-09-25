nome=input("Digite seu nome: ")
idade=int(input("Digite sua idade: "))
doenca_infecciosa=input("Suspeita de doencas infectocontagiosas? ").upper()
if idade >= 65:
    print("O paciente ", nome, " possui atendimento prioritário")
elif doenca_infecciosa == "SIM":
    print("O paciente ", nome, " deve ser direcionado para a sala de espera reservada")
else:
    print("O paciente ", nome, " NAO precisa de atendimento prioritário e pode aguardar na sala normal!")