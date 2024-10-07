from Modularizacao.FuncaoModularizacao import *

minhaLista = []

print("Preenchendo")
preencherInventario(minhaLista)

print("\nExibindo")
exibirInventario(minhaLista)

print("\nLocalizando")
localizarPorNome(minhaLista)

print("\nDepreciando")
depreciarPorNome(minhaLista, int(10))

print("\nExcluindo")
print(excluirPorSerial(minhaLista))
exibirInventario(minhaLista)

print("\nResumindo")
resumirValores(minhaLista)
