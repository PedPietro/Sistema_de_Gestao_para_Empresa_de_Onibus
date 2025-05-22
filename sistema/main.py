#add funçao conecta bd aq no principal bbzudos
from viagem import viagem
import os
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
        
    espera = input("Pressione Enter para finalizar...")
    print("Obrigado pelo uso!")
    
    
def cadastropassageiros():
    pass
    
def cadastroviagens():
    pass
    
def vendapassagens():
    pass
    
    
def registroinicioefinal():
    #Registro de inicio e de final de viagem, liberando passageiros e vagas
    os.system('cls') or None
    print("Selecione uma opção:")
    print("0 - Finalizar")
    print("1 - Registro do Inicio da Viagem")
    print("2 - Registro do Final da Viagem")
    print("3 - Liberar Passageiros e Vagas")
            
    escolha = str (input("Escolha: "))
    passageiros = viagem()
    match escolha:
        case "1": passageiros.Registroinicio()
        case "2": passageiros.Registrofinal()
        case "3": passageiros.Liberarpassageirosevagas()
                
    espera = input("Pressione Enter para finalizar...")
    print("Obrigado pelo uso!")
        
        
        
if __name__ == '__main__':
    seletorDeOpcoes()