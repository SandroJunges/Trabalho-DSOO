from entidade.competidor import Competidor
from entidade.partida import Partida

class Competicao():
    
    def __init__(self, nome_torneio: str, esporte:str, formato: str, participantes: Competidor = None, partida: Partida = None):

        self.__nome_torneio = nome_torneio
        self.__esporte = esporte
        self.__formato = formato
        self.__participantes = participantes
        self.__partida = partida

    @property
    def nome_torneio(self):
        return self.__nome_torneio

    @nome_torneio.setter
    def nome_torneio(self, nome_torneio:str):
        if isinstance(nome_torneio, str):
            self.__nome_torneio = nome_torneio

    @property
    def esporte(self):
        return self.__esporte

    @esporte.setter
    def esporte(self, esporte:str):
        if isinstance(esporte, str):
            self.__esporte = esporte

    @property
    def formato(self):
        return self.__formato

    @formato.setter
    def formato(self, formato:str):
        if isinstance(formato, str):
            self.__formato = formato

    @property
    def participantes(self):
        return self.__participantes

    @participantes.setter
    def participantes(self, participantes: Competidor):
        if isinstance(participantes, Competidor):
            self.__participantes = participantes

    @property
    def partida(self):
        return self.__partida

    @partida.setter
    def partida(self, partida: Partida):
        if isinstance(partida, Partida):
            self.__partida = partida
