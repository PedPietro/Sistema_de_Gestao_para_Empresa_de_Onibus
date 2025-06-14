class ManutencaoMotorista:
    def __init__(self, conexao):
        self._conexao = conexao
        self.motoristas = []  # lista que armazena os motoristas

    #Chico Pediu Para Não Incluir Os Dados Na Tabela Por Python
    def incluir(self):          # Salva os dados do formulário (incluídos ou editados) no banco de dados
        meuCursor = self._conexao.cursor() # cria um cursor, objeto de comandos de SQL
        idPassageiro = 1
        while idPassageiro != 0:
            # pedimos que o usuário digite os dados do novo Passageiro
            idPassageiro = int(input("ID do novo Passageiro (0 para terminar): "))
            
            if idPassageiro != 0: # usuário não quer terminar o cadastro
                cpf = input("CPF: ")
                nome = input("Nome do Passageiro: ")
                telefone = input("Telefone: ")
                dataNascimento_str = input("Data do Nascimento (yyyy/mm/dd): ")
                dataNascimento = datetime.strptime(dataNascimento_str, "%Y/%m/%d").date()
                email = input("Email do Passageiro: ")
     
                # montamos string com o comando Insert contendo os dados digitados:
                sComando =  "insert into EmpresaOnibus.Passageiro " +\
                            " (cpf, nome, telefone, dataNascimento, email)"+\
                            "VALUES (?, ?, ?, Convert(date, ?, 13), ?)"
                
                # fazemos o cursor enviar ao servidor, para análise e execução,
                # a string com o comando Insert acima
                try: 
                    meuCursor.execute(sComando,(idPassageiro, cpf, nome, telefone, str(dataNascimento), email))
                    print("Passageiro incluído com sucesso!")
                except Exception as e: # em caso de erro
                    print(f"Não foi possível incluir. Erro: {e}.")

    def excluir(self):
        print("Excluir motorista:")
        id_motorista = input("Digite o ID do motorista que deseja excluir: ")
        encontrou = False
        for m in self.motoristas:
            if m["id"] == id_motorista:
                self.motoristas.remove(m)
                encontrou = True
                print("Motorista excluído com sucesso!\n")
                break
        if not encontrou:
            print("Motorista não encontrado.\n")

    def alterar(self):
        print("Alterar motorista:")
        id_motorista = input("Digite o ID do motorista a alterar: ")
        encontrou = False
        for m in self.motoristas:
            if m["id"] == id_motorista:
                novo_nome = input("Digite o novo nome: ")
                nova_cnh = input("Digite o novo número da CNH: ")
                m["nome"] = novo_nome
                m["cnh"] = nova_cnh
                encontrou = True
                print("Motorista alterado com sucesso!\n")
                break
        if not encontrou:
            print("Motorista não encontrado.\n")

    def buscar(self):
        print("Buscar motorista:")
        id_motorista = input("Digite o ID do motorista a buscar: ")
        encontrou = False
        for m in self.motoristas:
            if m["id"] == id_motorista:
                print("ID:", m["id"])
                print("Nome:", m["nome"])
                print("CNH:", m["cnh"])
                encontrou = True
                break
        if not encontrou:
            print("Motorista não encontrado.\n")

    
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
                #arrumar indexação dessa merda aaaaaaaaaaaaa
                print(f"{motorista[0]}   \t{motorista[1]:20}")
            input("Tecle [enter] para terminar:")

            
        meuCursor.commit()
        