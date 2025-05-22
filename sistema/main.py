import os
import pyodbc as bd
import getpass as gp
import motorista
import onibus
import passageiros
import passagens
import viagem
import UF
import cidade

def conectouAoBancoDeDados() -> bool: # informará se conseguiu ou não conectar
    global conexao
    os.system('cls') or None
    senha = gp.getpass("Digite a senha do seu banco de dados:") # pede a senha
    try:
        conexao = bd.connect(driver="{SQL Server}",
                        server="regulus.cotuca.unicamp.br",
                        database="BDseuRA",
                        uid="BDseuRA", # seu username no servidor de BD
                        pwd=f"{senha}") # substitui variável senha
                        # pela senha digitada
        print("Conexão bem sucedida!")
        return True
    except:
        print("Não foi possível conectar ao banco de dados")
        return False

def seletor(): # CRUD: Create Retrieve Update Delete
    opcao = 1
    while opcao != 0:
        os.system('cls') or None
        print("1 - Motorista")
        print("2 - Ônibus")
        print("3 - Passageiro")
        print("4 - Viagem")
        print("5 - Cidade")
        print("6 - Passagem")
        print("0 - Sair")
        opcao = int(input("\nDigite o número da opção desejada:"))
        match opcao:
            case "1": motorista()
            case "2": onibus()
            case "3": passageiros()
            case "4": viagem()
            case "5": cidade()
            case "6": passagens()
            case "7": UF()

if __name__ == "__main__":
    seletor()