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
        self.abre_selecao()

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

    def retornar (self):
        self.abre_selecao()

#Abre a tela de cadastro para o Admin.

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_competidor, 2: self.cadastra_organizador, 3: self.cadastra_partida, 4: self.cadastra_competicao, 0: self.retornar}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes(self)
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

#Funções competidor e administrador servem para escolher a primeira tela.

    def competidor(self):
        self.abre_tela_visualizacao()

    def administrador(self):
        self.abre_tela()

#Abre a tela para escolher entre Competidor e Admin.

    def abre_selecao(self):
        lista_opcoes = {1: self.competidor, 2: self.administrador, 0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_inicial(self)
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

#Abre a tela de visualização para o Competidor.

    def visualizar_campeonatos(self):
        pass

    def visualizar_partidas(self):
        pass

    def abre_tela_visualizacao(self):
        lista_opcoes = {1: self.visualizar_campeonatos, 2: self.visualizar_partidas, 0: self.retornar}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_visualizacao(self)
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()