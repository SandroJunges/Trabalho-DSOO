from limite.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg
from limite.temas import *

class TelaCompeticao(TelaAbstrata):

    def tela_opcoes(self):
        sg.theme(tema)

        layout = [
            [sg.Image(logo2, size=(300, 300))],
            [sg.Text("Competição", font=fonte_titulo, size=(0, 1), text_color=cor_titulo, background_color=fundo_titulo)],
            [sg.Text("O que deseja fazer?", font=fonte_titulo, size=(0, 1), text_color=cor_titulo, background_color=fundo_titulo)],
            [sg.Text("")],
            [sg.Button("Cadastrar Competição", font=fonte_texto, size=tamanho_texto, key=1)],
            [sg.Button("Listar Competições", font=fonte_texto, size=tamanho_texto, key=2)],
            [sg.Button("Excluir Competição", font=fonte_texto, size=tamanho_texto, key=3)],
            [sg.Button("Administrar Competição", font=fonte_texto, size=tamanho_texto, key=4)],
            [sg.Button("Relatório Competições/Ganhadores", font=fonte_texto, size=tamanho_texto, key=5)],
            [sg.Button("Retornar", font=fonte_texto, size=tamanho_texto, key=0)]
        ]
        
        window = sg.Window("Competição", size=tamanho_janela2, element_justification="c", grab_anywhere=True, default_element_size=(40 , 1)).Layout(layout)
        
        button, values = window.read()
        window.close()
        return button
    
    def tela_administrar(self):

        print("----------- Competicao -----------")
        print("Escolha sua opção")
        print("1 - Visualizar Competição")
        print("2 - Registar Resultados")
        print("3 - Alterar Partidas")
        print("0 - Retornar")

        while True:
            try:
                opcao = int(input("Escolha a opção: "))
                if opcao > 3 or opcao < 0:
                    raise ValueError
            except (KeyError, ValueError, Exception):
                print("\033[31mERRO! Digite um número de 0 à 3.\033[m")
                continue
            else:
                return opcao

    def pega_dados(self):
        print("-------- DADOS COMPETIÇÃO --------")
        while True:
            try:
                nome = input("Nome da competição: ")
                esporte = input("Esporte: ")
                formato = input("Mata-Mata ou Liga: ").lower()
                if nome == "" or esporte == "" or formato not in ["mata-mata", "liga"]:
                    raise Exception
            except Exception:
                print("\033[31mERRO: Alguma das informações digitadas não é válida.\033[m")
                continue
            else:
                return {"nome_torneio": nome, "esporte": esporte, "formato": formato}

    def quer_competidor(Self):
        print("-------- DADOS COMPETIÇÃO --------")
        while True:
            try:
                continuar = input("Quer adicionar mais um competidor na competição? S/N").upper()
                if continuar not in ["S","N"]:
                    raise Exception
            except Exception:
                    print("Digite S ou N")
                    continue
            if continuar == "S":
                    return True
            else:
                return False
                

    def pega_participantes(self):
        print("-------- DADOS COMPETIÇÃO --------")
        participante = input("Qual participante?")

        return participante
        
            
    def mostra_dados(self, dados_competicao, dados_competidores, dados_partidas):
        print("Nome da competição: ",  dados_competicao["nome_torneio"])
        print("Esporte da competição: ",  dados_competicao["esporte"])
        print("Formato da competição: ",  dados_competicao["formato"])
        print("Participantes: ", dados_competidores)
        print("Partidas: ", dados_partidas)
        print("\n")

    def seleciona_competicao(self):
        nome = input("Nome da competição que deseja selecionar: ")
        return nome
    
    def mostra_mensagem(self, msg):
        print(msg)