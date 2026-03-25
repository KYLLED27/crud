clientes = []
id_config = 1

def cadastrar_convidado():
    global id_config
    print("COMEÇANDO O CADASTRO...")
    nome = input("DIGITE O NOME DO CONVIDADO: ")
    cpf = input("DIGITE O CPF DO CONVIDADO: ")
    mesa = input("DIGITE A MESA: ")
    convidado = {"id" : id_config, "nome": nome, "cpf": cpf, "mesa": mesa, "checkin": False}
    id_config += 1
    clientes.append(convidado)
    print(clientes)

while True:
    cadastrar_convidado()