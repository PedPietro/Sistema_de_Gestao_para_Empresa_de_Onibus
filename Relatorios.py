import  pyodbc as bd
import os
from conectaBD import conexao

class Relatorios:
    def __init__(self):
        self.cursor = conexao.cursor()
        
    def seletor(self):
        while True:
            os.system("cls") or None
            print("\n--- Menu de Relatórios ---")
            print("0 - Voltar ao menu principal")
            print("1 - Passageiro em uma vaigem")
            opcao = input("EScolha uma opcao:") 
            match opcao:
                case "0": break 
                case "1": self.relatorios_passageiros_viagem()
                case _: print("Opção inválida.")

    def relatorios_passageiros_viagem(self):
        try:
            id_viagem = input("Digite o Id da viagem:")

            consulta = """
            SELECT p.nome, p.cpf, pa.cpf, pa.data_e_hora
            FROM passagem passJOIN passageiro p ON pa.cpf = p.cpf
            WHERE pa.idViagem = ?
            ORDER BY pa.assento
            """

            resultado = self.cursor.execute(consulta, id_viagem)()

            if not resultado:
                print("Nenhum passageiro encontrado para esta viagem.") 
                return
        
            print("\n--- Passageiros na Viagem---")
            print("Nome                     | CPF        |Assento |Data e Hora")
            print("-" * 60)
            for linha in resultado:
                nome, cpf, assento, data_hora = linha
                print(f"{nome:<20}{cpf:<7}{assento:<7}{data_hora}")

        except Exception as e:
            print("Erro ao gerar relátorio:", e)
            
        