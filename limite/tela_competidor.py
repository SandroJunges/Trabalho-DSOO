from limite.tela_abstrata import TelaAbstrata

class TelaCompetidor(TelaAbstrata):
    def tela_opcoes(self):
        print("-------- Competidores ----------")
        print("Escolha a opcao")
        print("1 - Incluir Competidor")
        print("2 - Alterar Competidor")
        print("3 - Listar Competidor")
        print("4 - Excluir Competidor")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def pega_dados(self):
        print("-------- DADOS COMPETIDOR --------")
        nome = input("Nome: ")
        email = input("E-mail: ")

        return {"nome": nome, "email": email}

    def mostra_dados(self, dados_competidor):
        print("Nome do competidor: ",  dados_competidor["nome"])
        print("E-mail do competidor: ",  dados_competidor["email"])
        print("\n")

    def seleciona_competidor(self):
        nome = input("Nome do competidor que deseja selecionar: ")
        return nome
    
    def mostra_mensagem(self, msg):
        print(msg)