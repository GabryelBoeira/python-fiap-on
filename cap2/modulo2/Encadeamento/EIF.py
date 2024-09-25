respondeu=False
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

while respondeu == False:
    doenca_infecciosa=input("Suspeita de doencas infectocontagiosas? ").upper()
    if idade>=65 and doenca_infecciosa=="SIM":
        respondeu = True
        print("O paciente será direcionado para sala AMARELA - COM prioridade")
    elif idade < 65 and doenca_infecciosa == "SIM":
        respondeu = True
        print("O paciente será direcionado para sala AMARELA - SEM prioridade")
    elif idade >= 65 and doenca_infecciosa == "NAO":
        respondeu = True
        print("O paciente será direcionado para sala BRANCA - COM prioridade")
    elif idade < 65 and doenca_infecciosa == "NAO":
        respondeu = True
        print("O paciente será direcionado para sala BRANCA - SEM prioridade")
    else:
        respondeu = False
        print("Responda a suspeita de doença infectocontagiosa com SIM ou NAO")

print("Fim")

