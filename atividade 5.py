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
    
def listar():
    for lista in clientes:
        print("id =", lista["id"])
        print("nome =", lista["nome"])
        print("cpf =", lista["cpf"])
        print("mesa =", lista["mesa"])

def buscar():
    busca_input = int(input("DIGITE O ID DO CONVIDADO: "))
    encontrado = False
    for busca in clientes:
        if busca["id"] == busca_input:
            print("id =", busca["id"])
            print("nome =", busca["nome"])
            print("cpf =", busca["cpf"])
            print("mesa =", busca["mesa"])
            encontrado = True
            break
    if not encontrado:
            print("CONVIDADO NÃO ENCONTRADO")

def editar():
    global id_config
    edita_input = int(input("DIGITE O ID DO CONVIDADO PARA EDITAR: "))
    for edit in clientes:
        if edit["id"] == edita_input:
            print("EDITANDO...")
            novo_nome = input("DIGITE O NOVO NOME: ")
            novo_cpf = input("DIGITE O NOVO CPF: ")
            mesa = input("DIGITE A NOVA MESA: ")
            edit["nome"] = novo_nome
            edit["cpf"] = novo_cpf
            edit["mesa"] = mesa
            break

def excluir():
    global id_config
    ex = int(input("DIGITE O ID PARA EXCLUIR"))
    for excluir2 in clientes:
        if excluir2["id"] == ex:
            clientes.remove(excluir2)
            print(clientes)
            
    
    
cadastrar_convidado()

excluir()