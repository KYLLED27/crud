convidados = [
    {"nome": "Lucas", "checkin": False},
    {"nome": "Paulo", "checkin": False},
    {"nome": "Barj", "checkin": False},
    {"nome": "Mario", "checkin": True},
    {"nome": "luis", "checkin": False},
    {"nome": "Perola", "checkin": True}
]

pendentes = 0

for pendente in convidados:
    if pendente["checkin"] == False:
        pendentes += 1
        
print(pendentes)