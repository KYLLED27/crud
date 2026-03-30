lista = [
    "luis",
    "maria",
    "joao",
    "ana",
    "carlos"
]

busca = input("digite o nome: ")

busca = [nome for nome in lista if busca in nome]
print(busca)