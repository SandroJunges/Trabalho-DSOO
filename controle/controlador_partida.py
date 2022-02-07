from limite.tela_partida import TelaPartida

class ControladorPartida():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_partida = TelaPartida()
        self.__partidas = []
        
    def retornar (self):
        self.__controlador_sistema.abre_tela()

    def pega_partida_por_numero(self, numero: int):
        for partida in self.__partidas:
            if (partida.numero == numero):
                return partida
                
        return None
    
    def relatorio(self):
        ###mostrar o resultado ou data das partidas###
        pass

    def abre_tela(self):
        lista_opcoes = {1: self.relatorio, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_partida.tela_opcoes()]()