class ManutencaoOnibus:
    def __init__(self, conexao):
        self._conexao = conexao
        self.onibus = []  # lista que armazena os ônibus

    def incluir(self):
        meuCursor = self._conexao.cursor() # objeto de manipulação de dados (insert, update, delete, select)
        # cursor é o objeto que permite ao programa executar comandos SQL no servidor:
        opcao = input("Deseja incluir um Ônibus?")
        if opcao == "s":
            result = meuCursor.execute(
                        ' SELECT capacidade, '+\
                        ' marca, modelo,'+\
                        ' idMotorista'+\
                        ' FROM EmpresaOnibus.Onibus ')
            registros = result.fetchall()
            if len(registros) == 0:     # se o departamento não existe, não podemos excluí-lo
                print("\nÔnibus não encontrado.\n")
            else:
                print("\nRegistro encontrado:")
                capacidade           = registros[0][0]
                marca               = registros[0][1]
                modelo      = registros[0][2]
                idMotorista     = registros[0][3]

                print(f"Capacidade: {capacidade}")
                print(f"Marca: {marca}")
                print(f"Modelo: {modelo}")
                print(f"ID Motorista: {idMotorista}\n")

                # montamos string com o comando Insert contendo os dados digitados:
                sComando =  "insert into EmpresaOnibus.Onibus " +\
                            " (capacidade, marca, modelo, idMotorista)"+\
                            "VALUES (?, ?, ?, ?)"
                
                # fazemos o cursor enviar ao servidor, para análise e execução,
                # a string com o comando Insert acima
                try: 
                    meuCursor.execute(sComando,(capacidade, marca, modelo, str(idMotorista)))
                    print("Ônibus incluído com sucesso!")
                except Exception as e: # em caso de erro
                    print(f"Não foi possível incluir. Erro: {e}.")

            meuCursor.commit()        
        else:
            input("Tecle [Enter] para Sair")

    def excluir(self):
        meuCursor = self._conexao.cursor() # objeto de manipulação de dados (insert, update, delete, select)
        # cursor é o objeto que permite ao programa executar comandos SQL no servidor:
        opcao = input("Deseja excluir um Ônibus?")
        if opcao == "s":
            onibusEscolhido = 1
            while onibusEscolhido!= 0:
            # pedimos que o usuário digite o número do departamento a ser excluído
                onibusEscolhido = int(input("ID do Ônibus (0 para terminar): "))
                if onibusEscolhido != 0: # usuário não quer terminar o cadastro
                # verifica no BD se existe um departamento com esse número digitado
                    result = meuCursor.execute(
                        ' SELECT idOnibus, capacidade, '+\
                        ' marca, modelo,'+\
                        ' idMotorista'+\
                        ' FROM EmpresaOnibus.Onibus '+\
                        ' Where idOnibus = ?', onibusEscolhido)
                registros = result.fetchall()
                if len(registros) == 0:     # se o departamento não existe, não podemos excluí-lo
                    print("\nÔnibus não encontrado.\n")
                else:
                    print("\nRegistro encontrado:")
                    idOnibus             = registros[0][0]
                    capacidade           = registros[0][1]
                    marca               = registros[0][2]
                    modelo      = registros[0][3]
                    idMotorista     = registros[0][4]

                    print(f"ID Ônibus\: {idOnibus}")
                    print(f"Capacidade: {capacidade}")
                    print(f"Marca: {marca}")
                    print(f"Modelo: {modelo}")
                    print(f"ID Motorista: {idMotorista}\n")
                    resposta = input("Deseja realmente excluir (s/n)?")
                    if resposta == "s":
                    
                        sComando =  ("Delete * from EmpresaOnibus.Onibus " +\
                                    " Where idOnibus = ?")
                        
                        # fazemos o cursor enviar ao servidor, para análise e execução,
                        # a string com o comando acima
                        try: 
                            meuCursor.execute(sComando,onibusEscolhido)
                            print("Ônibus Excluído com sucesso!")
                        except Exception as e: # em caso de erro
                            print(f"Não foi possível incluir. Erro: {e}.")
                    else:
                        input("Tecle [Enter] para Sair")
                meuCursor.commit()        
        else:
            input("Tecle [Enter] para Sair")

    def buscar(self):
        meuCursor = self._conexao.cursor() # objeto de manipulação de dados (insert, update, delete, select)
        # cursor é o objeto que permite ao programa executar comandos SQL no servidor:
        onibusEscolhido = 1
        while onibusEscolhido!= 0:
        # pedimos que o usuário digite o número do departamento a ser excluído
            onibusEscolhido = int(input("ID do Ônibus (0 para terminar): "))
            if onibusEscolhido != 0: # usuário não quer terminar o cadastro
                # verifica no BD se existe um departamento com esse número digitado
                result = meuCursor.execute(
                            ' SELECT idOnibus, capacidade, '+\
                            ' marca, modelo,'+\
                            ' idMotorista'+\
                            ' FROM EmpresaOnibus.Onibus '+\
                            ' WHERE idOnibus = ?', onibusEscolhido)
                registros = result.fetchall()
                if len(registros) == 0:     # se o departamento não existe, não podemos excluí-lo
                    print("\nÔnibus não encontrado.\n")
                else:
                    print("\nRegistro encontrado:")
                    idOnibus            = registros[0][0]
                    capacidade           = registros[0][1]
                    marca               = registros[0][2]
                    modelo      = registros[0][3]
                    idMotorista     = registros[0][4]

                    print(f"\nID Ônibus:  {idOnibus}")
                    print(f"Capacidade: {capacidade}")
                    print(f"Marca: {marca}")
                    print(f"Modelo: {modelo}")
                    print(f"ID Motorista: {idMotorista}\n")


        meuCursor.commit()

    def listar(self):
        meuCursor = self._conexao.cursor()
        result = meuCursor.execute(
                            ' SELECT idOnibus, capacidade, '+\
                            ' marca, modelo,'+\
                            ' idMotorista'+\
                            ' FROM EmpresaOnibus.Onibus')
        registros = result.fetchall()
        if len(registros) == 0:
            print("Motoristas não encontrados.")
        else:
            print("ID. \tCapacidade  \tMarca  \tModelo \tID Motorista")
            for motorista in registros:
                print(f"{str(motorista[0]).ljust(3, ' ')}   \t{str(motorista[1]).ljust(6, ' ')}          \t{str(motorista[2]).ljust(26, ' ')} \t{str(motorista[3]).ljust(40, ' ')} \t{str(motorista[4]).ljust(43, ' ')}           ")
            input("Tecle [enter] para terminar:")

        meuCursor.commit()