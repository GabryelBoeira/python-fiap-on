from cap4.DicionarioDados.Funcoes import *

usuarios = {}
opcao = perguntar()

while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
    if opcao.upper() == "I":
        inserir(usuarios)
    elif opcao.upper() == "P":
        pesquisar(usuarios)
    elif opcao.upper() == "E":
        excluir(usuarios)
    elif opcao.upper() == "L":
       listar(usuarios)

    opcao = perguntar()
