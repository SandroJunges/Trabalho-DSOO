from limite.tela_abstrata import TelaAbstrata

class TelaPartida(TelaAbstrata):
    
    def tela_opcoes(self):

        print("----------- Partida -----------")
        print("Escolha sua opção")
        print("1 - Relatório")
        print("0 - Retornar")
        
        while True:
            try:
                opcao = int(input("Escolha a opção: "))
            except (KeyError, ValueError, Exception):
                print("\033[31mERRO! Digite um número válido.\033[m")
                continue
            else:
                return opcao

    def mostra_mensagem(self, msg):
        print(msg)

    def mostra_dados(self):
        pass

    def pega_dados(self):
        pass