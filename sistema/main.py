#add funçao conecta bd aq no principal bbzudos
import os 
from passageiros import ManutencaoPassageiros
from passagens import ManutencaoPassagens
from viagem import ManutencaoDeViagem
import getpass as gp
import pyodbc as bd

def conectouAoBancoDeDados() -> bool: # informará se conseguiu ou não conectar
        global conexao
        os.system('cls') or None
        senha = gp.getpass("Digite a senha do seu banco de dados: ") # pede a senha
        try:
            conexao = bd.connect(driver="{SQL Server}",
                            server="regulus.cotuca.unicamp.br",
                            database="BD24147",
                            uid="BD24147", # seu username no servidor de BD
                            pwd=f"{senha}") # substitui variável senha
                            # pela senha digitada
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
    #opçoes para o balcão presencial(nn web)
    #preencher tabelas diretamente no SSMS usando insrt e nn por programação
    
    opcao = str(input("Escolha: "))
    match opcao:
        case "1": cadastropassageiros()
        case "2": cadastroviagens()
        case "3": vendapassagens()
        case "4": registroinicioefinal()
        
    opcao = input("Pressione Enter para finalizar...")
    print("Obrigado pelo uso!")
    
    
def cadastropassageiros():
    #Manutenção passageiros, excluir, alterar, buscar e listar
    os.system('cls') or None
    print("Selecione uma opção:")
    print("0 - Finalizar")
    print("1 - Excluir Passageiros")
    print("2 - Alterar Passageiros")
    print("3 - Buscar Passageiros")
    print("4 - Listar Passageiros")
            
    escolha = str (input("Escolha: "))
    passageiros = ManutencaoPassageiros(conexao)
    match escolha:
        case "1": passageiros.excluir()
        case "2": passageiros.alterar()
        case "3": passageiros.buscar()
        case "4": passageiros.listar()

    escolha = input("Pressione Enter para finalizar...")
    print("Obrigado pelo uso!")
        
        
                
    
def cadastroviagens():
    #Manutenção viagem, excluir, alterar, buscar e listar
    os.system('cls') or None
    print("Selecione uma opção:")
    print("0 - Finalizar")
    print("1 - Excluir Viagem")
    print("2 - Alterar Viagem")
    print("3 - Buscar Viagem")
    print("4 - Listar Viagem")
            
    escolha = str (input("Escolha: "))
    viagem = ManutencaoDeViagem(conexao)
    match escolha:
        case "1": viagem.excluir()
        case "2": viagem.alterar()
        case "3": viagem.buscar()
        case "4": viagem.listar()
        
    escolha = input("Pressione Enter para finalizar...")
    print("Obrigado pelo uso!")
        
    
def vendapassagens():
    #Manutenção passagens, excluir, alterar, buscar e listar
    os.system('cls') or None
    print("Selecione uma opção:")
    print("0 - Finalizar")
    print("1 - Vender Passagens")
    print("2 - Cancelar Passageiros")
    print("3 - Buscar Passageiros")
    print("4 - Listar Passagens")
    print("5 - Verificar Disponibilidade")
            
    escolha = str (input("Escolha: "))
    passagens = ManutencaoPassagens(conexao)
    match escolha:
        case "1": passagens.vendapassagens()
        case "2": passagens.cancelar()
        case "3": passagens.buscar()
        case "4": passagens.listar()
        case "5": passagens.disponibilidade()
        
    
def registroinicioefinal():
    #Registro de inicio e de final de viagem, liberando passageiros e vagas
    os.system('cls') or None
    print("Selecione uma opção:")
    print("0 - Finalizar")
    print("1 - Registro do Inicio da Viagem")
    print("2 - Registro do Final da Viagem")
    print("3 - Liberar Passageiros e Vagas")
            
    escolha = str (input("Escolha: "))
    viagem = ManutencaoDeViagem(conexao)
    match escolha:
        case "1": viagem.Registroinicio()
        case "2": viagem.Registrofinal()
        case "3": viagem.Liberarpassageirosevagas()
                
    escolha = input("Pressione Enter para finalizar...")
    print("Obrigado pelo uso!")
        
        
        
if __name__ == '__main__':
    conectouAoBancoDeDados()
    seletorDeOpcoes()