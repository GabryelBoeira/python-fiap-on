from cap5.DicionariosArquivos.Funcoes import *

usuarios = {}
opcao = perguntar()

while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
    if opcao.upper() == "I":
        inserir(usuarios)
    elif opcao.upper() == "P":
        pesquisar()
    elif opcao.upper() == "L":
        listar()
    elif opcao.upper() == "E":
        excluir()
    opcao = perguntar()