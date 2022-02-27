class Partida:

    def __init__(self, participante1: str, participante2: str):
        self.__participante1 = participante1
        self.__participante2 = participante2

    @property
    def participante1(self):
        return self.__participante1

    @participante1.setter
    def participante1(self, participante1: str):
        if isinstance(participante1, str):
            self.__participante1 = participante1
    
    @property
    def participante2(self):
        return self.__participante2

    @participante2.setter
    def participante2(self, participante2: str):
        if isinstance(participante2, str):
            self.__participante2 = participante2
