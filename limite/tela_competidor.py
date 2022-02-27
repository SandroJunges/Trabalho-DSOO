from limite.tela_abstrata import TelaAbstrata

class TelaCompetidor(TelaAbstrata):

    def tela_opcoes(self):
        
        print("-------- Competidores ----------")
        print("Escolha a opcao")
        print("1 - Incluir Competidor")
        print("2 - Alterar Competidor")
        print("3 - Listar Competidores")
        print("4 - Excluir Competidor")
        print("0 - Retornar")

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

    def pega_dados(self):
        print("-------- DADOS COMPETIDOR --------")
        while True:
            try:
                nome = input("Nome: ")
                idade = input("Idade: ")
                nick = input("Apelido: ")
                if nome == "" or idade == "" or nick == "":
                    raise Exception
            except Exception:
                print("\033[31mERRO: Alguma das informações digitadas não é válida.\033[m")
                continue
            else:
                return {"nome": nome, "idade": idade, "nick": nick}

    def mostra_dados(self, dados_competidor):
        print("Nome do competidor: ",  dados_competidor["nome"])
        print("Idade do competidor: ",  dados_competidor["idade"])
        print("Apelido do competidor: ",  dados_competidor["nick"])

    def seleciona_competidor(self):
        nome = input("Nome do competidor que deseja selecionar: ")
        return nome
    
    def mostra_mensagem(self, msg):
        print(msg)