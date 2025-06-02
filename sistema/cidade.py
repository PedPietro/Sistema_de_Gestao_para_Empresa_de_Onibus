class ManutencaoCidade:
    def __init__(self, conexao):
        self._conexao = conexao
        self.cidades = []  # lista que armazena as cidades

    def incluir(self):
        print("Incluir cidade:")
        id_cidade = input("Digite o ID da cidade: ")
        nome = input("Digite o nome da cidade: ")
        estado = input("Digite o estado (sigla): ")
        cidade = {"id": id_cidade, "nome": nome, "estado": estado}
        self.cidades.append(cidade)
        print("Cidade incluída com sucesso!\n")

    def excluir(self):
        print("Excluir cidade:")
        id_cidade = input("Digite o ID da cidade que deseja excluir: ")
        encontrou = False
        for c in self.cidades:
            if c["id"] == id_cidade:
                self.cidades.remove(c)
                encontrou = True
                print("Cidade excluída com sucesso!\n")
                break
        if not encontrou:
            print("Cidade não encontrada.\n")

    def alterar(self):
        print("Alterar cidade:")
        id_cidade = input("Digite o ID da cidade a alterar: ")
        encontrou = False
        for c in self.cidades:
            if c["id"] == id_cidade:
                novo_nome = input("Digite o novo nome: ")
                novo_estado = input("Digite o novo estado (sigla): ")
                c["nome"] = novo_nome
                c["estado"] = novo_estado
                encontrou = True
                print("Cidade alterada com sucesso!\n")
                break
        if not encontrou:
            print("Cidade não encontrada.\n")

    def buscar(self):
        print("Buscar cidade:")
        id_cidade = input("Digite o ID da cidade a buscar: ")
        encontrou = False
        for c in self.cidades:
            if c["id"] == id_cidade:
                print("ID:", c["id"])
                print("Nome:", c["nome"])
                print("Estado:", c["estado"])
                encontrou = True
                break
        if not encontrou:
            print("Cidade não encontrada.\n")

    def listar(self):
        print("Lista de cidades:")
        if len(self.cidades) == 0:
            print("Nenhuma cidade cadastrada.\n")
        else:
            for c in self.cidades:
                print("ID:", c["id"])
                print("Nome:", c["nome"])
                print("Estado:", c["estado"])
                print()