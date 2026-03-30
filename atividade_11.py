convidados = [
    {"nome": "Lucas", "checkin": False},
    {"nome": "Paulo", "checkin": False},
    {"nome": "Barj", "checkin": False},
    {"nome": "Mario", "checkin": True},
    {"nome": "luis", "checkin": False},
    {"nome": "Perola", "checkin": True}
]
conf = 0

for confirmado in convidados:
    if confirmado["checkin"] == True:
        conf += 1

print(conf)