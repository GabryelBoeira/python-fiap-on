texto = "Eu gosto de programar em Python"

#Consulta a primeira ocorência
print(texto.find("o"))

#consulta a ultima ocorência
print(texto[texto.find("o") + 1:].find("o"))

# Dividindo o texto
print(texto.split(" "))

