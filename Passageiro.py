class ManutençãoPassageiros:

    def __init__(self):
        self.passageiros = []
        
    def incluir_passageiro(self):
        id_passageiro = input("ID do passageiro: ")
        nome = input("Nome: ")
        cpf = input("CPF: ")
        passageiro = {"id": id_passageiro, "nome": nome, "cpf": cpf}
        self.passageiros.append(passageiro)
        print("Passageiro incluido com sucesso!\n")
            
    def excluir_passageiro(self):
        id_passageiro = input("ID do passageiro que deseja excluir: ")
        for p in self.passageiros:
            if p["id"] == id_passageiro:
                self.passageiros.remove(p)
                print("Passageiro excluido com sucesso!")
                return
        print("Passageiro não encontrado")
            
    def alterar_passageiro(self):
        id_passageiro = input("ID do passageiro a alterar: ")
        for p in self.passageiros:
            if p["id"] == id_passageiro:
                p["nome"] = input("Novo nome: ")
                p["cpf"] = input("Novo CPF: ")
                print("Passageiro alterado com sucesso!\n")
                return
        print("Passageiro não encontrado.\n")
                
    def buscar_passageiro(self):
        id_passageiro = input("ID do passageiro a buscar:")
        for p in self.passageiros:
            if p["id"] == id_passageiro:
                print(f"ID: {p['id']}, Nome: {p['nome']}, CPF: {p['cpf']}\n")
                return
            print("Passageiro não encontrado.\n")

    def listar_passageiro(self):
        if not self.passageiros:
            print("Nenhum passageiro cadastrado.\n")
        else:
            for p in self.passageiros:
                print(f"ID: {p['id']}, Nome: {p['nome']}, CPF: {p['cpf']}\n")
                print()

