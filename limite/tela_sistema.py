from limite.tela_abstrata import TelaAbstrata

class TelaSistema(TelaAbstrata):
    
    def tela_opcoes(self):
        print("----------- Sistema de competição -----------")
        print("Escolha sua opção")
        print("1 - Competidor")
        print("2 - Organizador")
        print("3 - Partida")
        print("4 - Competição")
        print("0 - Finalizar Sistema")
        opcao = int(input("Escolha a opção: "))
        return opcao