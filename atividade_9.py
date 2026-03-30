convidados = [
    {"nome": "Lucas", "checkin": False},
    {"nome": "Paulo", "checkin": False},
    {"nome": "Barj", "checkin": False},
    {"nome": "Mario", "checkin": True},
    {"nome": "luis", "checkin": False},
    {"nome": "Perola", "checkin": True}
]

total = 0
totalok = 0
pendente = 0

for convidado in convidados:
    total += 1
    if convidado["checkin"] == True:
        totalok += 1
    else:
        pendente += 1

print("TOTAL: ", total)
print("TOTAL OK: ", totalok)
print("PENDENTE: ", pendente)