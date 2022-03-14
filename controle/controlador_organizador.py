from limite.tela_organizador import TelaOrganizador
from entidade.organizador import Organizador
from persistencia.organizador_dao import OrganizadorDAO
from excecoes.empty_field import EmptyFieldError
from excecoes.duplicated_exception import DuplicatedException

class ControladorOrganizador():

    def __init__(self, controlador_sistema):
        self.__organizador_dao = OrganizadorDAO()
        self.__controlador_sistema = controlador_sistema
        self.__tela_organizador = TelaOrganizador()
        self.__id_organizador = 0

    def incluir_organizador(self):
        dados_organizador = self.__tela_organizador.pega_dados()
        if (dados_organizador == None):
            return

        try:
            if dados_organizador['nome'] == "" or dados_organizador['senha'] == "":
                raise EmptyFieldError()
        except EmptyFieldError as e:
            return self.__tela_organizador.mostra_mensagem(e.mensagem)
        try:
            self.verifica_duplicidade_de_nome(dados_organizador['nome'])
        except DuplicatedException as e:
            return self.__tela_organizador.mostra_mensagem(str(e))

        else:
            id = 0
            for organizador in self.__organizador_dao.get_all():
                if organizador.id_organizador > id:
                    id = organizador.id_organizador
            self.__id_organizador = id + 1
            organizador = Organizador(dados_organizador["nome"], dados_organizador["senha"], self.__id_organizador)
            self.__organizador_dao.add(organizador)
            self.__tela_organizador.mostra_mensagem("Organizador cadastrado!")
    
    def pega_organizador_por_id(self, id):
        if id == "" or id ==  None:
            return None

        for organizador in self.__organizador_dao.get_all():
            if organizador.id_organizador == int(id):
                return organizador
        return None

    def dados_lista_organizadores(self):
        return [f'ID: {organizador.id_organizador}  Nome: {organizador.nome}' for organizador in self.__organizador_dao.get_all()]

    def alterar_organizador(self):
        id = self.__tela_organizador.seleciona_organizador(self.dados_lista_organizadores())
        organizador = self.pega_organizador_por_id(id)

        if(organizador is not None):
            novos_dados_organizador = self.__tela_organizador.pega_dados()
            try:
                if novos_dados_organizador['nome'] == "" or novos_dados_organizador['senha'] == "":
                    raise EmptyFieldError()
            except EmptyFieldError as e:
                return self.__tela_organizador.mostra_mensagem(e.mensagem)
            try:
                self.verifica_duplicidade_de_nome(novos_dados_organizador['nome'])
            except DuplicatedException as e:
                return self.__tela_organizador.mostra_mensagem(str(e))
            if novos_dados_organizador != None:
                organizador.nome = novos_dados_organizador["nome"]
                organizador.senha = novos_dados_organizador["senha"]
                self.__organizador_dao.add(organizador)
                self.__tela_organizador.mostra_mensagem("Organizador alterado!")
                return
            return
    
    def lista_organizadores(self):
        self.__tela_organizador.mostra_dados(self.dados_lista_organizadores())

    def excluir_organizador(self):
        id = self.__tela_organizador.seleciona_organizador(self.dados_lista_organizadores())
        organizador = self.pega_organizador_por_id(id)

        if (organizador is not None):
            self.__tela_organizador.mostra_mensagem("Organizador excluído!")
            self.__organizador_dao.remove(organizador)

    def verifica_duplicidade_de_nome (self, nome):
        for organizador in self.__organizador_dao.get_all():
            if nome == organizador.nome:
                raise DuplicatedException(mensagem_personalizada='Este organizador já foi criado!')

    def retornar (self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_organizador, 2: self.alterar_organizador, 3: self.excluir_organizador, 4: self.lista_organizadores, 5: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_organizador.tela_opcoes()]()