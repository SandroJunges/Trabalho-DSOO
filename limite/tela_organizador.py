from limite.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg
from limite.temas import *

class TelaOrganizador(TelaAbstrata):

    def tela_opcoes(self):

        sg.theme(tema)

        layout = [
            [sg.Image(logo2, size=(300, 300))],
            [sg.Text("Organizador", font=fonte_titulo, size=(0, 1), text_color=cor_titulo, background_color=fundo_titulo)],
            [sg.Text("O que deseja fazer?", font=fonte_titulo, size=(0, 1), text_color=cor_titulo, background_color=fundo_titulo)],
            [sg.Text("")],
            [sg.Button("Cadastrar Organizador", font=fonte_texto, size=tamanho_texto, key=1)],
            [sg.Button("Editar Organizador", font=fonte_texto, size=tamanho_texto, key=2)],
            [sg.Button("Excluir Organizador", font=fonte_texto, size=tamanho_texto, key=3)],
            [sg.Button("Listar Organizadores", font=fonte_texto, size=tamanho_texto, key=4)],
            [sg.Button("Retornar", font=fonte_texto, size=tamanho_texto, key=5)]
        ]
        
        window = sg.Window("Participante", size=tamanho_janela2, element_justification="c", grab_anywhere=True, default_element_size=(40 , 1)).Layout(layout)
        
        button, values = window.read()
        window.close()
        return button

        print("-------- Organizadores ----------")
        print("Escolha a opcao")
        print("1 - Cadastrar Organizador")
        print("2 - Alterar Organizador")
        print("3 - Listar Organizador")
        print("4 - Excluir Organizador")
        print("0 - Retornar")

    def pega_dados(self):
        print("-------- DADOS ORGANIZADOR --------")
        while True:
            try:
                nome = input("Nome: ")
                senha = input("Senha: ")
                if nome == "" or senha == "":
                    raise Exception
            except Exception:
                print("\033[31mERRO: Alguma das informações digitadas não é válida.\033[m")
                continue
            else:
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