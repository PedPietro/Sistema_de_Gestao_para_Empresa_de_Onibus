import pyodbc
from conectaBD import conexao
import os

class VendaPassagens:
    def __init__(self):
        self.cursor = conexao.cursor()

    def menu(self):
        while True:
            os.system("cls") or None
            print("\n--- Menu de Venda de Passagens ---")
            print("1 - Realizar venda de passagem")
            print("2 - Listar vendas realizadas")
            print("0 - Voltar ao menu principal")
            opcao = input("Escolha uma opção: ")

            match opcao:
                case "1": self.vender_passagem()
                case "2": self.listar_vendas()
                case "0": break
                case _: print("Opção inválida.")

    def vender_passagem(self):
        try:
            id_viagem = input("ID da viagem: ")

            # Verifica se a viagem existe e pega a quantidade de vagas disponíveis
            consulta = """
                SELECT vagasDisponiveis
                FROM Viagem
                WHERE idViagem = ?
            """
            resultado = self.cursor.execute(consulta, id_viagem).fetchone()
            if resultado is None:
                print("Viagem não encontrada.\n")
                return
            
            vagas = resultado[0]
            if vagas <= 0:
                print("Não há vagas disponíveis para esta viagem.\n")
                return
            
            id_passageiro = input("ID do passageiro: ")

            # Verifica se o passageiro existe
            consulta = """
                SELECT nome FROM Passageiro WHERE idPassageiro = ?
            """
            resultado = self.cursor.execute(consulta, id_passageiro).fetchone()
            if resultado is None:
                print("Passageiro não encontrado.\n")
                return

            # Realiza a venda
            comando = """
                INSERT INTO VendaPassagem (idViagem, idPassageiro)
                VALUES (?, ?)
            """
            self.cursor.execute(comando, (id_viagem, id_passageiro))

            # Atualiza o número de vagas disponíveis
            comando = """
                UPDATE Viagem SET vagasDisponiveis = vagasDisponiveis - 1
                WHERE idViagem = ?
            """
            self.cursor.execute(comando, id_viagem)

            self.cursor.commit()
            print("Venda realizada com sucesso!\n")
        except Exception as e:
            print("Erro ao realizar a venda:", e)

    def listar_vendas(self):
        try:
            consulta = """
                SELECT v.idVenda, v.idViagem, v.idPassageiro, p.nome
                FROM VendaPassagem v
                JOIN Passageiro p ON v.idPassageiro = p.idPassageiro
                ORDER BY v.idVenda
            """
            resultado = self.cursor.execute(consulta).fetchall()
            if not resultado:
                print("Nenhuma venda registrada.\n")
                return

            print("\nIDVenda | IDViagem | IDPassageiro | Nome Passageiro")
            for venda in resultado:
                print(f"{venda[0]:<8} {venda[1]:<9} {venda[2]:<13} {venda[3]}")
        except Exception as e:
            print("Erro ao listar vendas:", e)
