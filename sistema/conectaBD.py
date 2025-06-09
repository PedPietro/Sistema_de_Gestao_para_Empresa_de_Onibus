import pyodbc as bd
import os 
import getpass as gp

def conectouAoBancoDeDados():
    conexao = pyodbc.connect(
        "Driver={ODBC Driver 17 for SQL Server};"
        "Server=localhost;"         # ou NOME_DO_SERVIDOR\INSTANCIA
        "Database=NomeDoSeuBanco;"  # substitua pelo nome real do banco
        "Trusted_Connection=yes;"
    )
    return conexao
if __name__ == '__main__':
    conectouAoBancoDeDados()