from limite.tela_sistema import TelaSistema
from controle.controlador_competidor import ControladorCompetidor
from controle.controlador_organizador import ControladorOrganizador
from controle.controlador_partida import ControladorPartida
from controle.controlador_competicao import ControladorCompeticao

class ControladorSistema:
    def __init__(self):
        self.__controlador_competidor = ControladorCompetidor(self)
        self.__controlador_organizador = ControladorOrganizador(self)
        self.__controlador_partida = ControladorPartida(self)
        self.__controlador_competicao = ControladorCompeticao(self)
        self.__tela_sistema = TelaSistema

    def inicializa_sistema(self):
        self.abre_tela()

    def cadastra_competidor(self):
        self.__controlador_competidor.abre_tela()

    def cadastra_organizador(self):
        self.__controlador_organizador.abre_tela()

    def cadastra_partida(self):
        self.__controlador_partida.abre_tela()

    def cadastra_competicao(self):
        self.__controlador_competicao.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_competidor, 2: self.cadastra_organizador, 3: self.cadastra_partida, 4: self.cadastra_competicao, 0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes(self)
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()