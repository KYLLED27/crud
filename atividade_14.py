convidados = [
    {"nome": "Lucas", "checkin": False},
    {"nome": "Paulo", "checkin": False},
    {"nome": "Barj", "checkin": False},
    {"nome": "Mario", "checkin": True},
    {"nome": "luis", "checkin": False},
    {"nome": "Perola", "checkin": True}
]

lista = sorted(convidados, key=lambda x: x["nome"])

nomes_apenas = [pessoa["nome"] for pessoa in lista]

print(nomes_apenas)