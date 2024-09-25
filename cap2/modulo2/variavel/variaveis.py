nome=input("Digite um funcionário: ")
empresa=input("Digite a instituição: ")
qtde_funcionarios=int(input("Digite a qtde de funcionários: "))
mediaMensalidade=float(input("Digite a média da mensalidade: "))
print("\n"+ nome+ " trabalha na empresa " + empresa)
print("Possui: ", qtde_funcionarios, " funcionarios.")
print("A média da mensalidade é de: " + str(mediaMensalidade))

print("\n====================Verifique os tipos de dados abaixo=====================")
print("O tipo da variável nome é: ", type(nome))
print("O tipo da variável empresa é: ", type(empresa))
print("O tipo da variável qtde_funcionários é: ", type(qtde_funcionarios))
print("O tipo da variável mediaMensalidade é: ", type(mediaMensalidade))

