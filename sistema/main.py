#add funçao conecta bd aq no principal bbzudos
import os 
from passageiros import ManutencaoPassageiros
from passagens import ManutencaoPassagens
from viagem import ManutencaoDeViagem
from motorista import ManutencaoMotorista
from onibus import ManutencaoOnibus

import getpass as gp
import pyodbc as bd

def conectouAoBancoDeDados() -> bool: # informará se conseguiu ou não conectar
        global conexao
        os.system('cls') or None
        senha = "BD24147"
        try:
            conexao = bd.connect(driver="{SQL Server}",
                            server="regulus.cotuca.unicamp.br",
                            database="BD24147",
                            uid="BD24147", # seu username no servidor de BD
                            pwd=f"{senha}")
                           
            print("Conexão bem sucedida!")
            return True
        except:
            print("Não foi possível conectar ao banco de dados")
            return False

def seletorDeOpcoes():
    print("Em qual sistema vc deseja mexer?")
    print("1 - Cadastro de Passageiros")
    print("2 - Cadastro de Viagens")
    print("3 - Venda de Passagens")
    print("4 - Registro de inicio e de final de viagem, liberando passageiros e vagas")
    print("5 - Cadastro de Motoristas")
    print("6 - Busca de Ônibus")
    #opçoes para o balcão presencial(nn web)
    #preencher tabelas diretamente no SSMS usando insrt e nn por programação
    
    opcao = str(input("Escolha: "))
    match opcao:
        case "1": cadastroPassageiros()
        case "2": cadastroViagens()
        case "3": vendaPassagens()
        case "4": registroInicioeFinal()
        case "5": cadastroMotorista()
        case "6": buscaOnibus()
        
    opcao = input("Pressione Enter para finalizar...")
    print("Obrigado pelo uso!")
    
    
def cadastroPassageiros():
    #Manutenção passageiros, excluir, alterar, buscar e listar
    os.system('cls') or None
    print("Selecione uma opção:")
    print("0 - Voltar Ao Seletor")
    print("1 - Excluir Passageiros")
    print("2 - Alterar Passageiros")
    print("3 - Buscar Passageiros")
    print("4 - Listar Passageiros")
            
    escolha = str (input("Escolha: "))
    passageiros = ManutencaoPassageiros(conexao)
    match escolha:
        case "0": seletorDeOpcoes()
        case "1": passageiros.excluir()
        case "2": passageiros.alterar()
        case "3": passageiros.buscar()
        case "4": passageiros.listar()

    escolha = input("Pressione Enter para finalizar...")
    print("Obrigado pelo uso!")
        
        
def cadastroMotorista():
    #Manutenção passageiros, excluir, alterar, buscar e listar
    os.system('cls') or None
    print("Selecione uma opção:")
    print("0 - Voltar Ao Seletor")
    print("1 - Excluir Motorista")
    print("2 - Alterar Motorista")
    print("3 - Buscar Motorista")
    print("4 - Listar Motorista")
            
    escolha = str (input("Escolha: "))
    motorista = ManutencaoMotorista(conexao)
    match escolha:
        case "0": seletorDeOpcoes()
        case "1": motorista.excluir()
        case "2": motorista.alterar()
        case "3": motorista.buscar()
        case "4": motorista.listar()

    escolha = input("Pressione Enter para finalizar...")
    print("Obrigado pelo uso!")                
    
def buscaOnibus():
    #Manutenção passageiros, excluir, alterar, buscar e listar
    os.system('cls') or None
    print("Selecione uma opção:")
    print("0 - Voltar Ao Seletor")
    print("1 - Buscar Ônibus")
    print("2 - Listar Ônibus")
            
    escolha = str (input("Escolha: "))
    onibus = ManutencaoOnibus(conexao)
    match escolha:
        case "0": seletorDeOpcoes()
        case "1": onibus.buscar()
        case "2": onibus.listar()

    escolha = input("Pressione Enter para finalizar...")
    print("Obrigado pelo uso!")     

def cadastroViagens():
    #Manutenção viagem, excluir, alterar, buscar e listar
    os.system('cls') or None
    print("Selecione uma opção:")
    print("0 - Voltar Ao Seletor")
    print("1 - Excluir Viagem")
    print("2 - Alterar Viagem")
    print("3 - Buscar Viagem")
    print("4 - Listar Viagem")
            
    escolha = str (input("Escolha: "))
    viagem = ManutencaoDeViagem(conexao)
    match escolha:
        case "0": seletorDeOpcoes()
        case "1": viagem.excluir()
        case "2": viagem.alterar()
        case "3": viagem.buscar()
        case "4": viagem.listar()
        
    escolha = input("Pressione Enter para finalizar...")
    print("Obrigado pelo uso!")
    
def vendaPassagens():
    #Manutenção passagens, excluir, alterar, buscar e listar
    os.system('cls') or None
    print("Selecione uma opção:")
    print("0 - Voltar Ao Seletor")
    print("1 - Vender Passagens")
    print("2 - Cancelar Passageiros")
    print("3 - Buscar Passageiros")
    print("4 - Listar Passagens")
    print("5 - Verificar Disponibilidade")
            
    escolha = str (input("Escolha: "))
    passagens = ManutencaoPassagens(conexao)
    match escolha:
        case "0": seletorDeOpcoes()
        case "1": passagens.vendapassagens()
        case "2": passagens.cancelar()
        case "3": passagens.buscar()
        case "4": passagens.listar()
        case "5": passagens.disponibilidade()
    
def registroinicioefinal():
    #Registro de inicio e de final de viagem, liberando passageiros e vagas
    os.system('cls') or None
    print("Selecione uma opção:")
    print("0 - Voltar Ao Seletor")
    print("1 - Registro do Inicio da Viagem")
    print("2 - Registro do Final da Viagem")
    print("3 - Liberar Passageiros e Vagas")
            
    escolha = str (input("Escolha: "))
    viagem = ManutencaoDeViagem(conexao)
    match escolha:
        case "0": seletorDeOpcoes()
        case "1": viagem.Registroinicio()
        case "2": viagem.Registrofinal()
        case "3": viagem.Liberarpassageirosevagas()
                
    escolha = input("Pressione Enter para finalizar ou 0 para continuar...")
    print("Obrigado pelo uso!")
        
        
        
if __name__ == '__main__':
    conectouAoBancoDeDados()
    seletorDeOpcoes()