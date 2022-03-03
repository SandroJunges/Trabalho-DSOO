from limite.tela_competidor import TelaCompetidor
from entidade.competidor import Competidor

class ControladorCompetidor():

    def __init__(self, controlador_sistema):
        self.__competidores = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_competidor = TelaCompetidor()
    
    def pega_competidor_por_nome(self, nome: str):
        for competidor in self.__competidores:
            if (competidor.nome == nome):
                return competidor
                
        return None
    
<<<<<<< HEAD
=======
    def lista_competidores(self):
        for competidor in ControladorCompetidor.__competidores:
            return competidor
    
>>>>>>> 978e9269b9cd34b4c5e22058cd0323a01ba82c9d
    def incluir_competidor(self):
        dados_competidor = self.__tela_competidor.pega_dados()
        competidor = Competidor(dados_competidor["nome"], dados_competidor["idade"], dados_competidor["nick"])
        self.__competidores.append(competidor)

        
    def alterar_competidor(self):
        self.lista_competidores()
        nome_competidor = self.__tela_competidor.seleciona_competidor()
        competidor = self.pega_competidor_por_nome(nome_competidor)

        if (competidor is not None):
            novos_dados_competidor = self.__tela_competidor.pega_dados()
            competidor.nome = novos_dados_competidor["nome"]
            competidor.idade = novos_dados_competidor["idade"]
            competidor.nick = novos_dados_competidor["nick"]
            self.lista_competidores()

        else:
            self.__tela_competidor.mostra_mensagem("\033[31mATENÇÃO: Competidor não existente!\033[m")
    
    def lista_competidores(self):
        for competidor in self.__competidores:
            self.__tela_competidor.mostra_dados({"nome": competidor.nome, "idade": competidor.idade, "nick": competidor.nick})

    def excluir_competidor(self):
        self.lista_competidores()
        nome_competidor = self.__tela_competidor.seleciona_competidor()
        competidor = self.pega_competidor_por_nome(nome_competidor)

        if (competidor is not None):
            self.__competidores.remove(competidor)
            self.lista_competidores()

        else:
            self.__tela_competidor.mostra_mensagem("\033[31mATENÇÃO: Competidor não existente!\033[m")

    def retornar (self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_competidor, 2: self.alterar_competidor, 3: self.lista_competidores, 4: self.excluir_competidor, 0: self.retornar}

        while True:
            lista_opcoes[self.__tela_competidor.tela_opcoes()]()