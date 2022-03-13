from limite.tela_competidor import TelaCompetidor
from entidade.competidor import Competidor

class ControladorCompetidor():

    def __init__(self, controlador_sistema):
        self.__competidores = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_competidor = TelaCompetidor()
        self.__id_competidor = 0
    

    def lista_competidores(self):
        return self.__competidores

    def incluir_competidor(self):
        dados_competidor = self.__tela_competidor.pega_dados()
        if (dados_competidor == None):
            return
        else:
            id = 0
            for competidor in self.__competidores:
                if competidor.id_competidor > id:
                    id = competidor.id_competidor
            self.__id_competidor = id + 1
            competidor = Competidor(dados_competidor["nome"], dados_competidor["idade"], dados_competidor["nick"], self.__id_competidor)
            self.__competidores.append(competidor)

    def pega_competidor_por_id(self, id):
        if id == "" or id ==  None:
            return None

        for competidor in self.__competidores:
            if competidor.id_competidor == int(id):
                return competidor
        return None

    def dados_lista_competidores(self):
        return [f'ID: {competidor.id_competidor}  Nome: {competidor.nome} | Idade: {competidor.idade} | Nick: {competidor.nick}' for competidor in self.__competidores]
    
    def dados_nome_competidores(self):
        return [competidor.nome for competidor in self.__competidores]
        
    def alterar_competidor(self):
        id = self.__tela_competidor.seleciona_competidor(self.dados_lista_competidores())
        competidor = self.pega_competidor_por_id(id)

        if(competidor is not None):
            novos_dados_competidor = self.__tela_competidor.pega_dados()
            if novos_dados_competidor != None:
                competidor.nome = novos_dados_competidor["nome"]
                competidor.idade = novos_dados_competidor["idade"]
                competidor.nick = novos_dados_competidor["nick"]
                return
            return
    
    def lista_competidores(self):
        self.__tela_competidor.mostra_dados(self.dados_lista_competidores())
        

#San depois de tu criar o DAO supostamente vai funcionar esse excluir
    def excluir_competidor(self):
        competidor = self.__tela_competidor.seleciona_competidor(self.dados_lista_competidores())

        if (competidor is not None):
            self.__competidores_dao.remove(id)

    def retornar (self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_competidor, 2: self.alterar_competidor, 3: self.excluir_competidor, 4: self.lista_competidores, 5: self.retornar}

        while True:
            lista_opcoes[self.__tela_competidor.tela_opcoes()]()