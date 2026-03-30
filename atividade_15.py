convidados = []
id_couter = 1

def iniciar_menu():
    print("\n ----- menu ----")
    print("1.CADASTRAR CONVIDADO")
    print("2.LISTAR ")
    print("3.BUSCAR CONVIDADO POR ID")
    print("4.ATUALIZAR CONVIDADO")
    print("5.REMOVER")
    print("6.SAIR")

def cadastrar():
    global id_couter
    print("COMEÇANDO CADASTRO..")
    while True:
        nome = input("DIGITE O NOME: ")
        if len(nome) >= 3:
            print("NOME VALIDO")
            break
        else:
            print("INVALIDO")
    while True:       
        cpf = input("DIGITE O CPF: ")
        duplicado = False
        for indentificar in convidados:
            if indentificar["cpf"] == cpf:
                duplicado = True
                
            if duplicado == True:
                print("CPF DUPLICADO")
                break
        if len(cpf) == 11 and cpf.isdigit():
            print("CPF ACEITO")
            break
        else:
            print("CPF INCORRETO")
    mesa = input("DIGITE A MESA: ")
    convidado = {"id": id_couter,"nome": nome, "cpf": cpf, "mesa": mesa, "checkin": False}
    id_couter += 1
    convidados.append(convidado)
    print("CONVIDADO CADASTRADO")

def listar():
    for lista in convidados:
        print("id =", lista["id"])
        print("nome =", lista["nome"])
        print("cpf =", lista["cpf"])
        print("mesa =", lista["mesa"])
        print("-" * 20)
        
def buscar():
    busca_input = input("DIGITE O ID DO PRODUTO PARA LOCALIZAR: ")
    for busca in convidados:
        busca["id"] == busca_input
        print("CONVIDADO")
        print("NOME", busca["nome"])
        print("CPF", busca["cpf"])
        print("MESA", busca["mesa"])

def atualizar():
    busca_input = input("DIGITE O ID DO CONVIDADO PARA ATUALIZAR: ")
    for busca in convidados:
        busca["id"] == busca_input
        novo_nome = input("DIGITE O NOVO NOME: ")
        novo_cpf = input("DIGITE O NOVO CPF: ")
        nova_mesa = input("DIGITE A NOVA MESA: ")
        busca["nome"] = novo_nome
        busca["cpf"] = novo_cpf
        busca["mesa"] = nova_mesa
        print("CONVIDADO ATUALIZADO COM SUCESSO")
        break

def remover():
    busca_input1 = input("DIGITE O ID DO CONVIDADO PARA REMOVER: ")
    for deletar in convidados:
        if deletar["id"] == int(busca_input1):
            convidados.remove(deletar)
            print("CONVIDADO DELETADO")
            break
            
while True:
    iniciar_menu()
    escolha = input()
    if escolha == "1":
        print("PRONTO PRA CADASTRAR")
        cadastrar()
        
    elif escolha == "2":
        print("LISTA COMPLETA")
        listar()
        
    elif escolha == "3":
        print("BUSQUE SEU CONVIDADO")
        buscar()
    elif escolha == "4":
        print("ATUALIZE SEU CONVIDADO")
        atualizar()
    elif escolha == "5":
        print("REMOVA SEU CONVIDADO")
        remover()
    elif escolha == "6":
        print("SAINDO...")
        break
    else:
        print("nao podi")