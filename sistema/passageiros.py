import os
from conectaBD import conexao
import pyodbc as bd
import getpass as gp

class ManutencaoPassageiros:
    def incluir():              # Salva os dados do formulário (incluídos ou editados) no banco de dados
        meuCursor = conexao.cursor() # cria um cursor, objeto de comandos de SQL
        cpf = 1
        while cpf != 0:
            # pedimos que o usuário digite os dados do novo Passageiro
            cpf = int(input("CPF do Passageiro (0 para terminar): "))
            
            if cpf != 0: # usuário não quer terminar o cadastro
                nome = input("Nome do Passageiro: ")
                telefone = input("Cpf do Passageiro: ")
                email = input("Email do Passageiro: ")
    
                # montamos string com o comando Insert contendo os dados digitados:
                sComando =  "insert into Passageiro " +\
                            " (cpf, nome, telefone, email)"+\
                            "VALUES (?, ?, ?, ?)"
                
                # fazemos o cursor enviar ao servidor, para análise e execução,
                # a string com o comando Insert acima
                try: 
                    meuCursor.execute(sComando,[cpf, nome, telefone, email])
                    print("Passageiro incluído com sucesso!")
                except: # em caso de erro
                    print("Não foi possível incluir. Pode haver Passageiro repetido.")
    def excluir():
        pass

    def alterar():
        pass
    
    def buscar():
        pass

    def listar():
        pass