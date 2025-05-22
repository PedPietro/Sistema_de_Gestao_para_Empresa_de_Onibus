import os
class viagem():
    def __init__(self):
        self.status = "planejada"
    
    def Registroinicio(self):
        self.status = "Em andamento"

    def Registrofinal(self):
        self.status = "Finalizada"
    
    def Liberarpassageirosevagas(self):
        pass
        