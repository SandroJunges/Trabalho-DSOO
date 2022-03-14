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
            [sg.Button("Excluir Competição", font=fonte_texto, size=tamanho_texto, key=2)],
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

    def seleciona_competicao(self, competicoes: list):
        competicoes = [
            [sg.Listbox(values=competicoes, font=fonte_texto, size=(80, 8), key='competicao')]
        ]

        layout = [
            [sg.Image(logo2, size=(300, 300))],
            [sg.Text('Selecione a competicao', font=fonte_titulo, size=(0,1), text_color=cor_titulo, background_color=fundo_titulo)],
            [competicoes],
            [sg.Text('')],
            [sg.Submit('Confirmar', font=fonte_texto, size=tamanho_texto), sg.Cancel('Cancelar e retornar', font=fonte_texto, size=tamanho_texto)]
        ]

        window = sg.Window('Selecionar Competicao', size=(900,900), element_justification="c", grab_anywhere=True).Layout(layout)
        button, competicao = window.Read()
        window.close()
        if button == 'Confirmar':
            id = (competicao['competicao'][0].split())[1]
            id = int(id)
            return id
        return
    
    def pega_participantes(self, competidores : list):
        competidores = [
            [sg.Listbox(values=competidores, font=fonte_texto, size=(80, 8), key='competidor')]
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
    
    def partidas(self, n_partida,rodada, lista_participantes: list):
        n_partida = n_partida
        rodada = rodada
        opcao_participante1 = [
            [sg.Listbox(lista_participantes, enable_events=True, key="participante1")]
        ]
        opcao_participante2 = [
            [sg.Listbox(lista_participantes, enable_events=True, key='participante2')]
        ]
        layout = [
            [sg.Image(logo2, size=(300, 300))],
            [sg.Text('Partida', font=fonte_texto, size=(0,1), text_color=cor_titulo, background_color=fundo_titulo), sg.Text(n_partida, font=fonte_texto, size=(0,1), text_color=cor_titulo, background_color=fundo_titulo)],
            [sg.Text('Rodada de', font=fonte_texto, size=(0,1), text_color=cor_titulo, background_color=fundo_titulo), sg.Text(rodada , font=fonte_texto, size=(0,1), text_color=cor_titulo, background_color=fundo_titulo), sg.Text('participantes' , font=fonte_texto, size=(0,1), text_color=cor_titulo, background_color=fundo_titulo)],
            [sg.Text('Selecione os participantes', font=fonte_titulo, size=(0,1), text_color=cor_titulo, background_color=fundo_titulo)],
            [opcao_participante1], [sg.Text('X', font=fonte_titulo, size=(0,1), text_color=cor_titulo, background_color=fundo_titulo)], [opcao_participante2],
            [(sg.Button('Participante 1 ganhou', font=fonte_texto, size=tamanho_texto2)), sg.Button('Participante 2 ganhou', font=fonte_texto, size=tamanho_texto2)],
            [sg.Text('')],
            [sg.Exit('Cancelar e retornar', font=fonte_texto, size=tamanho_texto, key="Exit")]
        ]

        window = sg.Window('Partidas', size=(900,900), element_justification="c", grab_anywhere=True).Layout(layout)
        while True:
            event, values = window.read()
            if event is None or event == 'Exit':
                break
            if event == 'Participante 1 ganhou':
                return values['participante2']
            if event == 'Participante 2 ganhou':
                return values['participante1']
        window.close()

    def ganhador(self, ganhador : list):
        vencedor = ganhador[0]
        layout = [
            [sg.Image(logo, size=(300, 300))],
            [sg.Text('O VENCEDOR É', font=fonte_titulo, size=(0,1), text_color=cor_titulo, background_color=fundo_titulo)],
            [sg.Text(vencedor, font=fonte_titulo, size=(0,1), text_color=cor_titulo, background_color=fundo_titulo)],
            [sg.Text('')],
            [sg.Button('Retornar', font=fonte_texto, size=tamanho_texto)]
        ]

        window = sg.Window('Partidas', size=(900,900), element_justification="c", grab_anywhere=True).Layout(layout)
        button, values = window.read()
        window.close()
    
    def mostra_dados(self, competicoes: list):
        competicoes = [
            [sg.Listbox(values=competicoes, font=fonte_texto, size=(80, 8), key='competicoes')]
        ]

        layout = [
            [sg.Image(logo2, size=(300, 300))],
            [sg.Text('Relatório Competições/Vencedores', font=fonte_titulo, size=(0,1), text_color=cor_titulo, background_color=fundo_titulo)],
            [competicoes],
            [sg.Text('')],
            [sg.Button('Retornar', font=fonte_texto, size=tamanho_texto, key=1)]
        ]

        window = sg.Window('Relatório Competições', size=(900,900), element_justification="c", grab_anywhere=True).Layout(layout)
        button = window.Read()
        window.close()
    
    def mostra_mensagem(self, msg):
        sg.theme(tema)
        layout = [
            [sg.Text(msg, font=fonte_texto, size=tamanho_texto_aviso, justification="c")],
            [sg.Cancel("Ok", font=fonte_texto, size= tamanho_texto_aviso)]
        ]

        window = sg.Window('Aviso!', size=tamanho_aviso2, element_justification="c", grab_anywhere=True).Layout(layout)
        button, msg = window.read()
        window.close()
        print(msg)