class ManutencaoOnibus:
    def __init__(self, conexao):
        self._conexao = conexao
        self.onibus = []  # lista que armazena os ônibus

    def buscar(self):
        meuCursor = self.conexao.cursor() # objeto de manipulação de dados (insert, update, delete, select)
        # cursor é o objeto que permite ao programa executar comandos SQL no servidor:
        onibusEscolhido = 1
        while onibusEscolhido!= 0:
        # pedimos que o usuário digite o número do departamento a ser excluído
            onibusEscolhido = int(input("ID do Passageiro (0 para terminar): "))
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
                    print("Passageiro não encontrado.")
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
                    print(f"ID Motorista: {idMotorista}")


        meuCursor.commit()

    def listar(self):
        meuCursor = self._conexao.cursor() # objeto de manipulação de dados (insert, update, delete, select)
        # cursor é o objeto que permite ao programa executar comandos SQL no servidor:
        # pedimos que o usuário digite o número do departamento a ser excluído
                # verifica no BD se existe um departamento com esse número digitado
        result = meuCursor.execute(
                            ' SELECT idOnibus, capacidade, '+\
                            ' marca, modelo,'+\
                            ' idMotorista'+\
                            ' FROM EmpresaOnibus.Onibus')
        registros = result.fetchall()
        if len(registros) == 0:     # se o departamento não existe, não podemos excluí-lo
            print("Motoristas não encontrados.")
        else:
            print("12345678901234567890123456789012345678901234567890123456789012345678901234567890")
            print("ID. \tCapacidade  \tMarca  \tModelo \tID Motorista")
            for motorista in registros:
                #arrumar indexação dessa merda aaaaaaaaaaaaa
                
                print(f"{motorista[0]}   \t{motorista[1]}          \t{motorista[2]} \t{motorista[3]} \t{motorista[4]}           ")
            input("Tecle [enter] para terminar:")

        meuCursor.commit()