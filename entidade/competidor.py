from entidade.pessoa import Pessoa

class Competidor(Pessoa):
    
    def __init__(self, nome: Pessoa, email: str):
        super().__init__(nome)
        if isinstance(email, str):
            self.__email = email

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email:str):
        if isinstance(email, str):
            self.__email = email