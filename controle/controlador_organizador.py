from limite.tela_organizador import TelaOrganizador
from entidade.organizador import Organizador

class ControladorOrganizador():

    def __init__(self, controlador_sistema):
        self.__organizadores = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_organizador = TelaOrganizador()
    
    def pega_organizador_por_nome(self, nome: str):
        for organizador in self.__organizadores:
            if (organizador.nome == nome):
                return organizador
                
        return None

    def incluir_organizador(self):
        dados_organizador = self.__tela_organizador.pega_dados()
        organizador = Organizador(dados_organizador["nome"], dados_organizador["senha"])
        self.__organizadores.append(organizador)
    
    def alterar_organizador(self):
        self.lista_organizadores()
        nome_organizador = self.__tela_organizador.seleciona_organizador()
        organizador = self.pega_organizador_por_nome(nome_organizador)

        if (organizador is not None):
            novos_dados_organizador = self.__tela_organizador.pega_dados()
            organizador.nome = novos_dados_organizador["nome"]
            organizador.senha = novos_dados_organizador["senha"]
            self.lista_organizadores()

        else:
            self.__tela_organizador.mostra_mensagem("ATENÇÃO: organizador não existente!")
    
    def lista_organizadores(self):
        for organizador in self.__organizadores:
            self.__tela_organizador.mostra_dados({"nome": organizador.nome, "senha": organizador.senha})

    def excluir_organizador(self):
        self.lista_organizadores()
        nome_organizador = self.__tela_organizador.seleciona_organizador()
        organizador = self.pega_organizador_por_nome(nome_organizador)

        if (organizador is not None):
            self.__organizadores.remove(organizador)
            self.lista_organizadores()

        else:
            self.__tela_organizador.mostra_mensagem("ATENÇÃO: organizador não existente!")

    def retornar (self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_organizador, 2: self.alterar_organizador, 3: self.lista_organizadores, 4: self.excluir_organizador, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_organizador.tela_opcoes()]()