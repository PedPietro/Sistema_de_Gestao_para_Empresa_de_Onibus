import os
import pyodbc as bd
import getpass as gp
from datetime import datetime

class ManutencaoDeViagem:

    def __init__(self, conexao):
        self._conexao = conexao

    def listar(self):
        meuCursor = self._conexao.cursor() # objeto de manipulação de dados
        # busca no BD os registros de departamentos
        #try: 
        result = meuCursor.execute(
                            ' SELECT idViagem, distancia, '+\
                            ' custo, idCidadeOrigem,'+\
                            ' idCidadeDestino'+\
                            ' FROM EmpresaOnibus.Viagem ')
        registros = result.fetchall()
        #except:
        #   print("Erro na busca dos dados\n")
        if len(registros) == 0:
            print("Viagens não encontradas")
        else:
            print("Id  Distancia Data Saída Custo      ID Cidade Origem  ID Cidade Destino ID Onibus ID Motorista")
            for viagem in registros:
                print(f"{str(viagem[0]).ljust(3, ' ')} {str(viagem[1]).ljust(10, ' ')} {str(viagem[2]).ljust(10, ' ')} {str(viagem[3]).ljust(17, ' ')} {str(viagem[4]).ljust(20, ' ')} {str(viagem[5]).ljust(23, ' ')} {str(viagem[6]).ljust(26, ' ')} {str(viagem[7])}")
                # passagem[2].strftime() serve para converter o datetime do bd em texto
            input("Tecle [enter] para terminar:")

    def buscar(self):
        meuCursor = self._conexao.cursor() # objeto de manipulação de dados (insert, update, delete, select)
        # cursor é o objeto que permite ao programa executar comandos SQL no servidor:
        viagemEscolhida = 1
        while viagemEscolhida!= 0:
        # pedimos que o usuário digite o número do departamento a ser excluído
            viagemEscolhida = int(input("ID Da Viagem (0 para terminar): "))
            if viagemEscolhida != 0: # usuário não quer terminar o cadastro
                # verifica no BD se existe um departamento com esse número digitado
                result = meuCursor.execute(
                            ' SELECT idViagem, distancia, '+\
                            ' custo, idCidadeOrigem,'+\
                            ' idCidadeDestino'+\
                            ' FROM EmpresaOnibus.Viagem '+\
                            ' WHERE idViagem = ?', viagemEscolhida)
                registros = result.fetchall()
                if len(registros) == 0:     # se o departamento não existe, não podemos excluí-lo
                    print("Viagem não encontrado.")
                else:
                    print("Registro encontrado:")
                    idViagem            = registros[0][0]
                    distancia           = registros[0][1]
                    dataSaida           = registros[0][2]
                    custo               = registros[0][3]
                    idCidadeOrigem      = registros[0][4]
                    idCidadeDestino     = registros[0][5]
                    idOnibus            = registros[0][5]
                    idMotorista         = registros[0][6]
                    print("ID Viagem: "+idViagem)
                    print("Distância: "+distancia)
                    print("Data da Saída: "+dataSaida)
                    print("Custo: "+custo)
                    print("Id Cidade Origem: "+idCidadeOrigem)
                    print("Id Cidade Destino: "+idCidadeDestino)
                    print("Id Ônibus: "+idOnibus)
                    print("Id Motorista: "+idMotorista)
        meuCursor.commit() # enviar as mudanças para o BD           
        
    def incluir(self):
        meuCursor = self._conexao.cursor() # cria um cursor, objeto de comandos de SQL
        opcao = input("Deseja Vender uma passagem? (s/n): ")
        if opcao == 's':
            distancia = input("Distância: ")
            dataSaida_str = input("Data Da Saída: ")
            dataSaida = datetime.strptime(dataSaida_str, "%Y/%m/%d").date()
            custo = input("Custo: ")
            idCidadeOrigem = input("ID Cidade Origem: ")
            idCidadeDestino = input("ID Cidade Destino: ")
            idOnibus = input("ID Ônibus: ")
            idMotorista = input("ID Motorista: ")
            sComando =  "insert into EmpresaOnibus.Viagem " +\
                        " (distancia, dataSaida, custo,"+\
                        " idCidadeOrigem, idCidadeDestino, idOnibus, idMotorista)"+\
                        "VALUES (?,Convert(date, ?, 103), ?, ?, ?)"
            
            try: 
                meuCursor.execute(sComando,(distancia, str(dataSaida), custo, idCidadeOrigem, idCidadeDestino, idOnibus, idMotorista))
                print("Viagem Incluída com sucesso!")
            except Exception as e: # em caso de erro
                print(f"Não foi possível incluir a viagem. Erro:{e}.")
                
        meuCursor.commit() # solicita ao servidor que registre as mudanças no BD 
                
        # após digitar numDepto = 0, paramos o cadastramento
        # e enviamos os registros inseridos para serem definitivamente
        # gravados no servidor de banco de dados remoto
        meuCursor.commit() # solicita ao servidor que registre as mudanças no BD 

    def excluir_viagem(self):
        meuCursor = self._conexao.cursor() # objeto de manipulação de dados (insert, update, delete, select)
        # cursor é o objeto que permite ao programa executar comandos SQL no servidor:
        viagemEscolhida = 1
        while viagemEscolhida!= 0:
        # pedimos que o usuário digite o número do departamento a ser excluído
            viagemEscolhida = int(input("ID Da Viagem (0 para terminar): "))
            if viagemEscolhida != 0: # usuário não quer terminar o cadastro
                # verifica no BD se existe um departamento com esse número digitado
                result = meuCursor.execute(
                            ' SELECT idViagem, distancia, '+\
                            ' custo, idCidadeOrigem,'+\
                            ' idCidadeDestino, idOnibus, idMotorista'+\
                            ' FROM EmpresaOnibus.Viagem '+\
                            ' WHERE idViagem = ?', viagemEscolhida)
                registros = result.fetchall()
                if len(registros) == 0:     # se o departamento não existe, não podemos excluí-lo
                    print("Viagem não encontrado.")
                else:
                    print("Registro encontrado:")
                    idViagem            = registros[0][0]
                    distancia           = registros[0][1]
                    dataSaida           = registros[0][2]
                    custo               = registros[0][3]
                    idCidadeOrigem      = registros[0][4]
                    idCidadeDestino     = registros[0][5]
                    idOnibus            = registros[0][5]
                    idMotorista         = registros[0][6]
                    print("ID Viagem: "+idViagem)
                    print("Distância: "+distancia)
                    print("Data da Saída: "+dataSaida)
                    print("Custo: "+custo)
                    print("Id Cidade Origem: "+idCidadeOrigem)
                    print("Id Cidade Destino: "+idCidadeDestino)
                    print("Id Ônibus: "+idOnibus)
                    print("Id Motorista: "+idMotorista)
                    resposta = input("Deseja realmente excluir (s/n)?")
                    if resposta == "s":
                    # criamos uma string com o comando Delete para excluir o registro lido
                        sComando = " Delete from Viagem " +\
                        " where idViagem = ? " 
                        # fazemos o cursor enviar ao servidor o comando Delete acima criado
                        try: # tente executar o comando abaixo:
                            meuCursor.execute(sComando, viagemEscolhida)
                            print("Registro excluído.")
                        except Exception as e: # em caso de erro
                            print(f"Não foi possível excluir. Pode ser uma viagem em uso por outra tabela.Erro: {e}") 
        
        meuCursor.commit() # enviar as mudanças para o BD 
