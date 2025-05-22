class ManutencaoCidade:
    def __init__(self):
        self.cidades = [] #lista que armazena as cidades

    def incluir(self):
        print("incluir cidade:")
        id_cidade = input("Digite o ID da cidade:")
        nome = input("Digite o nome da cidade:")
        estado = input("Digite o estado(sigla):")
        cidade = {"id": id_cidade, "nome": nome, "estado": estado}
        self.cidades.append(cidade)
        print("Cidade incluída com sucesso!\n")
       
    def excluir(self):
        print("Excluir motorista:")
        id_motorista = input("Digite o ID do motorista que deseja excluir:")

        encontrou = False
        for m in self.motoristas:
            if m ["id"] == id_motorista:
                self.motoristas.remove(m)

        encontrou = True
        print("Motorista exclúido com sucesso!\n")
        break
    if not encontrou:
        print("Motorista não encontrado.\n")

    def alterar(self):
        pass
    
    def buscar(self):
        pass

    def listar(self):
        pass