from asyncio import windows_events
from limite.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg
from limite.temas import *

class TelaCompetidor(TelaAbstrata):

    def tela_opcoes(self):

        sg.theme(tema)

        layout = [
            [sg.Image(logo2, size=(300, 300))],
            [sg.Text("Participante", font=fonte_titulo, size=(0, 1), text_color=cor_titulo, background_color=fundo_titulo)],
            [sg.Text("O que deseja fazer?", font=fonte_titulo, size=(0, 1), text_color=cor_titulo, background_color=fundo_titulo)],
            [sg.Text("")],
            [sg.Button("Cadastrar Participante", font=fonte_texto, size=tamanho_texto, key=1)],
            [sg.Button("Editar Participante", font=fonte_texto, size=tamanho_texto, key=2)],
            [sg.Button("Excluir Participante", font=fonte_texto, size=tamanho_texto, key=3)],
            [sg.Button("Listar Participantes", font=fonte_texto, size=tamanho_texto, key=4)],
            [sg.Button("Retornar", font=fonte_texto, size=tamanho_texto, key=5)]
        ]
        
        window = sg.Window("Participante", size=tamanho_janela2, element_justification="c", grab_anywhere=True, default_element_size=(40 , 1)).Layout(layout)
        
        button, values = window.read()
        window.close()
        return button

    def pega_dados(self):

        layout = [
            [sg.Image(logo2, size=(300, 300))],
            [sg.Text("Escreva os dados", font=fonte_titulo, size=(0, 1), text_color=cor_titulo, background_color=fundo_titulo)],
            [sg.Text("")],
            [sg.Text("Nome:", font=fonte_texto, size=tamanho_texto2), sg.InputText(key="nome")],
            [sg.Text("Idade:", font=fonte_texto, size=tamanho_texto2), sg.Spin([i for i in range(1,100)], initial_value=50, key = 'idade')],
            [sg.Text("Apelido:", font=fonte_texto, size=tamanho_texto2), sg.InputText(key="nick")],
            [sg.Text("")],
            [sg.Submit("Confirmar", font=fonte_texto, size=tamanho_texto2), sg.Cancel("Retornar", font=fonte_texto, size=tamanho_texto2)]
        ]

        window = sg.Window("Participante", size=tamanho_janela2 , element_justification="l", grab_anywhere=True, default_element_size=(40 , 1)).Layout(layout)
        
        button, dados_competidor = window.read()
        window.close()
        if button == "Confirmar":
            return dados_competidor

    def mostra_dados(self, competidores: list):
        competidores = [
            [sg.Listbox(values=competidores, font=fonte_texto, size=(60, 8), key='competidor')]
        ]

        layout = [
            [sg.Image(logo2, size=(300, 300))],
            [sg.Text('Listando competidores', font=fonte_titulo, size=(0,1), text_color=cor_titulo, background_color=fundo_titulo)],
            [competidores],
            [sg.Text('')],
            [sg.Button('Retornar', font=fonte_texto, size=tamanho_texto, key=1)]
        ]

        window = sg.Window('Listar Competidores', size=tamanho_janela, element_justification="c", grab_anywhere=True).Layout(layout)
        button = window.Read()
        window.close()

    

    def seleciona_competidor(self, competidores: list):
        competidores = [
            [sg.Listbox(values=competidores, font=fonte_texto, size=(60, 8), key='competidor')]
        ]

        layout = [
            [sg.Image(logo2, size=(300, 300))],
            [sg.Text('Selecione o competidor', font=fonte_titulo, size=(0,1), text_color=cor_titulo, background_color=fundo_titulo)],
            [competidores],
            [sg.Text('')],
            [sg.Submit('Confirmar', font=fonte_texto, size=tamanho_texto), sg.Cancel('Cancelar e retornar', font=fonte_texto, size=tamanho_texto)]
        ]

        window = sg.Window('Selecionar Competidor', size=tamanho_janela, element_justification="c", grab_anywhere=True).Layout(layout)
        button, competidor = window.Read()
        window.close()
        if button == 'Confirmar':
            id = (competidor['competidor'][0].split())[1]
            id = int(id)
            return id
        return
        
    
    def mostra_mensagem(self, msg):
        sg.theme(tema)
        layout = [
            [sg.Text(msg, font=fonte_texto, size=tamanho_texto2, justification="c")],
            [sg.Cancel("Ok", font=fonte_texto, size= tamanho_texto2)]
        ]

        window = sg.Window('Aviso!', size=tamanho_aviso, element_justification="c", grab_anywhere=True).Layout(layout)
        button, msg = window.read()
        window.close()
        print(msg)