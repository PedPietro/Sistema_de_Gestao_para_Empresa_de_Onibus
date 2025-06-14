class ManutencaoMotorista:
    def __init__(self, conexao):
        self._conexao = conexao
        self.motoristas = []  # lista que armazena os motoristas


    def cadastro_motorista(self):              # Salva os dados do formulário (incluídos ou editados) no banco de dados
        meuCursor = self._conexao.cursor() # cria um cursor, objeto de comandos de SQL
        opcao = input("Deseja Vender uma passagem? (s/n): ")
        if opcao == 's':
                nome = input("Nome: ")
     
                # montamos string com o comando Insert contendo os dados digitados:
                sComando =  "insert into EmpresaOnibus.Motorista " +\
                            " (nome)"+\
                            "VALUES (?)"
                
                # fazemos o cursor enviar ao servidor, para análise e execução,
                # a string com o comando Insert acima
                try: 
                    meuCursor.execute(sComando,(nome))
                    print("Passageiro incluído com sucesso!")
                except Exception as e: # em caso de erro
                    print(f"Não foi possível incluir. Erro: {e}.")


    def excluir(self):
        meuCursor = self._conexao.cursor() # objeto de manipulação de dados (insert, update, delete, select)
        # cursor é o objeto que permite ao programa executar comandos SQL no servidor:
        motoristaEscolhido = 1
        while motoristaEscolhido!= 0:
        # pedimos que o usuário digite o número do departamento a ser excluído
            motoristaEscolhido = int(input("ID do Motorista (0 para terminar): "))
            if motoristaEscolhido != 0: # usuário não quer terminar o cadastro
                # verifica no BD se existe um departamento com esse número digitado
                result = meuCursor.execute(
                            ' SELECT idMotorista, nome, '+\
                            ' WHERE idPassageiro = ?', motoristaEscolhido)
                registros = result.fetchall()
                if len(registros) == 0:     # se o departamento não existe, não podemos excluí-lo
                    print("Passageiro não encontrado.")
                else:
                    print("Registro encontrado:")
                    idMotorista            = registros[0][0]
                    nome           = registros[0][1]
                    print("ID Motorista: " + str(idMotorista))
                    print("nome: "+nome)
                    resposta = input("Deseja realmente excluir (s/n)?")
                    if resposta == "s":
                    # criamos uma string com o comando Delete para excluir o registro lido
                        sComando = " Delete from EmpresaOnibus.Motorista " +\
                        " where idMotorista = ? " 
                        # fazemos o cursor enviar ao servidor o comando Delete acima criado
                        try: # tente executar o comando abaixo:
                            meuCursor.execute(sComando, motoristaEscolhido)
                            print("Registro excluído.")
                        except Exception as e: # em caso de erro
                            print(f"Não foi possível excluir. Pode ser um passageiro em uso por outra tabela. Erro:{e}") 
        
        meuCursor.commit() # enviar as mudanças para o BD 

    def alterar(self):
        # cursor é o objeto que permite ao programa executar comandos SQL no servidor:
        meuCursor = self._conexao.cursor() # objeto de manipulação de dados
        motoristaEscolhido = 1
        while motoristaEscolhido != 0:
            # pedimos que o usuário digite o número do departamento a ser alterado
            motoristaEscolhido = int(input("ID do motorista (0 para terminar): "))
            
            if motoristaEscolhido!= 0: # usuário não quer terminar o cadastro
                # verifica no BD se existe um departamento com esse número digitado
                sComando = 'SELECT idMotorista, nome '+\
                ' FROM EmpresaOnibus.Motorista '+\
                ' WHERE idMotorista = ?'
                result = meuCursor.execute(sComando, motoristaEscolhido)                   
                registros = result.fetchall()
                if len(registros) == 0:
                    print("Motorista não encontrado.")
                else:
                    print("Registro encontrado:")
                    idMotorista     = registros[0][0]
                    nome            = registros[0][1]
                    print("ID Motorista: " + idMotorista    )
                    print("Nome: " + nome)

                    print("Digite os novos dados. [Enter] manterá os atuais:")
                    
                    idMotorista = int(input("ID do Motorista: "))
                    if idMotorista == "":             # usuário digitou [Enter]
                        idMotorista = registros[0][0] # nome original do BD

                    nome = str(input("Nome do Motorista: "))
                    if nome == "":               # usuário digitou [Enter]
                        nome = registros[0][1]   # gerente original do BD

                    # montamos string com o comando Update contendo os 
                    # dados digitados:

                    sComando =  " Update EmpresaOnibus.Motorista "+\
                                " SET idMotorista = ?, "+\
                                "     nome = ?, "+\
                                " where idMotorista = ? "
                    try:
                        meuCursor.execute(sComando,(idMotorista, nome, motoristaEscolhido))
                        meuCursor.commit() # registrar definitivamente as mudanças para o BD 
                        print("Motorista alterado com sucesso!")
                    except Exception as e: # em caso de erro
                        print(f"Não foi possível alterar. Verifique os dados.Erro {e}")


    def buscar(self):
        # cursor é o objeto que permite ao programa executar comandos SQL no servidor:
        meuCursor = self._conexao.cursor() # objeto de manipulação de dados
        motoristaEscolhido = 1
        while motoristaEscolhido != 0:
            # pedimos que o usuário digite o número do departamento a ser alterado
            motoristaEscolhido = int(input("ID do motorista (0 para terminar): "))
            
            if motoristaEscolhido!= 0: # usuário não quer terminar o cadastro
                # verifica no BD se existe um departamento com esse número digitado
                sComando = 'SELECT idMotorista, nome '+\
                ' FROM EmpresaOnibus.Motorista '+\
                ' WHERE idMotorista = ?'
                result = meuCursor.execute(sComando, motoristaEscolhido)                   
                registros = result.fetchall()
                if len(registros) == 0:
                    print("Motorista não encontrado.")
                else:
                    print("Registro encontrado:")
                    idMotorista     = registros[0][0]
                    nome            = registros[0][1]
                    print("ID Motorista: " + idMotorista    )
                    print("Nome: " + nome)


        meuCursor.commit()

    
    def listar(self):
        meuCursor = self._conexao.cursor() # objeto de manipulação de dados (insert, update, delete, select)
        # cursor é o objeto que permite ao programa executar comandos SQL no servidor:
        # pedimos que o usuário digite o número do departamento a ser excluído
                # verifica no BD se existe um departamento com esse número digitado
        result = meuCursor.execute(
                            ' SELECT idMotorista, nome '+\
                            ' FROM EmpresaOnibus.Motorista ')
        registros = result.fetchall()
        if len(registros) == 0:     # se o departamento não existe, não podemos excluí-lo
            print("Motoristas não encontrados.")
        else:
            print("ID. \tNome")
            for motorista in registros:
                print(f"{str(motorista[0]).ljust(3, ' ')}   \t{(motorista[1])}")
            input("Tecle [enter] para terminar:")

            
        meuCursor.commit()
        