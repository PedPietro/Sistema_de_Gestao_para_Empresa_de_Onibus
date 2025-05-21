class ManutençãoPassageiros:
    def __init__(self):
        passageiros = []
    
     #lista que guarda os passageiros
    def incluir():
        id_passageiro = input("ID do passageiro: ")
        nome = input("Nome: ")
        cpf = input("CPF: ")
        passageiro = {"id": id_passageiro, "nome": nome, "cpf": cpf}
        passageiros.append(passageiro)
        print("Passageiro incluido com sucesso!\n")
            
    def excluir():
        id_passageiro = input("ID do passageiro que deseja excluir: ")
        for p in passageiros:
            if p["id"] == id_passageiro:
                passageiros.remove(p)
                print("Passageiro excluido com sucesso!")
                return
        print("Passageiro não encontrado")
            
    def alterar():
        id_passageiro = input("ID do passageiro que deseja alterar: ")
        for p in 

    def buscar():
        id_passageiro = input("ID do passageiro a buscar:")
        for p in passageiros:
            if p["id"] == id_passageiro:
                print(f"ID: {p['id']}, Nome: {p['nome']}, CPF: {p['cpf']}\n")
                return
            print("Passageiro não encontrado.\n")

    def listar():
        if not passageiros:
            print("Nenhum passageiro cadastrado.\n")
        else:
            for p in passageiros:
                print(f"ID: {p['id']}, Nome: {p['nome']}, CPF: {p['cpf']}\n")
                print()

