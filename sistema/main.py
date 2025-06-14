import os 
from passageiros import ManutencaoPassageiros
from passagens import ManutencaoPassagens
from relatorios import Relatorios
from viagem import ManutencaoDeViagem
from motorista import ManutencaoMotorista
from onibus import ManutencaoOnibus
from cidade import ManutencaoCidade
from UF import ManutencaoUF
#from relatorios import Relatorios

import pyodbc as bd

def conectouAoBancoDeDados() -> bool:
    global conexao
    os.system('cls') or None
    senha = "BD24147"
    try:
        conexao = bd.connect(driver="{SQL Server}",
                             server="regulus.cotuca.unicamp.br",
                             database="BD24147",
                             uid="BD24147",
                             pwd=f"{senha}")
        print("Conexão bem sucedida!")
        return True
    except:
        print("Não foi possível conectar ao banco de dados")
        return False

def seletorDeOpcoes():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Manutenção de Passageiros")
        print("2 - Manutenção de Viagens (Rota, Data, Ônibus, Preço e Vagas)")
        print("3 - Venda de Passagens (Visualizar Assentos Disponíveis)")
        print("4 - Manutenção de Motoristas")
        print("5 - Consulta de Ônibus")
        print("6 - Relatórios Gerenciais")
        print("7 - Manutenção de Cidades")
        print("8 - Manutenção de UF")
        print("0 - Sair")
        
        opcao = str(input("Escolha: "))
        match opcao:
            case "1": cadastroPassageiros()
            case "2": cadastroViagens()
            case "3": vendaPassagens()
            case "4": cadastroMotorista()
            case "5": buscaOnibus()
            case "6": manutencaoCidade()
            case "7": manutencaoUF()
            case "0": 
                print("Saindo... Obrigado pelo uso!")
                break
            case _: 
                print("Opção inválida. Tente novamente.")

def cadastroPassageiros():
    os.system('cls') or None
    print("Manutenção de Passageiros:")
    print("0 - Voltar")
    print("1 - Cadastro de Passageiros")
    print("2 - Excluir Passageiros")
    print("3 - Alterar Passageiros")
    print("4 - Buscar Passageiros")
    print("5 - Listar Passageiros")
    escolha = input("Escolha: ")
    passageiros = ManutencaoPassageiros(conexao)
    match escolha:
        case "0": return
        case "1": passageiros.incluir()
        case "2": passageiros.excluir()
        case "3": passageiros.alterar()
        case "4": passageiros.buscar()
        case "5": passageiros.listar()

def cadastroMotorista():
    os.system('cls') or None
    print("Manutenção de Motoristas:")
    print("0 - Voltar")
    print("1 - Excluir Motorista")
    print("2 - Alterar Motorista")
    print("3 - Buscar Motorista")
    print("4 - Listar Motorista")
    escolha = input("Escolha: ")
    motorista = ManutencaoMotorista(conexao)
    match escolha:
        case "0": return
        case "1": motorista.excluir()
        case "2": motorista.alterar()
        case "3": motorista.buscar()
        case "4": motorista.listar()

def buscaOnibus():
    os.system('cls') or None
    print("Consulta de Ônibus:")
    print("0 - Voltar")
    print("1 - Buscar Ônibus")
    print("2 - Listar Ônibus")
    escolha = input("Escolha: ")
    onibus = ManutencaoOnibus(conexao)
    match escolha:
        case "0": return
        case "1": onibus.buscar()
        case "2": onibus.listar()

def cadastroViagens():
    os.system('cls') or None
    print("Manutenção de Viagens:")
    print("0 - Voltar")
    print("1 - Incluir Viagem")
    print("2 - Excluir Viagem")
    print("3 - Buscar Viagem")
    print("4 - Listar Viagem")
    escolha = input("Escolha: ")
    viagem = ManutencaoDeViagem(conexao)
    match escolha:
        case "0": return
        case "1": viagem.incluir()
        case "2": viagem.excluir_viagem()
        case "3": viagem.buscar()
        case "4": viagem.listar()

def vendaPassagens():
    os.system('cls') or None
    print("Venda de Passagens:")
    print("0 - Voltar")
    print("1 - Vender Passagens")
    print("2 - Cancelar Passagem")
    print("3 - Buscar Passageiros")
    print("4 - Listar Passagens")
    print("5 - Verificar Assentos Disponíveis")
    escolha = input("Escolha: ")
    passagens = ManutencaoPassagens(conexao)
    match escolha:
        case "0": return
        case "1": passagens.vender_passagem()
        case "2": passagens.cancelar()
        case "3": passagens.buscar()
        case "4": passagens.listar()

def manutencaoUF():
    os.system('cls') or None
    print("Manutenção de Passageiros:")
    print("0 - Voltar")
    print("1 - Cadastro de UF")
    print("2 - Excluir UF")
    print("3 - Alterar UF")
    print("4 - Buscar UF")
    print("5 - Listar UF")
    escolha = input("Escolha: ")
    uf = ManutencaoUF(conexao)
    match escolha:
        case "0": return
        case "1": uf.incluir()
        case "2": uf.excluir()
        case "3": uf.alterar()
        case "4": uf.buscar()
        case "5": uf.listar()

def manutencaoCidade():
    os.system('cls') or None
    print("Manutenção de Passageiros:")
    print("0 - Voltar")
    print("1 - Cadastro de Cidades")
    print("2 - Excluir Cidades")
    print("3 - Alterar Cidades")
    print("4 - Buscar Cidades")
    print("5 - Listar Cidades")
    escolha = input("Escolha: ")
    cidades = ManutencaoCidade(conexao)
    match escolha:
        case "0": return
        case "1": cidades.incluir()
        case "2": cidades.excluir()
        case "3": cidades.alterar()
        case "4": cidades.buscar()
        case "5": cidades.listar()

if __name__ == '__main__':
    if conectouAoBancoDeDados():
        seletorDeOpcoes()
