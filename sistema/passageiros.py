import os
from conectaBD import conectouAoBancoDeDados() as conexao
import pyodbc as bd
import getpass as gp

class ManutencaoPassageiros:
    def __init__(self):
        self.passageiros = [] # vetor que guarda os passageiros

    def cadastropassageiros():              # Salva os dados do formulário (incluídos ou editados) no banco de dados
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
                            "VALUES ("+cpf+", "+nome+", "+telefone+", "+email+")"
                
                # fazemos o cursor enviar ao servidor, para análise e execução,
                # a string com o comando Insert acima
                try: 
                    meuCursor.execute(sComando)
                    print("Passageiro incluído com sucesso!")
                except: # em caso de erro
                    print("Não foi possível incluir. Pode haver Passageiro repetido.")
    def excluir(self):
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

    def alterar(self):
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
    
    def buscar(self):
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

    def listar(self):
        print("Lista de passageiros:")
        if len(self.passageiros) == 0:
            print("Nenhum passageiro cadastrado.\n")
        else:
            for p in self.passageiros:
                print("ID:", p["id"])
                print("Nome:", p["nome"])
                print("CPF:", p["cpf"])
                print()