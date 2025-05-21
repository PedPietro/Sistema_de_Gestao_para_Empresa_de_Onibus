import pyodbc as bd
import getpass as gp
import os

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
        print("Operações disponíveis")
        print("========= ===========\n")
        print("0 - Terminar este programa")
        print("1 - Incluir departamentos")
        print("2 - Alterar departamentos") 
        print("3 - Excluir departamentos")
        print("4 - Listar departamentos")
        opcao = int(input("\nDigite o número da opção desejada:"))
        match opcao:
            case 1: incluir()
            case 2: alterar()
            case 3: excluir()
            case 4: listar()

