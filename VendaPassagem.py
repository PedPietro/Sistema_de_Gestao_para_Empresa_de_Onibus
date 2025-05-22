import pyddbc
import os

class VendaPassagens:
    def __init__(self):
        self.cursor = conexao.cursor()
        
    def menu(self):
        while True:
            os.system("cls") or None
            print("===Menu vendas ")
            print("")
            print("")
            print("")
            opcao = input("")
            
            match opcao:
                case "1":self.vernder_passagem()
                case "1":self.listar_vendas()
                    
    def vender_passagem(self):
        try:
            id_viagem =  input("ID da viagem: ")
            consulta = """"
                SELECT vagasDisponiveis
                FROM Viagem
                WHERE idViagem = ? """"
            