import PySimpleGUI as sg

def setup_gui():
    layout= [
        [sg.Text('Twitter Username'), sg.Input(key='-USERNAME-')],
        [sg.Button('Get User Details'), sg.Button('Exit')]
    ]
    sg.Window(title="Hello World", layout=layout, margins=(800, 500)).read()