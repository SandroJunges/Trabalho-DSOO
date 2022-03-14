from limite.tela_competicao import TelaCompeticao
from entidade.competicao import Competicao
from persistencia.competicao_dao import CompeticaoDAO
from excecoes.empty_field import EmptyFieldError

class ControladorCompeticao():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_competicao = TelaCompeticao()
        self.__competicao_dao = CompeticaoDAO()
        self.__id_competicao = 0

    def criar_competicao(self):
        list_organizador = self.__controlador_sistema.controlador_organizador.dados_lista_organizadores()
        dados_competicao = self.__tela_competicao.pega_dados(list_organizador)
        if (dados_competicao == None):
            return

        try:
            if dados_competicao['nome_torneio'] == "" or dados_competicao['esporte'] == "":
                raise EmptyFieldError()
        except EmptyFieldError as e:
            return self.__tela_competicao.mostra_mensagem(e.mensagem)   

        else:
            id = 0
            for competicao in self.__competicao_dao.get_all():
                if competicao.id_competicao > id:
                    id = competicao.id_competicao
            self.__id_competicao = id + 1
            n = 1
            participantes = []
            while n <= dados_competicao['formato']:
                participante = self.__tela_competicao.pega_participantes(self.__controlador_sistema.controlador_competidor.dados_lista_competidores())
                participantes.append(participante)
                n = n +1
            ganhador = 'Nenhum'
            competicao = Competicao(dados_competicao["nome_torneio"], dados_competicao["esporte"], dados_competicao["formato"], dados_competicao["organizador"], participantes, ganhador, self.__id_competicao)
            self.__competicao_dao.add(competicao)
            self.__tela_competicao.mostra_mensagem("Competição criada com sucesso!")
    
    def pega_competicao_por_id(self, id):
        if id == "" or id ==  None:
            return None

        for competicao in self.__competicao_dao.get_all():
            if competicao.id_competicao == int(id):
                return competicao
        return None

    def dados_lista_competicoes(self):
        return [f'ID: {competicao.id_competicao}  Nome: {competicao.nome_torneio} | Esporte: {competicao.esporte} | Qtd. Participantes: {competicao.formato} | Organizador: {competicao.organizador}' for competicao in self.__competicao_dao.get_all()]        
    
    def excluir_competicao(self):
        id = self.__tela_competicao.seleciona_competicao(self.dados_lista_competicoes())
        competicao = self.pega_competicao_por_id(id)

        if (competicao is not None):
            self.__tela_competicao.mostra_mensagem("Competição excluída!")
            self.__competicao_dao.remove(competicao)
    
    def administrar_competicao(self):
        id = self.__tela_competicao.seleciona_competicao(self.dados_lista_competicoes())
        competicao = self.pega_competicao_por_id(id)

        if(competicao is not None):
            lista_participantes = []
            total_participantes = competicao.participantes
            for n in total_participantes:
                    competidor = self.__controlador_sistema.controlador_competidor.pega_competidor_por_id(n)
                    lista_participantes.append(competidor.nome)
            n = 1
            while n <= competicao.formato:
                if len(lista_participantes) == 1:
                    self.__tela_competicao.ganhador(lista_participantes)
                    competicao.ganhador = lista_participantes[0]
                    n = competicao.formato + 1
                    self.__competicao_dao.add(competicao)
                    self.__tela_competicao.mostra_mensagem("Competição finalizada!")
                else:
                    rodada = competicao.formato
                    novos_dados_competicao = self.__tela_competicao.partidas(n, rodada, lista_participantes)
                    if novos_dados_competicao != None:
                        #aqui é pra remover SAN ve ai
                            name =  novos_dados_competicao[0]
                            competicao.participantes.remove(self.__controlador_sistema.controlador_competidor.pega_id_por_nome(name))
                            lista_participantes.remove(name)
                            n = n+1
                    else:
                        return
    
    def dados_competicao_ganhador(self):
         return [f'ID: {competicao.id_competicao}  Nome: {competicao.nome_torneio} | Esporte: {competicao.esporte} | Qtd. Participantes: {competicao.formato} ||||| Vencedor: {competicao.ganhador}' for competicao in self.__competicao_dao.get_all()]        
        
    def relatorio (self):
        self.__tela_competicao.mostra_dados(self.dados_competicao_ganhador())

    def retornar (self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.criar_competicao, 2: self.excluir_competicao, 3: self.administrar_competicao, 4: self.relatorio, 5: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_competicao.tela_opcoes()]()