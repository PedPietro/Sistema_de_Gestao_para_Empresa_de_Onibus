import os
class viagem():
    def __init__():
        pass
    
    def seletordeopcoes():
        #Registro de inicio e de final de viagem, liberando passageiros e vagas
        os.system('cls') or None
        print("Selecione uma opção:")
        print("0 - Finalizar")
        print("1 - Registro do Inicio da Viagem")
        print("2 - Registro do Final da Viagem")
        print("3 - Liberar Passageiros e Vagas")
        
        escolha = str (input("Escolha: "))
        match escolha:
            case "1": Registroinicio()
            case "2": Registrofinal()
            case "3": Liberarpassageirosevagas()
            
            
        
        
    def Registroinicio():
        pass

    def Registrofinal():
        pass
    
    def Liberarpassageirosevagas():
        pass
        
        