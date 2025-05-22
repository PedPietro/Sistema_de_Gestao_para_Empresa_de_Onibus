import pyodbc

conexao = None

def conectar(ra: str, senha: str):
    global conexao
    try:
        conexao = pyodbc.connect(
            driver="{SQL Server}",
            server="regulus.cotuca.unicamp.br",
            database=f"BD:{ra}",
            uid=f"BB{ra}",
            pwd=senha
        )
        print("conexão com o banco de dados estabelecida com sucesso!")
        return True
    except Exception as erro:
        print("ERRO ao conectar ao banco de dados:", erro)
        return False
