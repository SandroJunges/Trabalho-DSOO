from limite.tela_abstrata import TelaAbstrata

class TelaSistema(TelaAbstrata):
    def tela_opcoes(self):
        
        print("----------- Sistema de competição -----------")
        print("Escolha...")
        print("1 - Registro Competidores")
        print("2 - Registro Organizadores")
        print("3 - Registro Competições")
        print("4 - Administrar Competições Existentes")
        print("0 - Encerrar Sistema")

        while True:
            try:
                opcao = int(input("Escolha a opção: "))
                if opcao > 4 or opcao < 0:
                    raise ValueError
            except (KeyError, ValueError, Exception):
                print("\033[31mERRO! Digite um número de 0 à 4.\033[m")
                continue
            else:
                return opcao