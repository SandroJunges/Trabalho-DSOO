from entidade.pessoa import Pessoa

class Competidor(Pessoa):
    
    def __init__(self, nome: Pessoa, idade: int, nick: str):
        super().__init__(nome)
        self.__idade = idade
        self.__nick = nick
        
    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade:int):
        if isinstance(idade, int):
            self.__idade = idade

    @property
    def nick(self):
        return self.__nick

    @nick.setter
    def nick(self, nick: str):
        if isinstance(nick, str):
            self.__nick = nick