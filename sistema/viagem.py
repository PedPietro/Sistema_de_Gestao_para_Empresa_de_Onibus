import os
import pyodbc as bd
import getpass as gp

class ManutencaoDeViagem:

    def __init__(self, conexao):
        self._conexao = conexao

    '''def incluir(self):
        meuCursor = self.conexao.cursor() # cria um cursor, objeto de comandos de SQL
        numDepto = 1
        while numDepto != 0:
            # pedimos que o usuário digite os dados do novo departamento
            numDepto = int(input("Número do departamento (0 para terminar): "))
            
            if numDepto != 0: # usuário não quer terminar o cadastro
                nomeDepto = input("Nome do departamento: ")
                gerente_ssn = input("Cpf do gerente: ")
                dataInicial = input("Data de início do gerente (dd/mm/aaaa): ")
    
                # montamos string com o comando Insert contendo os dados digitados:
                sComando =  "insert into empresa.departamento " +\
                            " (numDepto, nomeDepto, gerente_NumSegSocial, gerente_dataInicial)"+\
                            "VALUES (?, ?, ?, Convert(date, ?, 103))"
                
                # fazemos o cursor enviar ao servidor, para análise e execução,
                # a string com o comando Insert acima
                try: 
                    meuCursor.execute(sComando,[numDepto, nomeDepto, gerente_ssn, dataInicial])
                    print("Departamento incluído com sucesso!")
                except: # em caso de erro
                    print("Não foi possível incluir. Pode haver departamento repetido.")
                
        # após digitar numDepto = 0, paramos o cadastramento
        # e enviamos os registros inseridos para serem definitivamente
        # gravados no servidor de banco de dados remoto
        meuCursor.commit() # solicita ao servidor que registre as mudanças no BD 
'''
''' def excluir_viagem(self):
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
                            ' FROM Viagem '+\
                            ' WHERE idViagem = ?', viagemEscolhida)
                registros = result.fetchall()
                if len(registros) == 0:     # se o departamento não existe, não podemos excluí-lo
                    print("Viagem não encontrado.")
                else:
                    print("Registro encontrado:")
                    idViagem            = registros[0][0]
                    distancia           = registros[0][1]
                    custo               = registros[0][2]
                    idCidadeOrigem      = registros[0][3]
                    idCidadeDestino     = registros[0][4]
                    print("ID Viagem: "+idViagem)
                    print("Distância: "+distancia)
                    print("Custo: "+custo)
                    print("Id Cidade Origem: "+idCidadeOrigem)
                    print("Id Cidade Destino: "+idCidadeDestino)
                    resposta = input("Deseja realmente excluir (s/n)?")
                    if resposta == "s":
                    # criamos uma string com o comando Delete para excluir o registro lido
                        sComando = " Delete from Viagem " +\
                        " where idViagem = ? " 
                        # fazemos o cursor enviar ao servidor o comando Delete acima criado
                        try: # tente executar o comando abaixo:
                            meuCursor.execute(sComando, viagemEscolhida)
                            print("Registro excluído.")
                        except: # em caso de erro
                            print("Não foi possível excluir. Pode ser uma viagem em uso por outra tabela.") 
        
        meuCursor.commit() # enviar as mudanças para o BD 
'''
def listar_viagem(self):
    meuCursor = self._conexao.cursor() # objeto de manipulação de dados
    # busca no BD os registros de departamentos
    #try: 
    result = meuCursor.execute(
                        ' SELECT idViagem, distancia, '+\
                        ' custo, idCidadeOrigem,'+\
                        ' idCidadeDestino'+\
                        ' FROM Viagem ')
    registros = result.fetchall()
    #except:
    #   print("Erro na busca dos dados\n")
    if len(registros) == 0:
        print("Viagens não encontradas")
    else:
        print("ID.   \tDistancia \tCusto   \tID Cidade Origem \tID Cidade Destino")
        for viagem in registros:
            print(f"{viagem[0]:<5} \t{viagem[1]:<10} \t{viagem[2]:<15} {viagem[3]:<20} {viagem[4]:<25}")
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
                        ' FROM Viagem '+\
                        ' WHERE idViagem = ?', viagemEscolhida)
            registros = result.fetchall()
            if len(registros) == 0:     # se o departamento não existe, não podemos excluí-lo
                print("Viagem não encontrado.")
            else:
                print("Registro encontrado:")
                idViagem            = registros[0][0]
                distancia           = registros[0][1]
                custo               = registros[0][2]
                idCidadeOrigem      = registros[0][3]
                idCidadeDestino     = registros[0][4]
                print("ID Viagem: "+idViagem)
                print("Distância: "+distancia)
                print("Custo: "+custo)
                print("Id Cidade Origem: "+idCidadeOrigem)
                print("Id Cidade Destino: "+idCidadeDestino)
    meuCursor.commit() # enviar as mudanças para o BD           