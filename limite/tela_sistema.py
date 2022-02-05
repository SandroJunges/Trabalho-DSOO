from limite.tela_abstrata import TelaAbstrata

class TelaSistema(TelaAbstrata):
    def tela_inicial(self):
        
        print("----------- Sistema de competição -----------")
        print("Como você deseja entrar?")
        print("1 - Competidor")
        print("2 - Administrador")
        print("0 - Finalizar Sistema")
        
        while True:
            try:
                opcao = int(input("Escolha a opção: "))
                if opcao > 2 or opcao < 0:
                    raise ValueError
            except (KeyError, ValueError, Exception):
                print("\033[31mERRO! Digite um número de 0 à 2.\033[m")
                continue
            else:
                return opcao

    def tela_opcoes(self):
        
        print("----------- Sistema de competição -----------")
        print("Cadastrar torneio")
        print("1 - Cadastrar Competidor")
        print("2 - Cadastrar Organizador")
        print("3 - Cadastrar Partida")
        print("4 - Cadastrar/Editar Campeonato")
        print("0 - Retornar")

        while True:
            try:
                opcao = int(input("Escolha a opção: "))
                if opcao > 4 or opcao < 0:
                    raise ValueError
            except (KeyError, ValueError, Exception):
                print("\033[31mERRO! Digite um número de 0 à 2.\033[m")
                continue
            else:
                return opcao

    def tela_visualizacao(self):
        
        print("----------- Sistema de competição -----------")
        print("Cadastrar torneio")
        print("1 - Visualizar campeonatos")
        print("2 - Visualizar partidas")
        print("0 - Retornar")

        while True:
            try:
                opcao = int(input("Escolha a opção: "))
                if opcao > 2 or opcao < 0:
                    raise ValueError
            except (KeyError, ValueError, Exception):
                print("\033[31mERRO! Digite um número de 0 à 2.\033[m")
                continue
            else:
                return opcao