from limite.tela_sistema import TelaSistema
from controle.controlador_competidor import ControladorCompetidor
from controle.controlador_partida import ControladorPartida
from controle.controlador_competicao import ControladorCompeticao

class ControladorSistema:
    
    def __init__(self):
        self.__controlador_competidor = ControladorCompetidor(self)
        self.__controlador_partida = ControladorPartida(self)
        self.__controlador_competicao = ControladorCompeticao(self)
        self.__tela_sistema = TelaSistema

    def inicializa_sistema(self):
        self.abre_tela()

    def cadastra_competidor(self):
        self.__controlador_competidor.abre_tela()

<<<<<<< HEAD
    def cadastra_organizador(self):
        self.__controlador_organizador.abre_tela()

=======
>>>>>>> 978e9269b9cd34b4c5e22058cd0323a01ba82c9d
    def cadastra_competicao(self):
        self.__controlador_competicao.abre_tela()
    
    def administra_competicao(self):
        self.__controlador_competicao.administrar()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
<<<<<<< HEAD
        lista_opcoes = {1: self.cadastra_competidor, 2: self.cadastra_organizador, 3: self.cadastra_competicao, 4: self.administra_competicao, 0: self.encerra_sistema}
=======
        lista_opcoes = {1: self.cadastra_competidor, 2: self.cadastra_competicao, 3: self.administra_competicao, 0: self.encerra_sistema}
>>>>>>> 978e9269b9cd34b4c5e22058cd0323a01ba82c9d

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes(self)
            funcao_escolhida = lista_opcoes[opcao_escolhida]
<<<<<<< HEAD
            funcao_escolhida()
=======
            funcao_escolhida()
>>>>>>> 978e9269b9cd34b4c5e22058cd0323a01ba82c9d
