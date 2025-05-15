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
