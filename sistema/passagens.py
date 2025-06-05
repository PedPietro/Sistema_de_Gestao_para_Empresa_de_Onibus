class ManutencaoPassagens:
    def __init__(self, conexao):
        self._conexao = conexao
        self.passagens = []  # lista que armazena as passagens

    def excluir(self):
        meuCursor = self.conexao.cursor() # objeto de manipulação de dados (insert, update, delete, select)
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
        print("Buscar passagem:")
        id_passagem = input("Digite o ID da passagem a buscar: ")
        encontrou = False
        for p in self.passagens:
            if p["id"] == id_passagem:
                print("ID:", p["id"])
                print("Passageiro:", p["passageiro"])
                print("Viagem:", p["viagem"])
                print("Assento:", p["assento"])
                print("Preço:", p["preco"])
                encontrou = True
                break
        if not encontrou:
            print("Passagem não encontrada.\n")

    def listar(self):
        print("Lista de passagens:")
        if len(self.passagens) == 0:
            print("Nenhuma passagem cadastrada.\n")
        else:
            for p in self.passagens:
                print("ID:", p["id"])
                print("Passageiro:", p["passageiro"])
                print("Viagem:", p["viagem"])
                print("Assento:", p["assento"])
                print("Preço:", p["preco"])
                print()

    

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