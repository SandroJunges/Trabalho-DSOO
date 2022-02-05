from entidade.pessoa import Pessoa

class Competidor(Pessoa):
    
    def __init__(self, nome: Pessoa):
        super().__init__(nome)