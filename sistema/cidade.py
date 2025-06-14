class ManutencaoCidade:
    def __init__(self, conexao):
        self._conexao = conexao
        self.cidades = []  # lista que armazena as cidades

    def incluir(self):          # Salva os dados do formulário (incluídos ou editados) no banco de dados
        meuCursor = self._conexao.cursor() # cria um cursor, objeto de comandos de SQL
        opcao = input("Deseja Incluir Uma Cidade?(s/n)")
        if opcao == "s":
                nome = input("Nome: ")
                endereco_terminal = input("Endereço do Terminal: ")
                idUF = input("ID da UF: ")
     
                # montamos string com o comando Insert contendo os dados digitados:
                sComando =  "insert into EmpresaOnibus.Cidade " +\
                            " (nome, endereco_terminal, idUF)"+\
                            "VALUES (?, ?, ?)"
                
                # fazemos o cursor enviar ao servidor, para análise e execução,
                # a string com o comando Insert acima
                try: 
                    meuCursor.execute(sComando,(nome, endereco_terminal, idUF))
                    print("Cidade incluída com sucesso!")
                except Exception as e: # em caso de erro
                    print(f"Não foi possível incluir. Erro: {e}.")
        else:
            input("Tecle [Enter] para sair")     

    def excluir(self):
        meuCursor = self._conexao.cursor() # objeto de manipulação de dados (insert, update, delete, select)
        # cursor é o objeto que permite ao programa executar comandos SQL no servidor:
        cidadeEscohlida = 1
        while cidadeEscohlida!= 0:
        # pedimos que o usuário digite o número do departamento a ser excluído
            cidadeEscohlida = int(input("ID da Cidade (0 para terminar): "))
            if cidadeEscohlida != 0: # usuário não quer terminar o cadastro
                # verifica no BD se existe um departamento com esse número digitado
                result = meuCursor.execute(
                            ' SELECT idCidade, nome, '+\
                            ' endereco_terminal, idUF,'+\
                            ' FROM EmpresaOnibus.Passageiro '+\
                            ' WHERE idCidade = ?', cidadeEscohlida)
                registros = result.fetchall()
                if len(registros) == 0:     # se o departamento não existe, não podemos excluí-lo
                    print("Cidade não encontrada.")
                else:
                    print("Registro encontrado:")
                    idCidade            = registros[0][0]
                    nome           = registros[0][1]
                    endereco_terminal               = registros[0][2]
                    idUF      = registros[0][3]
                    print("ID Cidade: " + str(idCidade))
                    print("Nome: "+nome)
                    print("Endereço Terminal: "+nome)
                    print("ID UF: "+idUF)
                    
                    resposta = input("Deseja realmente excluir (s/n)?")
                    if resposta == "s":
                    # criamos uma string com o comando Delete para excluir o registro lido
                        sComando = " Delete from EmpresaOnibus.Cidade " +\
                        " where idCidade = ? " 
                        # fazemos o cursor enviar ao servidor o comando Delete acima criado
                        try: # tente executar o comando abaixo:
                            meuCursor.execute(sComando, cidadeEscohlida)
                            print("Registro excluído.")
                        except Exception as e: # em caso de erro
                            print(f"Não foi possível excluir. Pode ser uma Cidade em uso por outra tabela. Erro:{e}") 
        
        meuCursor.commit() # enviar as mudanças para o BD

    def alterar(self):
        # cursor é o objeto que permite ao programa executar comandos SQL no servidor:
        meuCursor = self._conexao.cursor() # objeto de manipulação de dados
        cidadeEscolhida = 1
        while cidadeEscolhida != 0:
            # pedimos que o usuário digite o número da Cidade a ser alterado
            cidadeEscolhida = int(input("ID da Cidade (0 para terminar): "))
            
            if cidadeEscolhida!= 0: # usuário não quer terminar o cadastro
                # verifica no BD se existe uma Cidade com esse número digitado
                sComando = 'SELECT idCidade, nome,'+\
                ' endereco_terminal, idUF'+\
                ' FROM EmpresaOnibus.Cidade '+\
                ' WHERE idCidade = ?'
                result = meuCursor.execute(sComando, cidadeEscolhida)                   
                registros = result.fetchall()
                if len(registros) == 0:
                    print("Cidade não encontrada.")
                else:
                    print("Registro encontrado:")
                    idCidade           = registros[0][0]
                    nome                     = registros[0][1]
                    endereco_terminal                    = registros[0][2]
                    idUF                = registros[0][3]

                    print("Digite os novos dados. [Enter] manterá os atuais:")
                    
                    idCidade = int(input("ID da Cidade: "))
                    if idCidade == "":             # usuário digitou [Enter]
                        idCidade = registros[0][0] # nome original do BD

                    nome = str(input("Nome da Cidade: "))
                    if nome == "":               # usuário digitou [Enter]
                        nome = registros[0][1]   # gerente original do BD

                    endereco_terminal = str(input("Endereço Terminal: "))
                    if endereco_terminal == "":                  # usuário digitou [Enter]
                        endereco_terminal = registros[0][2]      # data original do BD


                    idUF = str(input("ID UF: "))
                    if idUF == "":                  # usuário digitou [Enter]
                        idUF = registros[0][3]      # data original do BD

                    # montamos string com o comando Update contendo os 
                    # dados digitados:

                    sComando =  " Update EmpresaOnibus.Passageiro "+\
                                " SET idCidade = ?, "+\
                                "     nome = ?, "+\
                                "     endereco_terminal = ?, "+\
                                "     idUF = ?, "+\
                                " where idCidade = ? "
                    try:
                        meuCursor.execute(sComando,(idCidade, nome, endereco_terminal, idUF, cidadeEscolhida))
                        meuCursor.commit() # registrar definitivamente as mudanças para o BD 
                        print("Cidade alterada com sucesso!")
                    except Exception as e: # em caso de erro
                        print(f"Não foi possível alterar. Verifique os dados.Erro {e}")

    def buscar(self):
        meuCursor = self._conexao.cursor() # objeto de manipulação de dados (insert, update, delete, select)
        # cursor é o objeto que permite ao programa executar comandos SQL no servidor:
        cidadeEscolhida = 1
        while cidadeEscolhida!= 0:
        # pedimos que o usuário digite o número a ser excluído
            cidadeEscolhida = int(input("ID da Cidade (0 para terminar): "))
            if cidadeEscolhida != 0: # usuário não quer terminar o cadastro
                # verifica no BD se existe uma cidade com esse número digitado
                result = meuCursor.execute(
                            ' SELECT idCidade, nome, '+\
                            ' endereco_terminal, idUF'+\
                            ' FROM EmpresaOnibus.Cidade '+\
                            ' WHERE idCidade = ?', cidadeEscolhida)
                registros = result.fetchall()
                if len(registros) == 0:     # se o não existe, não podemos busca-lá
                    print("Cidade não encontrada.")
                else:
                    print("\nRegistro encontrado:")
                    idCidade            = registros[0][0]
                    nome           = registros[0][1]
                    endereco_terminal               = registros[0][2]
                    idUF      = registros[0][3]
                    print("\nID Cidade: " + str(idCidade))
                    print(f"Nome: {nome}")
                    print(f"Endereço Terminal: {endereco_terminal}")
                    print(f"ID UF: {idUF}")

        meuCursor.commit()

    def listar(self):
        meuCursor = self._conexao.cursor()
        result = meuCursor.execute(
                            ' SELECT idCidade, nome, '+\
                            ' endereco_terminal, idUF'+\
                            ' FROM EmpresaOnibus.Cidade ')
        registros = result.fetchall()
        if len(registros) == 0:
            print("Cidades não encontradas.")
        else:
            print("ID. \tNome              \tEndereço Terminal                 \tID UF")
            for cidade in registros:
                print(f"{(cidade[0]).ljust(3, ' ')}   \t{(cidade[1]).ljust(19, ' ')}        \t{(cidade[2]).ljust(40, ' ')}     \t{cidade[3].ljust(58, ' ')}   \t{cidade[4].ljust(69, ' ')}           \t{cidade[5]}")          

            input("Tecle [enter] para terminar:")
        meuCursor.commit()
