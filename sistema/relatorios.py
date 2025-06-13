class Relatorios:
    def __init__(self, conexao):
        self._conexao = conexao
        
    def passageirosEmUmaViagem(self):
        meuCursor = self._conexao.cursor()
        qualViagem = -1
        while qualViagem != 0:
            qualViagem = int(input('ID da Viagem (0 para terminar): '))
            if qualViagem != 0:
                result = meuCursor.execute(
                    ' SELECT * FROM EmpresaOnibus.Viagem '+\
                            ' WHERE idViagem = ?', qualViagem)
                
                registros = result.fetchall()
                
                if len(registros) == 0:
                    print('Não Há Viagem Registrada Com Esse ID!')
                else:
                    caminho = input('Caminho: ')
                    file = open(caminho, "w")
                    
                    idViagem        = registros[0][0]
                    distancia       = registros[0][1]
                    dataSaida       = registros[0][2]
                    custo           = registros[0][3]
                    idCidadeOrigem  = registros[0][4]
                    idCidadeDestino = registros[0][5]
                    idOnibus        = registros[0][6]
                    idMotorista     = registros[0][7]
                    
                    file.write("Id Viagem        : " + str(idViagem) + "\n")
                    file.write("Distancia        : " + str(distancia) + "\n")
                    file.write("Data Saida       : " + dataSaida.strftime('%d-%m-%Y %H:%M:%S') + "\n")
                    file.write("Custo Passagem   : " + str(custo) + "\n")
                                        
                    result = meuCursor.execute(
                        'SELECT nome FROM EmpresaOnibus.Cidade WHERE idCidade = ?', idCidadeOrigem
                    )
                    cidades = result.fetchall()
                    
                    file.write("Cidade Origem    : " + cidades[0][0] + "\n")
                    
                    result = meuCursor.execute(
                        'SELECT nome FROM EmpresaOnibus.Cidade WHERE idCidade = ?', idCidadeDestino
                    )
                    cidades = result.fetchall()
                    
                    file.write("Cidade Destino   : " + cidades[0][0] + "\n")
                                        
                    result = meuCursor.execute(
                        'SELECT placa FROM EmpresaOnibus.Onibus WHERE idOnibus = ?', idOnibus
                    )
                    onibus = result.fetchall()
                    
                    file.write("Id Onibus        : " + str(idOnibus) + "\n")
                    file.write("Onibus           : " + onibus[0][0] + "\n")
                                        
                    result = meuCursor.execute(
                        'SELECT nome FROM EmpresaOnibus.Motorista WHERE idMotorista = ?', idMotorista
                    )
                    motorista = result.fetchall()
                    
                    file.write("Id Motorista     : " + str(idMotorista) + "\n")
                    file.write("Nome Monitorista : " + motorista[0][0] + "\n")
                    
                    file.write("\n============================================\n")
                    
                    result = meuCursor.execute(
                        'SELECT * FROM EmpresaOnibus.Passagem WHERE idViagem = ?', idViagem
                    )
                    registros = result.fetchall()
                    
                    for passagem in registros:
                        result = meuCursor.execute(
                            'SELECT nome FROM EmpresaOnibus.Passageiro WHERE idPassageiro = ?', passagem[3]
                        )
                        passageiro = result.fetchall()
                        
                        file.write("\nId Passagem      : " + str(passagem[0]) + "\n")
                        file.write("Assento          : " + str(passagem[1]) + "\n")
                        file.write("Id Passageiro    : " + str(passagem[3]) + "\n")
                        file.write("Nome Passageiro  : " + passageiro[0][0] + "\n")
                
                    file.close()
                    
                    print('Tudo Pronto!')
        
        meuCursor.commit()
