from Modularizacao.FuncaoModularizacao import *

minhaLista = []

print("Preenchendo")
preencherInventario(minhaLista)

print("Exibindo")
exibirInventario(minhaLista)

print("Localizando")
localizarPorNome(minhaLista)

print("Depreciando")
depreciarPorNome(minhaLista, int(10))

print("Excluindo")
print(excluirPorSerial(minhaLista))
exibirInventario(minhaLista)

print("Resumindo")
resumirValores(minhaLista)
