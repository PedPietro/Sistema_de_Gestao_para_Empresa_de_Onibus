import os
from Passageiro import ManutençãoPassageiros

def main():
    opcao = 1
    while opcao != 0:
        os.system("cls") or None
        print("\nSelecione uma opção:")
        print("0. Terminar a execução do programa")
        print("1. Incluir passageiros")
        print("2. Excluir passageiros")
        print("3. Alterar passageiros")
        print("4. Buscar passageiros")
        print("5. Listar passageiros")
        opcao = int(input("Opção: "))
        match opcao:
            case 1: incluir_passageiro()
            case 2: excluir_passageiro()
            case 3: alterar_passageiro()
            case 4: buscar_passageiro()
            case 5: listar_passageiro()
        if opcao != 0:
            input("Tecle [Enter] para prosseguir:")

if __name__ == "__main__":
    main()