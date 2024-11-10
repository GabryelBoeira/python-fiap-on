import platform
import getpass
from datetime import datetime

from cap4.DicionarioDados.DicionarioExemplo import usuarios

print("Sistema Operacional: \n")

print("Nome da maquina: ...............", platform.node())
print("Sistema Operacional: ...........", platform.system())
print("Arquitetura: ...................", platform.architecture())
print("Versão do SO: ..................", platform.version())
print("Versão do Python: ..............", platform.python_version())
print("Processador: ...................", platform.processor())

print("\n---------------Data e Hora ----------------\n")

print("Data e Hora completa: ", datetime.now())
print("dia: ", datetime.now().day)
print("mes: ", datetime.now().month)
print("ano: ", datetime.now().year)
print("hora: ", datetime.now().hour)
print("minuto: ", datetime.now().minute)
print("segundo: ", datetime.now().second)

print("\n------------------------------------\n")

print("Usuário logado: ", getpass.getuser())
senha = getpass.getpass("Digite sua senha: ")

if senha == "1234":
    print("Acesso permitido")
else:
    print("Acesso negado")
