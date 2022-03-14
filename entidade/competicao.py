class Competicao():
    
    def __init__(self, nome_torneio: str, esporte:str, formato: int, organizador: str, participantes: list, ganhador: str, id_competicao: int):

        self.__nome_torneio = nome_torneio
        self.__esporte = esporte
        self.__formato = formato
        self.__organizador = organizador
        self.__participantes = participantes
        self.__ganhador = ganhador
        self.__id_competicao = id_competicao

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
    def formato(self, formato:int):
        if isinstance(formato, int):
            self.__formato = formato
    
    @property
    def organizador(self):
        return self.__organizador

    @organizador.setter
    def organizador(self, organizador:str):
        if isinstance(organizador, str):
            self.__organizador = organizador

    @property
    def participantes(self):
        return self.__participantes

    @participantes.setter
    def participantes(self, participantes: list):
        if isinstance(participantes, list):
            self.__participantes = participantes
    
    @property
    def ganhador(self):
        return self.__ganhador

    @ganhador.setter
    def ganhador(self, ganhador:str):
        if isinstance(ganhador, str):
            self.__ganhador = ganhador

    @property
    def id_competicao(self):
        return self.__id_competicao