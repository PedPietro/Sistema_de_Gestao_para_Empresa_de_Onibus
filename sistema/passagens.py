class ManutencaoPassagens:
    def __init__(self, conexao):
        self._conexao = conexao
        self.passagens = []  # lista que armazena as passagens
        
    def vendapassagens(self):
        print("Incluir passagem:")
        id_passagem = input("Digite o ID da passagem: ")
        id_passageiro = input("Digite o ID do passageiro: ")
        id_viagem = input("Digite o ID da viagem: ")
        assento = input("Digite o número do assento: ")
        preco = input("Digite o valor da passagem: ")

        passagem = {
            "id": id_passagem,
            "passageiro": id_passageiro,
            "viagem": id_viagem,
            "assento": assento,
            "preco": preco
        }

        self.passagens.append(passagem)
        print("Passagem incluída com sucesso!\n")

    def cancelar(self):
        print("Cancelar passagem:")
        id_passagem = input("Digite o ID da passagem que deseja cancelar: ")
        encontrou = False
        for p in self.passagens:
            if p["id"] == id_passagem:
                self.passagens.remove(p)
                encontrou = True
                print("Passagem cancelar com sucesso!\n")
                break
        if not encontrou:
            print("Passagem não encontrada.\n")

    def buscar(self):
        print("Buscar passagem:")
        id_passagem = input("Digite o ID da passagem a buscar: ")
        encontrou = False
        for p in self.passagens:
            if p["id"] == id_passagem:
                print("ID:", p["id"])
                print("Passageiro:", p["passageiro"])
                print("Viagem:", p["viagem"])
                print("Assento:", p["assento"])
                print("Preço:", p["preco"])
                encontrou = True
                break
        if not encontrou:
            print("Passagem não encontrada.\n")

    def listar(self):
        print("Lista de passagens:")
        if len(self.passagens) == 0:
            print("Nenhuma passagem cadastrada.\n")
        else:
            for p in self.passagens:
                print("ID:", p["id"])
                print("Passageiro:", p["passageiro"])
                print("Viagem:", p["viagem"])
                print("Assento:", p["assento"])
                print("Preço:", p["preco"])
                print()

    def disponibilidade(self):
        pass
