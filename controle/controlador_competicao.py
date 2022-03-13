from limite.tela_competicao import TelaCompeticao
from entidade.competicao import Competicao
from controle.controlador_competidor import ControladorCompetidor
from controle.controlador_partida import ControladorPartida
from entidade.partida import Partida

class ControladorCompeticao():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_competicao = TelaCompeticao()
        self.__competicoes = []
        self.__id_competicao = 0

    def criar_competicao(self):
        list_organizador = self.__controlador_sistema.controlador_organizador.dados_nome_organizador()
        dados_competicao = self.__tela_competicao.pega_dados(list_organizador)
        if (dados_competicao == None):
            return
        else:
            id = 0
            for competicao in self.__competicoes:
                if competicao.id_competicao > id:
                    id = competicao.id_competicao
            self.__id_competicao = id + 1
            participantes = self.__controlador_sistema.controlador_competidor.lista_competidores
            competicao = Competicao(dados_competicao["nome_torneio"], dados_competicao["esporte"], dados_competicao["formato"], dados_competicao["organizador"], participantes, self.__id_competicao)
            self.__competicoes.append(competicao)
    
    def pega_competicao_por_id(self, id):
        if id == "" or id ==  None:
            return None

        for competicao in self.__competicoes:
            if competicao.id_competicao == int(id):
                return competicao
        return None

    def dados_lista_competicoes(self):
        return [f'ID: {competicao.id_competicao}  Nome: {competicao.nome_torneio} | Esporte: {competicao.esporte} | Qtd. Participantes: {competicao.formato} | Organizador: {competicao.organizador}' for competicao in self.__competicoes]        
    
    def informacoes_competicao(self):
        self.__tela_competicao.mostra_dados(self.dados_lista_competicoes())
    
    def administrar_competicao(self):
        id = self.__tela_competicao.seleciona_competicao(self.dados_lista_competicoes())
        competicao = self.pega_competicao_por_id(id)
        if(competicao is not None):
            lista_participantes = self.__controlador_sistema.controlador_competidor.dados_nome_competidores()
            n = 1
            while n <= competicao.formato:
                novos_dados_competicao = self.__tela_competicao.partidas(lista_participantes)
                if novos_dados_competicao != None:
                    #aqui é pra remover SAN ve ai
                    competicao.participantes = competicao.participantes_dao.remove("participante")
                    n = n+1
                else:
                    return
            return
        
    def relatorio (self):
        return

    def retornar (self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.criar_competicao, 2: self.informacoes_competicao, 3: self.administrar_competicao, 4: self.relatorio, 5: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_competicao.tela_opcoes()]()

