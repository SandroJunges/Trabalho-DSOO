class Partida:

    def __init__(self, participante1: str, participante2: str, placarp1 : int, placarp2 : int):
        self.__participante1 = participante1
        self.__participante2 = participante2
        self.__placarp1 = placarp1
        self.__placarp2 = placarp2


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

    @property
    def placarp1(self):
        return self.__placarp1

    @placarp1.setter
    def placarp1(self, placarp1: int):
        if isinstance(placarp1, int):
            self.__placarp1 = placarp1

    @property
    def placarp2(self):
        return self.__placarp2

    @placarp2.setter
    def placarp2(self, placarp2: int):
        if isinstance(placarp2, int):
            self.__placarp2 = placarp2
