class ManutencaoPassagens:
    def __init__(self, conexao):
        self._conexao = conexao
        self.passagens = []  # lista que armazena as passagens

    def vender_passagem(self):          # Salva os dados do formulário (incluídos ou editados) no banco de dados
        meuCursor = self._conexao.cursor() # cria um cursor, objeto de comandos de SQL
        idPassagem = 1
        while idPassagem != 0:
            # pedimos que o usuário digite os dados do novo Passageiro
            idPassagem = int(input("ID da Passagem (0 para terminar): "))
            
            if idPassagem != 0: # usuário não quer terminar o cadastro
                assento = input("Assento: ")
                data_e_hora = input("Data e Hora(yyyy-mm-ddThh:hh:hh): ")
                idOnibus = input("Email do Passageiro: ")
                idPassageiro = input("ID Passagem: ")
                idViagem = input("ID Viagem: ")
     
                # montamos string com o comando Insert contendo os dados digitados:
                sComando =  "insert into Passagem " +\
                            " (assento, data_e_hora, idOnibus, idPassageiro, idViagem)"+\
                            "VALUES (?,Convert(date, ?, 103), ?, ?, ?)"
                
                # fazemos o cursor enviar ao servidor, para análise e execução,
                # a string com o comando Insert acima
                try: 
                    meuCursor.execute(sComando[assento, data_e_hora, idOnibus, idPassageiro, idViagem])
                    print("Passagem incluída com sucesso!")
                except: # em caso de erro
                    print("Não foi possível incluir. Pode haver ID repetido.")
                
        # após digitar numDepto = 0, paramos o cadastramento
        # e enviamos os registros inseridos para serem definitivamente
        # gravados no servidor de banco de dados remoto
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
                            ' SELECT idPassagem, assento, data_e_hora, '+\
                            ' idOnibus, idPassageiro,'+\
                            ' idViagem'+\
                            ' FROM EmpresaOnibus.Passagem '+\
                            ' WHERE idPassagem = ?', passagemEscolhida)
                registros = result.fetchall()
                if len(registros) == 0:     # se o departamento não existe, não podemos excluí-lo
                    print("Passagem não encontrada.")
                else:
                    print("Registro encontrado:")
                    idPassagem            = registros[0][0]
                    assento            = registros[0][0]
                    data_e_hora           = registros[0][1]
                    idOnibus               = registros[0][2]
                    idPassageiro      = registros[0][3]
                    idViagem     = registros[0][4]
                    print("ID da Passagem: " + str(idPassagem))
                    print("Assento: " + str(assento))
                    print("Data e hora: "+data_e_hora)
                    print("ID do Ônibus: "+idOnibus)
                    print("ID do Passageiro: "+idPassageiro)
                    print("Viagem: "+idViagem)
                    resposta = input("Deseja realmente cancelar (s/n)?")
                    if resposta == "s":
                    # criamos uma string com o comando Delete para excluir o registro lido
                        sComando = " Delete from EmpresaOnibus.Passagem " +\
                        " where idPassagem = ? " 
                        # fazemos o cursor enviar ao servidor o comando Delete acima criado
                        try: # tente executar o comando abaixo:
                            meuCursor.execute(sComando, passagemEscolhida)
                            print("Registro excluído.")
                        except: # em caso de erro
                            print("Não foi possível excluir. Pode ser uma passagem em uso por outra tabela.") 

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
                                ' data_e_hora, idOnibus, idPassageiro, idViagem'+\
                                ' FROM EmpresaOnibus.Passagem'
                                ' Where idPassagem = ? ', passagemEscolhida)
                registros = result.fetchall()
                if len(registros) == 0:     # se o departamento não existe, não podemos excluí-lo
                    print("Passagem não encontrada.")
                else:
                    print("\nRegistro encontrado:")
                    idPassagem            = registros[0][0]
                    assento           = registros[0][1]
                    data_e_hora               = registros[0][2]
                    idOnibus      = registros[0][3]
                    idPassageiro     = registros[0][4]
                    idViagem     = registros[0][5]
                    print(f"\nID Passagem: {idPassagem}" )
                    print(f"Assento: {assento}")
                    print(f"Data e Hora: {data_e_hora}")
                    print(f"ID Ônibus: {idOnibus}")
                    print(f"ID Passageiro: {idPassageiro}\n")           
                    print(f"ID Viagem: {idViagem}\n")          

    def listar(self):
        meuCursor = self._conexao.cursor() # objeto de manipulação de dados
        # busca no BD os registros de departamentos
        #try: 
        result = meuCursor.execute(
                                ' SELECT idPassagem, assento, '+\
                                ' data_e_hora, idOnibus, idPassageiro, idViagem'+\
                                ' FROM EmpresaOnibus.Passagem')
        registros = result.fetchall()
        #except:
        #   print("Erro na busca dos dados\n")
        if len(registros) == 0:
            print("Viagens não encontradas")
        else:
            print("ID.   \tAssento \tData e Hora   \tID Ônibus \tID Passageiro \tID Viagem")
            for passagem in registros:
                print(f"{passagem[0]:<5} \t{passagem[1]:<10} \t{passagem[2]:<15} {passagem[3]:<20} {passagem[4]:<25} {passagem[5]:<30}")
            input("Tecle [enter] para terminar:")

    

    def disponibilidade(self):
        pass

'''     
    def vendapassagens(self):
        print("Incluir passagem:")
        id_passagem = input("Digite o ID da passagem: ")
        id_passageiro = input("Digite o ID do passageiro: ")
        id_viagem = input("Digite o ID da viagem: ")
        assento = input("Digite o número do assento: ")
        preco = input("Digite o valor da passagem: ")

        passagem = {
            "id": id_passagem,
            "passageiro": id_passageiro,
            "viagem": id_viagem,
            "assento": assento,
            "preco": preco
        }

        self.passagens.append(passagem)
        print("Passagem incluída com sucesso!\n")
'''