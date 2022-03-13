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
            [sg.Button("Administrar Competição", font=fonte_texto, size=tamanho_texto, key=3)],
            [sg.Button("Relatório Competições/Ganhadores", font=fonte_texto, size=tamanho_texto, key=4)],
            [sg.Button("Retornar", font=fonte_texto, size=tamanho_texto, key=5)]
        ]
        
        window = sg.Window("Competição", size=tamanho_janela2, element_justification="c", grab_anywhere=True, default_element_size=(40 , 1)).Layout(layout)
        
        button, values = window.read()
        window.close()
        return button
    
    def pega_dados(self, organizadores : list):
        list_organizador = [
            [sg.Listbox(organizadores, key="organizador")]
        ]
        layout = [
            [sg.Image(logo2, size=(300, 300))],
            [sg.Text("Escreva os dados", font=fonte_titulo, size=(0, 1), text_color=cor_titulo, background_color=fundo_titulo)],
            [sg.Text("")],
            [sg.Text("Nome:", font=fonte_texto, size=tamanho_texto2), sg.InputText(key="nome_torneio")],
            [sg.Text("Esporte:", font=fonte_texto, size=tamanho_texto2), sg.InputText(key="esporte")],
            [sg.Text('Quantos participantes para o mata-mata?', font=fonte_texto, size=tamanho_texto2), sg.InputCombo((2,4,8,16,32),default_value='selecione', size=(9,1),key = 'formato')],
            [sg.Text("Organizador:", font=fonte_texto, size=tamanho_texto2)], [list_organizador],
            [sg.Text("")],
            [sg.Submit("Confirmar", font=fonte_texto, size=tamanho_texto2), sg.Cancel("Retornar", font=fonte_texto, size=tamanho_texto2)]
        ]

        window = sg.Window("Competicao", size=tamanho_janela2 , element_justification="l", grab_anywhere=True, default_element_size=(40 , 1)).Layout(layout)
        
        button, dados_competidor = window.read()
        window.close()
        if button == "Confirmar":
            return dados_competidor
            
    def mostra_dados(self, competicoes: list):
        competicoes = [
            [sg.Listbox(values=competicoes, font=fonte_texto, size=(60, 8), key='competicao')]
        ]

        layout = [
            [sg.Image(logo2, size=(300, 300))],
            [sg.Text('Listando competicoes', font=fonte_titulo, size=(0,1), text_color=cor_titulo, background_color=fundo_titulo)],
            [competicoes],
            [sg.Text('')],
            [sg.Button('Retornar', font=fonte_texto, size=tamanho_texto, key=1)]
        ]

        window = sg.Window('Listar Competicoes', size=tamanho_janela, element_justification="c", grab_anywhere=True).Layout(layout)
        button = window.Read()
        window.close()


    def seleciona_competicao(self, competicoes: list):
        competicoes = [
            [sg.Listbox(values=competicoes, font=fonte_texto, size=(60, 8), key='competicao')]
        ]

        layout = [
            [sg.Image(logo2, size=(300, 300))],
            [sg.Text('Selecione a competicao', font=fonte_titulo, size=(0,1), text_color=cor_titulo, background_color=fundo_titulo)],
            [competicoes],
            [sg.Text('')],
            [sg.Submit('Confirmar', font=fonte_texto, size=tamanho_texto), sg.Cancel('Cancelar e retornar', font=fonte_texto, size=tamanho_texto)]
        ]

        window = sg.Window('Selecionar Competicao', size=tamanho_janela, element_justification="c", grab_anywhere=True).Layout(layout)
        button, competicao = window.Read()
        window.close()
        if button == 'Confirmar':
            id = (competicao['competicao'][0].split())[1]
            id = int(id)
            return id
        return
    
    def partidas(self, lista_participantes: list):
        opcoes_participantes = [
            [sg.Listbox(lista_participantes)]
        ]
        teste = [
            [sg.Listbox(lista_participantes)]
        ]
        layout = [
            [sg.Image(logo2, size=(300, 300))],
            [sg.Text('Partida', font=fonte_titulo, size=(0,1), text_color=cor_titulo, background_color=fundo_titulo)],
            [sg.Text('Selecione os participantes', font=fonte_titulo, size=(0,1), text_color=cor_titulo, background_color=fundo_titulo)],
            [opcoes_participantes], [sg.Text('X', font=fonte_titulo, size=(0,1), text_color=cor_titulo, background_color=fundo_titulo)], [teste],
            [sg.Text('')],
            [sg.Submit('Confirmar', font=fonte_texto, size=tamanho_texto), sg.Cancel('Cancelar e retornar', font=fonte_texto, size=tamanho_texto)]
        ]

        window = sg.Window('Partidas', size=tamanho_janela, element_justification="c", grab_anywhere=True).Layout(layout)
        button, dados_partida = window.Read()
        window.close()
        if button == 'Confirmar':
            return dados_partida

        
    
    def mostra_mensagem(self, msg):
        print(msg)