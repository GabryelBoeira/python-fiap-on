def perguntar():
    return input("\nO que deseja fazer? \n"
          "<I> - Cadastrar um ususario\n"
          "<P> - Consultar um ususario\n"
          "<E> - Excluir um ususario\n"
          "<L> - Listar um ususario :").upper()

def inserir(dicionario):
    dicionario[input("Digite o Login: ")] \
        = [input("Digite o nome: "),
           input("Digite a ultima data de acesso: "),
           input("Digite a ultima estacao de acesso: ").upper()]

def listar(dicionario):
    print(dicionario)

def excluir(dicionario):
    nome = input("Nome: ")
    if nome in dicionario:
        del dicionario[nome]
    else:
        print("Usuário não encontrado")

def pesquisar(dicionario):
    lista = dicionario.get(input("Qual login deseja pesquisar: "))
    if lista is not None:
        print("Nome: ", lista[1])
        print("data_acesso: ", lista[2])
    else:
        print("Usuário não encontrado")