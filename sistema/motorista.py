class ManutencaoMotorista:
    def __init__(self, conexao):
        self._conexao = conexao
        self.motoristas = []  # lista que armazena os motoristas

    #Chico Pediu Para Não Incluir Os Dados Na Tabela Por Python
    '''def incluir(self):
        print("Incluir motorista:")
        id_motorista = input("Digite o ID do motorista: ")
        nome = input("Digite o nome do motorista: ")
        cnh = input("Digite o número da CNH: ")
        motorista = {"id": id_motorista, "nome": nome, "cnh": cnh}
        self.motoristas.append(motorista)
        print("Motorista incluído com sucesso!\n")'''

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
        meuCursor = self.conexao.cursor() 
        meuCursor.execute('SELECT idMotorista, nome FROM EmpresaOnibus.Motorista ')
        registros = meuCursor.fetchall()
        if len(registros) == 0: 
            print("Motoristas não encontrados.")
        else:
            print("\tID\tnome ")
            print("\t--\t------------------------")
            for motorista in registros:
                print(f"\t{motorista[0]}\t{motorista[1]}")
                
            input("Tecle [enter] para terminar:")
            
        meuCursor.close()
        
        
        '''CREATE TABLE EmpresaOnibus.Motorista(
	nome varchar(50),
	idMotorista int primary key identity
	)'''