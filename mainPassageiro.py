class ManutençãoPassageiros:

    def __init__(self):
        pass

    def incluir():
        pass
            
    def excluir():
        pass

    def alterar():
        pass

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

