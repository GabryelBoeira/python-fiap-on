usuarios = {}
print("Usuários:", usuarios)

#add data to dictionary
usuarios = {
    "chaves" : ["Chaves do 8", "24/10/2024", "Recep_01"],
    "quicos" : ["Quicos das flores", "20/10/2024", "Raiox_03"],
}
print("Usuários:", usuarios)

#add new user to dictionary
usuarios["florinda"] = ["Dona Florinda", "23/10/2024", "Raiox_01"]
print("Usuários:", usuarios)


print("###-----###")
print(usuarios.get("chaves"))
