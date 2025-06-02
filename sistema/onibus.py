class ManutencaoOnibus:
    def __init__(self, conexao):
        self._conexao = conexao
        self.onibus = []  # lista que armazena os ônibus

    def incluir(self):
        print("Incluir ônibus:")
        id_onibus = input("Digite o ID do ônibus: ")
        placa = input("Digite a placa do ônibus: ")
        modelo = input("Digite o modelo do ônibus: ")
        capacidade = input("Digite a capacidade de passageiros: ")
        onibus = {"id": id_onibus, "placa": placa, "modelo": modelo, "capacidade": capacidade}
        self.onibus.append(onibus)
        print("Ônibus incluído com sucesso!\n")

    def excluir(self):
        print("Excluir ônibus:")
        id_onibus = input("Digite o ID do ônibus que deseja excluir: ")
        encontrou = False
        for o in self.onibus:
            if o["id"] == id_onibus:
                self.onibus.remove(o)
                encontrou = True
                print("Ônibus excluído com sucesso!\n")
                break
        if not encontrou:
            print("Ônibus não encontrado.\n")

    def alterar(self):
        print("Alterar ônibus:")
        id_onibus = input("Digite o ID do ônibus a alterar: ")
        encontrou = False
        for o in self.onibus:
            if o["id"] == id_onibus:
                nova_placa = input("Digite a nova placa: ")
                novo_modelo = input("Digite o novo modelo: ")
                nova_capacidade = input("Digite a nova capacidade: ")
                o["placa"] = nova_placa
                o["modelo"] = novo_modelo
                o["capacidade"] = nova_capacidade
                encontrou = True
                print("Ônibus alterado com sucesso!\n")
                break
        if not encontrou:
            print("Ônibus não encontrado.\n")

    def buscar(self):
        print("Buscar ônibus:")
        id_onibus = input("Digite o ID do ônibus a buscar: ")
        encontrou = False
        for o in self.onibus:
            if o["id"] == id_onibus:
                print("ID:", o["id"])
                print("Placa:", o["placa"])
                print("Modelo:", o["modelo"])
                print("Capacidade:", o["capacidade"])
                encontrou = True
                break
        if not encontrou:
            print("Ônibus não encontrado.\n")

    def listar(self):
        print("Lista de ônibus:")
        if len(self.onibus) == 0:
            print("Nenhum ônibus cadastrado.\n")
        else:
            for o in self.onibus:
                print("ID:", o["id"])
                print("Placa:", o["placa"])
                print("Modelo:", o["modelo"])
                print("Capacidade:", o["capacidade"])
                print()
