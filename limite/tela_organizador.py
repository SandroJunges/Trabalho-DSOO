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
        
        window = sg.Window("Organizador", size=tamanho_janela2, element_justification="c", grab_anywhere=True, default_element_size=(40 , 1)).Layout(layout)
        
        button, values = window.read()
        window.close()
        return button
    
    def pega_dados(self):
        
        layout = [
            [sg.Image(logo2, size=(300, 300))],
            [sg.Text("Escreva os dados", font=fonte_titulo, size=(0, 1), text_color=cor_titulo, background_color=fundo_titulo)],
            [sg.Text("")],
            [sg.Text("Nome:", font=fonte_texto, size=tamanho_texto2), sg.InputText(key="nome")],
            [sg.Text("Senha:", font=fonte_texto, size=tamanho_texto2), sg.InputText(key="senha")],
            [sg.Text("")],
            [sg.Submit("Confirmar", font=fonte_texto, size=tamanho_texto2), sg.Cancel("Retornar", font=fonte_texto, size=tamanho_texto2)]
        ]

        window = sg.Window("Organizador", size=(700,700) , element_justification="l", grab_anywhere=True, default_element_size=(40 , 1)).Layout(layout)
        
        button, dados_organizador = window.read()
        window.close()
        if button == "Confirmar":
            return dados_organizador
       
    def mostra_dados(self, organizadores: list):
        organizadores = [
            [sg.Listbox(values=organizadores, font=fonte_texto, size=(60, 8), key='organizador')]
        ]

        layout = [
            [sg.Image(logo2, size=(300, 300))],
            [sg.Text('Listando organizadores', font=fonte_titulo, size=(0,1), text_color=cor_titulo, background_color=fundo_titulo)],
            [organizadores],
            [sg.Text('')],
            [sg.Button('Retornar', font=fonte_texto, size=tamanho_texto, key=1)]
        ]

        window = sg.Window('Listar Organizadores', size=tamanho_janela, element_justification="c", grab_anywhere=True).Layout(layout)
        button = window.Read()
        window.close()

    def seleciona_organizador(self, organizadores: list):
        organizadores = [
            [sg.Listbox(values=organizadores, font=fonte_texto, size=(60, 8), key='organizador')]
        ]

        layout = [
            [sg.Image(logo2, size=(300, 300))],
            [sg.Text('Listando organizadores', font=fonte_titulo, size=(0,1), text_color=cor_titulo, background_color=fundo_titulo)],
            [organizadores],
            [sg.Text('')],
            [sg.Submit('Confirmar', font=fonte_texto, size=tamanho_texto), sg.Cancel('Cancelar e retornar', font=fonte_texto, size=tamanho_texto)]
        ]

        window = sg.Window('Selecionar Organizador', size=tamanho_janela, element_justification="c", grab_anywhere=True).Layout(layout)
        button, organizador = window.Read()
        window.close()
        if button == 'Confirmar':
            id = (organizador['organizador'][0].split())[1]
            id = int(id)
            return id
        return
    
    def mostra_mensagem(self, msg):
        print(msg)