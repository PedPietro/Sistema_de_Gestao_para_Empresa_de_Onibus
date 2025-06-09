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
            idPassageiro = int(input("Número do Passageiro (0 para terminar): "))
            
            if idPassageiro!= 0: # usuário não quer terminar o cadastro
                # verifica no BD se existe um departamento com esse número digitado
                sComando = 'SELECT idPassageiro, cpf, nome, '+\
                ' telefone, dataNascimento, email '+\
                ' FROM EmpresaOnibus.Passageiro '+\
                ' WHERE idPassageiro = ?'
                result = meuCursor.execute(sComando, idPassageiro)                   
                registros = result.fetchall()
                if len(registros) == 0:
                    print("Passageiro não encontrado.")
                else:
                    print("Registro encontrado:")
                    idPassageiro            = registros[0][0]
                    cpf           = registros[0][1]
                    nome               = registros[0][2]
                    telefone      = registros[0][3]
                    dataNascimento     = registros[0][4]
                    email     = registros[0][5]
                    print("ID Passageiro: " + str(idPassageiro))
                    print("CPF: "+cpf)
                    print("Nome: "+nome)
                    print("Telefone: "+telefone)
                    print("Data De Nascimento: "+dataNascimento)
                    print("Email: "+email)
                    print("Digite os novos dados. [Enter] manterá os atuais:")
                    idPassageiro = input("ID do Passageiro: ")
                    cpf = input("Cpf do Passageiro: ")
                    nome = input("Nome do Passageiro: ")
                    telefone = input("Telefone do Passageiro: ")
                    dataNascimento = input("Data de Nascimento do Passageiro(dd/mm/yyyy): ")
                    email = input("Email do Passageiro: ")
                    
                    # montamos string com o comando Update contendo os 
                    # dados digitados:
                    
                    if nomeDepto == "":             # usuário digitou [Enter]
                        nomeDepto = registros[0][0] # nome original do BD
                        
                    if gerente == "":               # usuário digitou [Enter]
                        gerente = registros[0][1]   # gerente original do BD
                        
                    if data == "":                  # usuário digitou [Enter]
                        data = registros[0][2]      # data original do BD
                        
                    sComando =  " Update EmpresaOnibus.Passageiro "+\
                                " SET idPassageiro = ?, "+\
                                "     cpf = ?, "+\
                                "     nome = ?, "+\
                                "     telefone = ?, "+\
                                "     dataNascimento = Convert(date, ?, 103) "+\
                                "     email = ?, "+\
                                " where idPassageiro = ? "
                    try:
                        meuCursor.execute(sComando,[idPassageiro, cpf, nome, telefone, dataNascimento, email])
                        print("Departamento alterado com sucesso!")
                    except: # em caso de erro
                        print("Não foi possível alterar. Verifique os dados.")
        
        meuCursor.commit() # registrar definitivamente as mudanças para o BD 

    def excluir(self):
        meuCursor = self.conexao.cursor() # objeto de manipulação de dados (insert, update, delete, select)
        # cursor é o objeto que permite ao programa executar comandos SQL no servidor:
        passageiroEscolhido = 1
        while passageiroEscolhido!= 0:
        # pedimos que o usuário digite o número do departamento a ser excluído
            passageiroEscolhido = int(input("ID do Passageiro (0 para terminar): "))
            if passageiroEscolhido != 0: # usuário não quer terminar o cadastro
                # verifica no BD se existe um departamento com esse número digitado
                result = meuCursor.execute(
                            ' SELECT idPassageiro, cpf, '+\
                            ' nome, telefone,'+\
                            ' dataNascimento, email'+\
                            ' FROM EmpresaOnibus.Passageiro '+\
                            ' WHERE idPassageiro = ?', passageiroEscolhido)
                registros = result.fetchall()
                if len(registros) == 0:     # se o departamento não existe, não podemos excluí-lo
                    print("Passageiro não encontrado.")
                else:
                    print("Registro encontrado:")
                    idPassageiro            = registros[0][0]
                    cpf           = registros[0][1]
                    nome               = registros[0][2]
                    telefone      = registros[0][3]
                    dataNascimento     = registros[0][4]
                    email     = registros[0][5]
                    print("ID Passageiro: " + str(idPassageiro))
                    print("CPF: "+cpf)
                    print("Nome: "+nome)
                    print("Telefone: "+telefone)
                    print("Data De Nascimento: "+dataNascimento)
                    print("Email: "+email)
                    resposta = input("Deseja realmente excluir (s/n)?")
                    if resposta == "s":
                    # criamos uma string com o comando Delete para excluir o registro lido
                        sComando = " Delete from EmpresaOnibus.Passageiro " +\
                        " where idPassageiro = ? " 
                        # fazemos o cursor enviar ao servidor o comando Delete acima criado
                        try: # tente executar o comando abaixo:
                            meuCursor.execute(sComando, passageiroEscolhido)
                            print("Registro excluído.")
                        except: # em caso de erro
                            print("Não foi possível excluir. Pode ser um passageiro em uso por outra tabela.") 
        
        meuCursor.commit() # enviar as mudanças para o BD 
