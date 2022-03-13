from limite.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg
from limite.temas import *

class TelaSistema(TelaAbstrata):
    def tela_opcoes(self):
        sg.theme(tema)
        
        layout = [
            [sg.Image(logo, size=(300, 300))],
            [sg.Text("Bem-vindo ao knockouter", font=fonte_titulo, size=(0,1), text_color=cor_titulo, background_color=fundo_titulo)],
            [sg.Text("O que deseja fazer?", font=fonte_titulo, size=(0,1), text_color=cor_titulo, background_color=fundo_titulo)],
            [sg.Text("")],
            [sg.Button("Competidor", font=fonte_texto, size=tamanho_texto)],
            [sg.Button("Organizador", font=fonte_texto, size=tamanho_texto)],
            [sg.Button("Competição", font=fonte_texto, size=tamanho_texto)],
            [sg.Button("Encerrar Sistema", font=fonte_texto, size=tamanho_texto)]
        ]

        window = sg.Window("Tela Inicial", size=(tamanho_janela), element_justification="c", grab_anywhere=True, default_element_size=(40 , 1)).Layout(layout)
        button = window.read()
        opcao = {"Competidor": 1, "Organizador": 2, "Competição": 3, "Encerrar Sistema": 0}
        window.close()
        return opcao[button[0]]

