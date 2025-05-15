import os
from conectaBD import co

def seletor(): # CRUD: Create Retrieve Update Delete
    opcao = 1
    while opcao != 0:
        os.system('cls') or None
        print("Operações disponíveis")
        print("========= ===========\n")
        print("0 - Terminar este programa")
        print("1 - Incluir departamentos")
        print("2 - Alterar departamentos") 
        print("3 - Excluir departamentos")
        print("4 - Listar departamentos")
        opcao = int(input("\nDigite o número da opção desejada:"))
        match opcao:
            case 1: incluir()
            case 2: alterar()
            case 3: excluir()
            case 4: listar()

def incluir():
    meuCursor = conexao.cursor() # cria um cursor, objeto de comandos de SQL
    numDepto = 1
    while numDepto != 0:
        # pedimos que o usuário digite os dados do novo departamento
        numDepto = int(input("Número do departamento (0 para terminar): "))
        
        if numDepto != 0: # usuário não quer terminar o cadastro
            nomeDepto = input("Nome do departamento: ")
            gerente_ssn = input("Cpf do gerente: ")
            dataInicial = input("Data de início do gerente (dd/mm/aaaa): ")
 
            # montamos string com o comando Insert contendo os dados digitados:
            sComando =  "insert into empresa.departamento " +\
                        " (numDepto, nomeDepto, gerente_NumSegSocial, gerente_dataInicial)"+\
                        "VALUES (?, ?, ?, Convert(date, ?, 103))"
            
            # fazemos o cursor enviar ao servidor, para análise e execução,
            # a string com o comando Insert acima
            try: 
                meuCursor.execute(sComando,[numDepto, nomeDepto, gerente_ssn, dataInicial])
                print("Departamento incluído com sucesso!")
            except: # em caso de erro
                print("Não foi possível incluir. Pode haver departamento repetido.")
            
    # após digitar numDepto = 0, paramos o cadastramento
    # e enviamos os registros inseridos para serem definitivamente
    # gravados no servidor de banco de dados remoto
    meuCursor.commit() # solicita ao servidor que registre as mudanças no BD 

def alterar():
    # cursor é o objeto que permite ao programa executar comandos SQL no servidor:
    meuCursor = conexao.cursor() # objeto de manipulação de dados
    numDeptoDigitado = 1
    while numDeptoDigitado != 0:
        # pedimos que o usuário digite o número do departamento a ser alterado
        numDeptoDigitado = int(input("Número do departamento (0 para terminar): "))
        
        if numDeptoDigitado!= 0: # usuário não quer terminar o cadastro
            # verifica no BD se existe um departamento com esse número digitado
            sComando = 'SELECT NOMEDEPTO, GERENTE_NUMSEGSOCIAL, '+\
            ' GERENTE_DATAINICIAL '+\
            ' FROM EMPRESA.DEPARTAMENTO '+\
            ' WHERE NUMDEPTO = ?'
            result = meuCursor.execute(sComando, numDeptoDigitado)                   
            registros = result.fetchall()
            if len(registros) == 0:
                print("Departamento não encontrado.")
            else:
                print("Registro encontrado:")
                nomeDepto = registros[0][0]     # 1o campo do 1o registro
                gerente   = registros[0][1]     # 2o campo do 1o registro
                data      = registros[0][2]     # 3o campo do 1o registro      
                print("Nome do departamento: "+nomeDepto)
                print("Gerente:"+gerente)
                print("Data inicial:"+data)
                print("Digite os novos dados. [Enter] manterá os atuais:")
                nomeDepto = input("Nome do departamento: ")
                gerente = input("Cpf do gerente: ")
                data = input("Data de início do gerente (dd/mm/aaaa): ")
                
                # montamos string com o comando Update contendo os 
                # dados digitados:
                
                if nomeDepto == "":             # usuário digitou [Enter]
                    nomeDepto = registros[0][0] # nome original do BD
                    
                if gerente == "":               # usuário digitou [Enter]
                    gerente = registros[0][1]   # gerente original do BD
                    
                if data == "":                  # usuário digitou [Enter]
                    data = registros[0][2]      # data original do BD
                    
                sComando =  " Update empresa.departamento "+\
                            " SET nomeDepto = ?, "+\
                            "     gerente_NumSegSocial = ?, "+\
                            "     gerente_dataInicial = Convert(date, ?, 103) "+\
                            " where numDepto = ? "
                try:
                    meuCursor.execute(sComando,[nomeDepto, gerente, data, numDeptoDigitado])
                    print("Departamento alterado com sucesso!")
                except: # em caso de erro
                    print("Não foi possível alterar. Verifique os dados.")
    
    meuCursor.commit() # registrar definitivamente as mudanças para o BD 

def excluir():
    meuCursor = conexao.cursor() # objeto de manipulação de dados (insert, update, delete, select)
    # cursor é o objeto que permite ao programa executar comandos SQL no servidor:
    numDeptoDigitado = 1
    while numDeptoDigitado!= 0:
    # pedimos que o usuário digite o número do departamento a ser excluído
        numDeptoDigitado = int(input("Número do departamento (0 para terminar): "))
        if numDeptoDigitado!= 0: # usuário não quer terminar o cadastro
            # verifica no BD se existe um departamento com esse número digitado
            result = meuCursor.execute(
                        ' SELECT NOMEDEPTO, GERENTE_NUMSEGSOCIAL, '+\
                        ' GERENTE_DATAINICIAL '+\
                        ' FROM EMPRESA.DEPARTAMENTO '+\
                        ' WHERE NUMDEPTO = ?', numDeptoDigitado)
            registros = result.fetchall()
            if len(registros) == 0:     # se o departamento não existe, não podemos excluí-lo
                print("Departamento não encontrado.")
            else:
                print("Registro encontrado:")
                nomeDepto = registros[0][0]
                gerente   = registros[0][1]
                data      = registros[0][2]
                print("Nome do departamento: "+nomeDepto)
                print("Gerente:"+gerente)
                print("Data inicial:"+data)
                resposta = input("Deseja realmente excluir (s/n)?")
                if resposta == "s":
                # criamos uma string com o comando Delete para excluir o registro lido
                    sComando = " Delete from empresa.departamento " +\
                    " where numDepto = ? " 
                    # fazemos o cursor enviar ao servidor o comando Delete acima criado
                    try: # tente executar o comando abaixo:
                        meuCursor.execute(sComando, numDeptoDigitado)
                        print("Registro excluído.")
                    except: # em caso de erro
                        print("Não foi possível excluir. Pode ser uma tabela que está em uso em outra tabela(foreign key)") 
    
    meuCursor.commit() # enviar as mudanças para o BD 

def listar():
    meuCursor = conexao.cursor() # objeto de manipulação de dados
    # busca no BD os registros de departamentos
    try: 
        result = meuCursor.execute(
        ' SELECT numdepto, NOMEDEPTO, GERENTE_NUMSEGSOCIAL, '+\
        ' GERENTE_DATAINICIAL '+\
        ' FROM EMPRESA.DEPARTAMENTO order by NomeDepto') 
        registros = result.fetchall()
    except:
        print("Erro na busca dos dados\n")
        
    print("Num. Nome        Gerente     Data Inicial")
    for depto in registros:
        print(f"{depto[0]}\t{depto[1]}\t{depto[2]}\t{depto[3]}")
    input("Tecle [enter] para terminar:")

                    
if __name__ == "__main__":
    if conectouAoBancoDeDados() :
        seletor()
        conexao.close()
    print("Programa encerrado")

