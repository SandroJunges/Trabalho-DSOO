from limite.tela_abstrata import TelaAbstrata

class TelaPartida(TelaAbstrata):
    
    def tela_opcoes(self):

        print("----------- Partida -----------")
        print("Escolha sua opção")
        print("1 - Competidor")
        print("2 - Organizador")
        print("3 - Partida")
        print("4 - Competição")
        print("0 - Finalizar Sistema")
        
        opcao = int(input("Escolha a opção: "))
        return opcao

    def mostra_mensagem(self):
        pass

    def mostra_dados(self):
        pass

    def pega_dados(self):
        pass