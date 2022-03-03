from limite.tela_abstrata import TelaAbstrata

class TelaSistema(TelaAbstrata):
    def tela_opcoes(self):
        
        print("----------- Sistema de competição -----------")
        print("Escolha...")
        print("1 - Registro Competidores")
<<<<<<< HEAD
        print("2 - Registro Organizadores")
        print("3 - Registro Competições")
        print("4 - Administrar Competições Existentes")
=======
        print("2 - Registro Competições")
        print("3 - Administrar Competições Existentes")
>>>>>>> 978e9269b9cd34b4c5e22058cd0323a01ba82c9d
        print("0 - Encerrar Sistema")

        while True:
            try:
                opcao = int(input("Escolha a opção: "))
<<<<<<< HEAD
                if opcao > 4 or opcao < 0:
                    raise ValueError
            except (KeyError, ValueError, Exception):
                print("\033[31mERRO! Digite um número de 0 à 4.\033[m")
=======
                if opcao > 3 or opcao < 0:
                    raise ValueError
            except (KeyError, ValueError, Exception):
                print("\033[31mERRO! Digite um número de 0 à 2.\033[m")
>>>>>>> 978e9269b9cd34b4c5e22058cd0323a01ba82c9d
                continue
            else:
                return opcao