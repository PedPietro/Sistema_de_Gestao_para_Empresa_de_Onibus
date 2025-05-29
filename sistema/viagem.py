import os
class Viagem():

    def excluir():
        pass

    def alterar():
        pass

    def buscar():
        pass

    def listar():
        pass

    def __init__(self):
        self.status = "planejada"
    
    def Registroinicio(self):
        self.status = "Em andamento"

    def Registrofinal(self):
        self.status = "Finalizada"
    
    def Liberarpassageirosevagas(self):
        pass
        




'''
import pyodbc
from conectaBD import conectouAoBancoDeDados


class Viagem:
    def __init__(self):
        if not conectouAoBancoDeDados():
            print("Erro na conexão. Encerrando...")
            exit()
        global conexao
        self.conexao = conexao
        self.cursor = self.conexao.cursor()

    def listar(self):
        print("\n---- Lista de Viagens ----")
        try:
            self.cursor.execute("SELECT * FROM Viagem")
            viagens = self.cursor.fetchall()
            for v in viagens:
                print(f"ID: {v.idViagem}, Origem: {v.origem}, Destino: {v.destino}, "
                      f"Data: {v.data}, Horário: {v.horario}, Status: {v.status}")
        except:
            print("Erro ao listar viagens")

    def buscar(self):
        id_viagem = input("Digite o ID da viagem: ")
        try:
            self.cursor.execute("SELECT * FROM Viagem WHERE idViagem = ?", id_viagem)
            v = self.cursor.fetchone()
            if v:
                print(f"ID: {v.idViagem}, Origem: {v.origem}, Destino: {v.destino}, "
                      f"Data: {v.data}, Horário: {v.horario}, Status: {v.status}")
            else:
                print("Viagem não encontrada")
        except:
            print("Erro ao buscar viagem")

    def excluir(self):
        id_viagem = input("Digite o ID da viagem que deseja excluir: ")
        try:
            self.cursor.execute("DELETE FROM Viagem WHERE idViagem = ?", id_viagem)
            self.conexao.commit()
            print("Viagem excluída com sucesso")
        except:
            print("Erro ao excluir viagem")

    def alterar(self):
        id_viagem = input("Digite o ID da viagem a alterar: ")
        try:
            self.cursor.execute("SELECT * FROM Viagem WHERE idViagem = ?", id_viagem)
            if not self.cursor.fetchone():
                print("Viagem não encontrada")
                return

            origem = input("Nova origem: ")
            destino = input("Novo destino: ")
            data = input("Nova data (AAAA-MM-DD): ")
            horario = input("Novo horário (HH:MM): ")
            status = input("Novo status (planejada, em andamento, finalizada): ")

            self.cursor.execute(
                "UPDATE Viagem SET origem = ?, destino = ?, data = ?, horario = ?, status = ? WHERE idViagem = ?",
                (origem, destino, data, horario, status, id_viagem)
            )
            self.conexao.commit()
            print("Viagem alterada com sucesso")
        except:
            print("Erro ao alterar viagem")

    def Registroinicio(self):
        id_viagem = input("Digite o ID da viagem para iniciar: ")
        try:
            self.cursor.execute("UPDATE Viagem SET status = 'em andamento' WHERE idViagem = ?", id_viagem)
            self.conexao.commit()
            print("Status da viagem alterado para 'em andamento'")
        except:
            print("Erro ao registrar início da viagem")

    def Registrofinal(self):
        id_viagem = input("Digite o ID da viagem para finalizar: ")
        try:
            self.cursor.execute("UPDATE Viagem SET status = 'finalizada' WHERE idViagem = ?", id_viagem)
            self.conexao.commit()
            print("Status da viagem alterado para 'finalizada'")
        except:
            print("Erro ao registrar final da viagem")

    def Liberarpassageirosevagas(self):
        id_viagem = input("Digite o ID da viagem para liberar passageiros e vagas: ")
        try:
            # Supondo que ao finalizar, limpamos as passagens dessa viagem
            self.cursor.execute("DELETE FROM Passagem WHERE idViagem = ?", id_viagem)
            self.conexao.commit()
            print("Passageiros e vagas liberados com sucesso")
        except:
            print("Erro ao liberar passageiros e vagas")

'''
#cod exemplo de IA