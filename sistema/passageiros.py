import os
import pyodbc as bd
import getpass as gp

class ManutencaoPassageiros:
    def __init__(self, conexao):
        self.conexao = conexao
        self.passageiros = [] # vetor que guarda os passageiros



    '''def cadastropassageiros():              # Salva os dados do formulário (incluídos ou editados) no banco de dados
        meuCursor = conexao.cursor() # cria um cursor, objeto de comandos de SQL
        cpf = 1
        while cpf != 0:
            # pedimos que o usuário digite os dados do novo Passageiro
            cpf = int(input("CPF do Passageiro (0 para terminar): "))
            
            if cpf != 0: # usuário não quer terminar o cadastro
                nome = input("Nome do Passageiro: ")
                telefone = input("Cpf do Passageiro: ")
                email = input("Email do Passageiro: ")
     
                # montamos string com o comando Insert contendo os dados digitados:
                sComando =  "insert into Passageiro " +\
                            " (cpf, nome, telefone, email)"+\
                            "VALUES ("+cpf+", "+nome+", "+telefone+", "+email+")"
                
                # fazemos o cursor enviar ao servidor, para análise e execução,
                # a string com o comando Insert acima
                try: 
                    meuCursor.execute(sComando)
                    print("Passageiro incluído com sucesso!")
                except: # em caso de erro
                    print("Não foi possível incluir. Pode haver Passageiro repetido.")'''
    def alterar(self):
        # cursor é o objeto que permite ao programa executar comandos SQL no servidor:
        meuCursor = self.conexao.cursor() # objeto de manipulação de dados
        idPassageiro = 1
        while idPassageiro != 0:
            # pedimos que o usuário digite o número do departamento a ser alterado
            idPassageiro = int(input("Número do Passagigeiro (0 para terminar): "))
            
            if idPassageiro!= 0: # usuário não quer terminar o cadastro
                # verifica no BD se existe um departamento com esse número digitado
                sComando = 'SELECT idPassageiro, cpf, nome, '+\
                ' telefone, dataNascimento, email '+\
                ' FROM Passageiro '+\
                ' WHERE idPassageiro = ?'
                result = meuCursor.execute(sComando, idPassageiro)                   
                registros = result.fetchall()
                if len(registros) == 0:
                    print("Departamento não encontrado.")
                else:
                    print("Registro encontrado:")
                    nomeDepto = registros[0][3]     # 1o campo do 1o registro
                    gerente   = registros[0][0]     # 2o campo do 1o registro
                    data      = registros[0][5]     # 3o campo do 1o registro      
                    print("Nome do Passageiro: "+nomeDepto)
                    print("Gerente:"+gerente)
                    print("Data inicial:"+data)
                    print("Digite os novos dados. [Enter] manterá os atuais:")
                    nomeDepto = input("Nome do departamento: ")
                    gerente = input("Cpf do gerente: ")
                    data = input("Data de início do gerente (dd/mm/aaaa): ")
                    
                    # montamos string com o comando Update contendo os 
                    # dados digitados:
                    
                    if nomeDepto == "":             # usuário digitou [Enter]
                        nomeDepto = registros[0][0] # nome original do BD
                        
                    if gerente == "":               # usuário digitou [Enter]
                        gerente = registros[0][1]   # gerente original do BD
                        
                    if data == "":                  # usuário digitou [Enter]
                        data = registros[0][2]      # data original do BD
                        
                    sComando =  " Update empresa.departamento "+\
                                " SET nomeDepto = ?, "+\
                                "     gerente_NumSegSocial = ?, "+\
                                "     gerente_dataInicial = Convert(date, ?, 103) "+\
                                " where numDepto = ? "
                    try:
                        meuCursor.execute(sComando,[nomeDepto, gerente, data, idPassageiro])
                        print("Departamento alterado com sucesso!")
                    except: # em caso de erro
                        print("Não foi possível alterar. Verifique os dados.")
        
        meuCursor.commit() # registrar definitivamente as mudanças para o BD 

    def excluir(self):
        meuCursor = self.conexao.cursor() # objeto de manipulação de dados (insert, update, delete, select)
        # cursor é o objeto que permite ao programa executar comandos SQL no servidor:
        viagemEscolhida = 1
        while viagemEscolhida!= 0:
        # pedimos que o usuário digite o número do departamento a ser excluído
            viagemEscolhida = int(input("Número Da Viagem (0 para terminar): "))
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
#precisava de um commit kkkkkkk
    def buscar(self):
        print("Buscar passageiro:")
        id_passageiro = input("Digite o ID do passageiro a buscar: ")
        encontrou = False
        for p in self.passageiros:
            if p["id"] == id_passageiro:
                print("ID:", p["id"])
                print("Nome:", p["nome"])
                print("CPF:", p["cpf"])
                encontrou = True
                break
        if not encontrou:
            print("Passageiro não encontrado.\n")

    '''def listar(self):
        print("Lista de passageiros:")
        if len(self.passageiros) == 0:
            print("Nenhum passageiro cadastrado.\n")
        else:
            for p in self.passageiros:
                print("ID:", p["id"])
                print("Nome:", p["nome"])
                print("CPF:", p["cpf"])
                print()'''

    def listar(self):
        meuCursor = self._conexao.cursor()  # objeto de manipulação de dados
        try:  
            result = meuCursor.execute(
                'SELECT assento, data_e_hora, idOnibus, idPassageiro,' +
                ' idViagem ' +
                ' FROM EmpresaOnibus.Passagem ')    
            registros = result.fetchall() #fetchall serve para pegar todos os dados de um select
            return registros
        except:
            print("Erro na busca dos dados\n")
            return
        '''
        print("Num. Nome       Gerente    Data Inicial")
        for depto in registros:
            print(f"{depto[0]}   {depto[1]}    {depto[2]}    {depto[3]}")
        input("Tecle [enter] para terminar:")'''