class ManutencaoUF:
    def __init__(self,  conexao):
        self._conexao = conexao
        self.estados = []  # Lista para armazenar os estados (UF)

    def incluir(self):
        print("Incluir estado (UF):")
        sigla = input("Digite a sigla do estado (ex: SP): ")
        nome = input("Digite o nome do estado: ")

        estado = {
            "sigla": sigla,
            "nome": nome
        }

        self.estados.append(estado)
        print("Estado incluído com sucesso!\n")

    def excluir(self):
        print("Excluir estado (UF):")
        sigla = input("Digite a sigla do estado que deseja excluir: ")
        encontrou = False

        for e in self.estados:
            if e["sigla"] == sigla:
                self.estados.remove(e)
                encontrou = True
                print("Estado excluído com sucesso!\n")
                break

        if not encontrou:
            print("Estado não encontrado.\n")

    def alterar(self):
        print("Alterar estado (UF):")
        sigla = input("Digite a sigla do estado que deseja alterar: ")
        encontrou = False

        for e in self.estados:
            if e["sigla"] == sigla:
                novo_nome = input("Digite o novo nome do estado: ")
                e["nome"] = novo_nome
                encontrou = True
                print("Estado alterado com sucesso!\n")
                break

        if not encontrou:
            print("Estado não encontrado.\n")

    def buscar(self):
        print("Buscar estado (UF):")
        sigla = input("Digite a sigla do estado que deseja buscar: ")
        encontrou = False

        for e in self.estados:
            if e["sigla"] == sigla:
                print("Sigla:", e["sigla"])
                print("Nome:", e["nome"])
                encontrou = True
                break

        if not encontrou:
            print("Estado não encontrado.\n")

    def listar(self):
        print("Lista de estados (UF):")
        if len(self.estados) == 0:
            print("Nenhum estado cadastrado.\n")
        else:
            for e in self.estados:
                print("Sigla:", e["sigla"])
                print("Nome:", e["nome"])
                print()


def menu_uf():
    manutencao = ManutencaoUF()
    opcao = -1

    while opcao != 0:
        print("\n=== MENU DE MANUTENÇÃO DE ESTADOS (UF) ===")
        print("1 - Incluir estado")
        print("2 - Excluir estado")
        print("3 - Alterar estado")
        print("4 - Buscar estado")
        print("5 - Listar estados")
        print("0 - Sair")
        entrada = input("Digite a opção desejada: ")

        if entrada.isdigit():
            opcao = int(entrada)
        else:
            print("Opção inválida. Digite um número.")
            continue

        match opcao:
            case 1:
                manutencao.incluir()
            case 2:
                manutencao.excluir()
            case 3:
                manutencao.alterar()
            case 4:
                manutencao.buscar()
            case 5:
                manutencao.listar()
            case 0:
                print("Encerrando o menu de manutenção de estados.")
            case _:
                print("Opção inválida. Tente novamente.")


# Executar se for o programa principal
if __name__ == "__main__":
    menu_uf()
