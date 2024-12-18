def perguntar():
    return input("\n<I> - Cadastrar um ususario \n"
                 "<P> - Consultar um ususario \n"
                 "<E> - Excluir um ususario \n"
                 "<L> - Listar um ususario \n"
                 "O que deseja fazer: ").upper()


def inserir(dicionario):
    dicionario[input("Digite o Login: ")] \
        = [input("Digite o nome: "),
           input("Digite a ultima data de acesso: "),
           input("Digite a ultima estacao de acesso: ").upper()]
    salvar(dicionario)


def listar():
    with open("bd_usuarios.txt", "r") as arquivo:
        for linha in arquivo.readlines():
            print(linha)


def excluir():
    login = input("login para excluir: ")
    with open("bd_usuarios.txt", 'r') as arquivo:
        lines = arquivo.readlines()
        arquivo.seek(0)
    with open("bd_usuarios.txt", 'w') as arquivo:
        for i, line in enumerate(lines, start=1):
            if login not in line:
                arquivo.write(line)
        arquivo.truncate()


def pesquisar():
    login = input("Qual login deseja pesquisar: ")
    with open("bd_usuarios.txt", 'a') as file:
        lines = file.readlines()
        for line_number, line in enumerate(lines, start=1):
            if login in line:
                print(f"found in line {line_number}: {line.strip()}")


def salvar(dicionario):
    with open("bd_usuarios.txt", "a") as arquivo:
        chave = list(dicionario)[-1]
        arquivo.write("\n" + chave + " : " + str(dicionario.get(chave)))
