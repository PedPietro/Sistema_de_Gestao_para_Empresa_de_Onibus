class ManutencaoUF:
    def __init__(self,  conexao):
        self._conexao = conexao
        self.estados = []  # Lista para armazenar os estados (UF)

def listar(self):
    meuCursor = self._conexao.cursor() # objeto de manipulação de dados
    # busca no BD os registros de departamentos
    #try: 
    result = meuCursor.execute(
                        ' SELECT siglaUF,' \
                        ' nome'+\
                        ' FROM Viagem ')
    registros = result.fetchall()
    #except:
    #   print("Erro na busca dos dados\n")
    if len(registros) == 0:
        print("Viagens não encontradas")
    else:
        print("Sigla UF   \tNome")
        for uf in registros:
            print(f"{(uf[0]).ljust(3, ' ')} \t{uf[1]}")
            # passagem[2].strftime() serve para converter o datetime do bd em texto
        input("Tecle [enter] para terminar:")

def buscar(self):
    meuCursor = self.conexao.cursor() # objeto de manipulação de dados (insert, update, delete, select)
    # cursor é o objeto que permite ao programa executar comandos SQL no servidor:
    ufEscolhida = 1
    while ufEscolhida!= 0:
    # pedimos que o usuário digite o número do departamento a ser excluído
        ufEscolhida = int(input("ID Da UF (0 para terminar): "))
        if ufEscolhida != 0: # usuário não quer terminar o cadastro
            # verifica no BD se existe um departamento com esse número digitado
            result = meuCursor.execute(
                        ' SELECT siglaUF,' \
                        ' nome'+\
                        ' FROM Viagem where idUF = ?', ufEscolhida)
            registros = result.fetchall()
            if len(registros) == 0:     # se o departamento não existe, não podemos excluí-lo
                print("Viagem não encontrado.")
            else:
                print("Registro encontrado:")
                siglaUF            = registros[0][0]
                nome           = registros[0][1]

                print("Sigla UF: "+siglaUF)
                print("Nome: "+nome)

    meuCursor.commit() # enviar as mudanças para o BD                    
