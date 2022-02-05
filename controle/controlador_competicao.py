from limite.tela_competicao import TelaCompeticao
from entidade.competicao import Competicao
from controle.controlador_competidor import ControladorCompetidor

class ControladorCompeticao():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_competicao = TelaCompeticao()
        self.__competicoes = []

    def seleciona_competicao(self, nome_torneio = str):
        for competicao in self.__competicoes:
            if (competicao.nome_torneio == nome_torneio):
                return competicao
        return None

    def criar_competicao(self):
        dados_competicao = self.__tela_competicao.pega_dados()
        competicao = Competicao(dados_competicao["nome_torneio"], dados_competicao["esporte"], dados_competicao["formato"])
        self.__competicoes.append(competicao)

    
    def informacoes_competicao(self):
        for competicao in self.__competicoes:
            self.__tela_competicao.mostra_dados({"nome_torneio": competicao.nome_torneio, "esporte": competicao.esporte, "formato" : competicao.formato})
    
    def alterar_competicao(self):
        self.informacoes_competicao()
        nome_torneio = self.__tela_competicao.seleciona_competicao()
        competicao = self.seleciona_competicao(nome_torneio)

        if(competicao is not None):
            novos_dados_competicao = self.__tela_competicao.pega_dados()
            competicao.nome_torneio = novos_dados_competicao["nome_torneio"]
            competicao.esporte = novos_dados_competicao["esporte"]
            competicao.formato = novos_dados_competicao["formato"]
            self.informacoes_competicao()
        else:
            self.__tela_competicao.mostra_mensagem("\033[31mATENCAO: Nome de torneio não encontrado!\033[m")

    def mata_mata(self):
        pass

    def retornar (self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.criar_competicao, 2: self.informacoes_competicao, 3: self.alterar_competicao, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_competicao.tela_opcoes()]()