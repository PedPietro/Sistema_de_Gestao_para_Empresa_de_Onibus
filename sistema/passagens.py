class ManutencaoPassagens:
    def __init__(self):
        self.passagens = []  # lista que armazena as passagens

    def incluir(self):
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

    def excluir(self):
        print("Excluir passagem:")
        id_passagem = input("Digite o ID da passagem que deseja excluir: ")
        encontrou = False
        for p in self.passagens:
            if p["id"] == id_passagem:
                self.passagens.remove(p)
                encontrou = True
                print("Passagem excluída com sucesso!\n")
                break
        if not encontrou:
            print("Passagem não encontrada.\n")

    def alterar(self):
        print("Alterar passagem:")
        id_passagem = input("Digite o ID da passagem a alterar: ")
        encontrou = False
        for p in self.passagens:
            if p["id"] == id_passagem:
                novo_passageiro = input("Digite o novo ID do passageiro: ")
                nova_viagem = input("Digite o novo ID da viagem: ")
                novo_assento = input("Digite o novo número do assento: ")
                novo_preco = input("Digite o novo valor da passagem: ")

                p["passageiro"] = novo_passageiro
                p["viagem"] = nova_viagem
                p["assento"] = novo_assento
                p["preco"] = novo_preco
                encontrou = True
                print("Passagem alterada com sucesso!\n")
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
