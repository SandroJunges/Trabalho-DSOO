from entidade.competidor import Competidor

class Partida:

    def __init__(self, data: str, resultado:str, participantes: Competidor):

        self.__data = data
        self.__resultado = resultado
        self.__participantes = participantes

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data:str):
        if isinstance(data, str):
            self.__data = data

    @property
    def resultado(self):
        return self.__resultado

    @resultado.setter
    def resultado(self, resultado:str):
        if isinstance(resultado, str):
            self.__resultado = resultado

    @property
    def participantes(self):
        return self.__participantes

    @participantes.setter
    def participantes(self, participantes: Competidor):
        if isinstance(participantes, Competidor):
            self.__participantes = participantes
