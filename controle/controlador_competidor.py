from limite.tela_competidor import TelaCompetidor
from entidade.competidor import Competidor
from persistencia.competidor_dao import CompetidorDAO
from excecoes.duplicated_exception import DuplicatedException
from excecoes.empty_field import EmptyFieldError

class ControladorCompetidor():

    def __init__(self, controlador_sistema):
        self.__competidor_dao = CompetidorDAO()
        self.__controlador_sistema = controlador_sistema
        self.__tela_competidor = TelaCompetidor()
        self.__id_competidor = 0
    
    def incluir_competidor(self):
        dados_competidor = self.__tela_competidor.pega_dados()
        if (dados_competidor == None):
            return

        try:
            if dados_competidor['nome'] == "" or dados_competidor['nick'] == "":
                raise EmptyFieldError()
        except EmptyFieldError as e:
            return self.__tela_competidor.mostra_mensagem(e.mensagem)
        try:
            self.verifica_duplicidade_de_nome(dados_competidor['nome'])
            self.verifica_duplicidade_de_nick(dados_competidor['nick'])
        except DuplicatedException as e:
            return self.__tela_competidor.mostra_mensagem(str(e))

        else:
            id = 0
            for competidor in self.__competidor_dao.get_all():
                if competidor.id_competidor > id:
                    id = competidor.id_competidor
            self.__id_competidor = id + 1
            competidor = Competidor(dados_competidor["nome"], dados_competidor["idade"], dados_competidor["nick"], self.__id_competidor)
            self.__competidor_dao.add(competidor)
            self.__tela_competidor.mostra_mensagem("Competidor criado!")

    def pega_competidor_por_id(self, id):
        if id == "" or id ==  None:
            return None

        for competidor in self.__competidor_dao.get_all():
            if competidor.id_competidor == int(id):
                return competidor
        return None

    def dados_lista_competidores(self):
        return [f'ID: {competidor.id_competidor}  Nome: {competidor.nome} | Idade: {competidor.idade} | Nick: {competidor.nick}' for competidor in self.__competidor_dao.get_all()]

    def alterar_competidor(self):
        
        id = self.__tela_competidor.seleciona_competidor(self.dados_lista_competidores())
        competidor = self.pega_competidor_por_id(id)

        novos_dados_competidor = self.__tela_competidor.pega_dados()
        try:
            if novos_dados_competidor['nome'] == "" or novos_dados_competidor['nick'] == "":
                raise EmptyFieldError()
        except EmptyFieldError as e:
            return self.__tela_competidor.mostra_mensagem(e.mensagem)
        try:
            self.verifica_duplicidade_de_nome(novos_dados_competidor['nome'])
            self.verifica_duplicidade_de_nick(novos_dados_competidor['nick'])
        except DuplicatedException as e:
            return self.__tela_competidor.mostra_mensagem(str(e))

        if(competidor is not None):
            if novos_dados_competidor != None:
                competidor.nome = novos_dados_competidor["nome"]
                competidor.idade = novos_dados_competidor["idade"]
                competidor.nick = novos_dados_competidor["nick"]
                self.__competidor_dao.add(competidor)
                return
            return
    
    def lista_competidores(self):
        self.__tela_competidor.mostra_dados(self.dados_lista_competidores())
        
    def excluir_competidor(self):
        id = self.__tela_competidor.seleciona_competidor(self.dados_lista_competidores())
        competidor = self.pega_competidor_por_id(id)

        if (competidor is not None):
            self.__competidor_dao.remove(competidor)

    def verifica_duplicidade_de_nome (self, nome):
        for competidor in self.__competidor_dao.get_all():
            if nome == competidor.nome:
                raise DuplicatedException(mensagem_personalizada='Este competidor já foi criado')

    def verifica_duplicidade_de_nick (self, nick):
        for competidor in self.__competidor_dao.get_all():
            if nick == competidor.nick:
                raise DuplicatedException(mensagem_personalizada='Já existe um competidor com esse apelido')

    def retornar (self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_competidor, 2: self.alterar_competidor, 3: self.excluir_competidor, 4: self.lista_competidores, 5: self.retornar}

        while True:
            lista_opcoes[self.__tela_competidor.tela_opcoes()]()