#precisava de um commit kkkkkkk
    def buscar(self):
        meuCursor = self.conexao.cursor() # objeto de manipulação de dados (insert, update, delete, select)
        # cursor é o objeto que permite ao programa executar comandos SQL no servidor:
        passageiroEscolhido = 1
        while passageiroEscolhido!= 0:
        # pedimos que o usuário digite o número do departamento a ser excluído
            passageiroEscolhido = int(input("ID do Passageiro (0 para terminar): "))
            if passageiroEscolhido != 0: # usuário não quer terminar o cadastro
                # verifica no BD se existe um departamento com esse número digitado
                result = meuCursor.execute(
                            ' SELECT idPassageiro, cpf, '+\
                            ' nome, telefone,'+\
                            ' dataNascimento, email'+\
                            ' FROM EmpresaOnibus.Passageiro '+\
                            ' WHERE idPassageiro = ?', passageiroEscolhido)
                registros = result.fetchall()
                if len(registros) == 0:     # se o departamento não existe, não podemos excluí-lo
                    print("Passageiro não encontrado.")
                else:
                    print("Registro encontrado:")
                    idPassageiro            = registros[0][0]
                    cpf           = registros[0][1]
                    nome               = registros[0][2]
                    telefone      = registros[0][3]
                    dataNascimento     = registros[0][4]
                    email     = registros[0][5]
                    print("ID Passageiro: " + str(idPassageiro))
                    print("CPF: "+cpf)
                    print("Nome: "+nome)
                    print("Telefone: "+telefone)
                    print("Data De Nascimento: "+dataNascimento)
                    print("Email: "+email)

        meuCursor.commit()
                    
    def listar(self):
        meuCursor = self.conexao.cursor() # objeto de manipulação de dados (insert, update, delete, select)
        # cursor é o objeto que permite ao programa executar comandos SQL no servidor:
        # pedimos que o usuário digite o número do departamento a ser excluído
                # verifica no BD se existe um departamento com esse número digitado
        result = meuCursor.execute(
                            ' SELECT idPassageiro, cpf, '+\
                            ' nome, telefone,'+\
                            ' dataNascimento, email'+\
                            ' FROM EmpresaOnibus.Passageiro ')
        registros = result.fetchall()
        if len(registros) == 0:     # se o departamento não existe, não podemos excluí-lo
            print("Passageiros não encontrados.")
        else:
            print("\tID. \tCpf              \tNome                 \tTelefone       \tData De Nascimento     \tEmail")
            for passageiro in registros:
                print(f"\t{passageiro[0]}   \t{passageiro[1]}        \t{passageiro[2]}     \t{passageiro[3]}   \t{passageiro[4]};           \t{passageiro[5]};\n")
            input("Tecle [enter] para terminar:")
            '''while passageiro < len(registros):
                print("Registros encontrados: \n")
                idPassageiro            = registros[0][0]
                cpf           = registros[0][1]
                nome               = registros[0][2]
                telefone      = registros[0][3]
                dataNascimento     = registros[0][4]
                email     = registros[0][5]
                print("ID Passageiro: " + str(idPassageiro))
                print("CPF: "+cpf)
                print("Nome: "+nome)
                print("Telefone: "+telefone)
                print("Data De Nascimento: "+dataNascimento)
                print("Email: "+email+"\n")
                passageiro =+1'''

        meuCursor.commit()
       
        