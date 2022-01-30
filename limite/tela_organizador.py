from limite.tela_abstrata import TelaAbstrata

class TelaOrganizador(TelaAbstrata):
    def tela_opcoes(self):
        print("-------- Organizadores ----------")
        print("Escolha a opcao")
        print("1 - Incluir Organizador")
        print("2 - Alterar Organizador")
        print("3 - Listar Organizador")
        print("4 - Excluir Organizador")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def pega_dados(self):
        print("-------- DADOS ORGANIZADOR --------")
        nome = input("Nome: ")
        senha = input("Senha: ")

        return {"nome": nome, "senha": senha}

    def mostra_dados(self, dados_organizador):
        print("Nome do organizador: ",  dados_organizador["nome"])
        print("Senha do organizador: ",  dados_organizador["senha"])
        print("\n")

    def seleciona_organizador(self):
        nome = input("Nome do organizador que deseja selecionar: ")
        return nome
    
    def mostra_mensagem(self, msg):
        print(msg)