from entidade.pessoa import Pessoa

class Organizador(Pessoa):

    def __init__(self, nome: Pessoa, senha: str, id_organizador : int):
        super().__init__(nome)
        if isinstance(senha, str):
            self.__senha = senha
        self.__id_organizador = id_organizador
        
    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha:str):
        if isinstance(senha, str):
            self.__senha = senha
    
    @property
    def id_organizador(self):
        return self.__id_organizador