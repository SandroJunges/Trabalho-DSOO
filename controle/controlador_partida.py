from limite.tela_partida import TelaPartida
from persistencia.partida_dao import PartidaDAO

class ControladorPartida():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_partida = TelaPartida()
        self.__partida_dao = PartidaDAO()
        
    def retornar (self):
        self.__controlador_sistema.controlador_competicao.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.relatorio, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_partida.tela_opcoes()]()