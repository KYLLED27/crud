
convidados = [
    {"id": 1, "nome": "Lucas", "checkin": False},
    {"id": 2, "nome": "Paulo", "checkin": False},
    {"id": 3, "nome": "Barj", "checkin": False},
    {"id": 4, "nome": "Mario", "checkin": True},
    {"id": 5, "nome": "luis", "checkin": False},
    {"id": 6, "nome": "Perola", "checkin": True}
]


def fazer_check():
    try:
        id_input = int(input("Digite o ID: "))
    except ValueError:
        print("ID inválido.")
        return

    for convidado in convidados:
        if convidado.get("id") == id_input:
            if convidado.get("checkin"):
                print(f"O convidado {convidado['nome']} (ID {id_input}) já fez o checkin.")
            else:
                convidado["checkin"] = True
                print(f"Checkin registrado para {convidado['nome']} (ID {id_input}).")
            return

    print("ID não encontrado.")


if __name__ == "__main__":
    fazer_check()
    print(convidados)