class ManutencaoPassagens:
    def __init__(self, conexao):
        self._conexao = conexao
        self.passagens = []  # lista que armazena as passagens

    def vender_passagem(self):          
        meuCursor = self._conexao.cursor() # cria um cursor, objeto de comandos de SQL
        opcao = input("Deseja Vender uma passagem? (s/n): ")
        if opcao == 's':
            assento = input("Assento: ")
            idPassageiro = input("ID Passageiro: ")
            idViagem = input("ID Viagem: ")
            
            # Verifica se o assento está disponível
            assento_disponivel = False
            while not assento_disponivel:
                assento = input("Assento desejado: ")
                meuCursor.execute(
                    "SELECT COUNT(*) FROM Passagem WHERE assento = ? AND idViagem = ?",
                    (assento, idViagem)
                )
                resultado = meuCursor.fetchone()#fetch one pois retorna apenas uma linha
                if resultado[0] == 0:
                    assento_disponivel = True
                else:
                    print("Esse assento já está ocupado nessa viagem.")

            sComando =  "insert into Empresa.Passagem " +\
                        " (assento, idViagem, idPassageiro)"+\
                        "VALUES (?,Convert(date, ?, 103), ?, ?, ?)"
            
            try: 
                meuCursor.execute(sComando,(assento, idViagem, idPassageiro))
                print("Passagem vendida com sucesso!")
            except Exception as e: # em caso de erro
                print(f"Não foi possível vender a passagem. Erro:{e}.")
                
        meuCursor.commit() # solicita ao servidor que registre as mudanças no BD 

    def cancelar(self):
        meuCursor = self._conexao.cursor() # objeto de manipulação de dados (insert, update, delete, select)
        # cursor é o objeto que permite ao programa executar comandos SQL no servidor:
        passagemEscolhida = 1
        while passagemEscolhida!= 0:
        # pedimos que o usuário digite o número do departamento a ser excluído
            passagemEscolhida = int(input("ID da Passagem (0 para terminar): "))
            if passagemEscolhida != 0: # usuário não quer terminar o cadastro
                # verifica no BD se existe um departamento com esse número digitado
                result = meuCursor.execute(
                            ' SELECT idPassagem, assento,'+\
                            ' idViagem, idPassageiro'+\
                            ' FROM EmpresaOnibus.Passagem '+\
                            ' WHERE idPassagem = ?', passagemEscolhida)
                registros = result.fetchall()
                if len(registros) == 0:     # se o departamento não existe, não podemos excluí-lo
                    print("Passagem não encontrada.")
                else:
                    print("Registro encontrado:")
                    idPassagem            = registros[0][0]
                    assento            = registros[0][1]
                    idViagem           = registros[0][2]
                    idPassageiro      = registros[0][3]
                    print("ID da Passagem: " + str(idPassagem))
                    print("Assento: " + str(assento))
                    print("ID da Viagem: "+idViagem)
                    print("ID do Passageiro: "+idPassageiro)
                    
                    resposta = input("Deseja realmente cancelar (s/n)?")
                    if resposta == "s":
                    # criamos uma string com o comando Delete para excluir o registro lido
                        sComando = " Delete from EmpresaOnibus.Passagem " +\
                        " where idPassagem = ? " 
                        # fazemos o cursor enviar ao servidor o comando Delete acima criado
                        try: # tente executar o comando abaixo:
                            meuCursor.execute(sComando, passagemEscolhida)
                            print("Registro excluído.")
                        except Exception as e: # em caso de erro
                            print(f"Não foi possível cancelar. Pode ser uma passagem em uso por outra tabela. Erro: {e}") 

    def buscar(self):
        meuCursor = self._conexao.cursor() # objeto de manipulação de dados (insert, update, delete, select)
        # cursor é o objeto que permite ao programa executar comandos SQL no servidor:
        passagemEscolhida = 1
        while passagemEscolhida!= 0:
        # pedimos que o usuário digite o número do departamento a ser excluído
            passagemEscolhida = int(input("ID da Passagem (0 para terminar): "))
            if passagemEscolhida != 0: # usuário não quer terminar o cadastro
                # verifica no BD se existe um departamento com esse número digitado
                result = meuCursor.execute(
                             ' SELECT idPassagem, assento, '+\
                                ' idViagem, idPassageiro'+\
                                ' FROM EmpresaOnibus.Passagem'
                                ' Where idPassagem = ? ', passagemEscolhida)
                registros = result.fetchall()
                if len(registros) == 0:     # se o departamento não existe, não podemos excluí-lo
                    print("Passagem não encontrada.")
                else:
                    print("\nRegistro encontrado:")
                    print("Registro encontrado:")
                    idPassagem            = registros[0][0]
                    assento            = registros[0][1]
                    idViagem           = registros[0][2]
                    idPassageiro      = registros[0][3]
                    print("ID da Passagem: " + str(idPassagem))
                    print("Assento: " + str(assento))
                    print("ID da Viagem: "+idViagem)
                    print("ID do Passageiro: "+idPassageiro)       

    def listar(self):
        meuCursor = self._conexao.cursor() # objeto de manipulação de dados
        # busca no BD os registros de departamentos
        #try: 
        result = meuCursor.execute(
                             ' SELECT idPassagem, assento, '+\
                                ' idViagem, idPassageiro'+\
                                ' FROM EmpresaOnibus.Passagem'
        )
        registros = result.fetchall()
        #except:
        #   print("Erro na busca dos dados\n")
        if len(registros) == 0:
            print("Viagens não encontradas")
        else:
            print("ID.   \tAssento \tData e Hora   \tID Ônibus \tID Passageiro \tID Viagem")
            for passagem in registros:
                print(f"{(passagem[0]).ljust(3, ' ')} \t{(passagem[1]).ljust(6, ' ')} \t{(passagem[2]).ljust(26, ' ')} {(passagem[3].ljust(29, ' '))} {(passagem[4]).ljust(32, ' ')} {passagem[5]}")
            input("Tecle [enter] para terminar:")