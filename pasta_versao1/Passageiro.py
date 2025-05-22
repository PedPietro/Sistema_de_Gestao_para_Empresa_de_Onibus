import os

class ManutencaoPassageiros:
    def __init__(self):
        self.passageiros = []  # lista que armazena os passageiros

    def incluir_passageiro(self):
        print("Incluir passageiro:")
        id_passageiro = input("Digite o ID do passageiro: ")
        nome = input("Digite o nome: ")
        cpf = input("Digite o CPF: ")
        passageiro = {"id": id_passageiro, "nome": nome, "cpf": cpf}
        self.passageiros.append(passageiro)
        print("Passageiro incluído com sucesso!\n")

    def excluir_passageiro(self):
        print("Excluir passageiro:")
        id_passageiro = input("Digite o ID do passageiro que deseja excluir: ")
        encontrou = False
        for p in self.passageiros:
            if p["id"] == id_passageiro:
                self.passageiros.remove(p)
                encontrou = True
                print("Passageiro excluído com sucesso!\n")
                break
        if not encontrou:
            print("Passageiro não encontrado.\n")

    def alterar_passageiro(self):
        print("Alterar passageiro:")
        id_passageiro = input("Digite o ID do passageiro a alterar: ")
        encontrou = False
        for p in self.passageiros:
            if p["id"] == id_passageiro:
                novo_nome = input("Digite o novo nome: ")
                novo_cpf = input("Digite o novo CPF: ")
                p["nome"] = novo_nome
                p["cpf"] = novo_cpf
                encontrou = True
                print("Passageiro alterado com sucesso!\n")
                break
        if not encontrou:
            print("Passageiro não encontrado.\n")

    def buscar_passageiro(self):
        print("Buscar passageiro:")
        id_passageiro = input("Digite o ID do passageiro a buscar: ")
        encontrou = False
        for p in self.passageiros:
            if p["id"] == id_passageiro:
                print("ID:", p["id"])
                print("Nome:", p["nome"])
                print("CPF:", p["cpf"])
                encontrou = True
                break
        if not encontrou:
            print("Passageiro não encontrado.\n")

    def listar_passageiro(self):
        print("Lista de passageiros:")
        if len(self.passageiros) == 0:
            print("Nenhum passageiro cadastrado.\n")
        else:
            for p in self.passageiros:
                print("ID:", p["id"])
                print("Nome:", p["nome"])
                print("CPF:", p["cpf"])
                print()

def main():
    sistema = ManutencaoPassageiros()
    opcao = 1
    while opcao != 0:
        os.system("cls") or None
        print("Menu de opções - Passageiros")
        print("0. Terminar a execução do programa")
        print("1. Incluir passageiro")
        print("2. Excluir passageiro")
        print("3. Alterar passageiro")
        print("4. Buscar passageiro")
        print("5. Listar passageiros")
        print()
        entrada = input("Digite a opção desejada: ")
        if entrada.isdigit():
            opcao = int(entrada)
        else:
            opcao = -1  # opção inválida

        if opcao == 1:
            sistema.incluir_passageiro()
        elif opcao == 2:
            sistema.excluir_passageiro()
        elif opcao == 3:
            sistema.alterar_passageiro()
        elif opcao == 4:
            sistema.buscar_passageiro()
        elif opcao == 5:
            sistema.listar_passageiro()
        elif opcao == 0:
            print("Encerrando o programa...")
        else:
            print("Opção inválida.\n")

        if opcao != 0:
            input("Tecle [Enter] para continuar...")

if __name__ == "__main__":
    main()
