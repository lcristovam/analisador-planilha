import PySimpleGUI as sg

sg.theme("LightGrey1")

layout = [
    [sg.Text("Line 1"), sg.Button("Botão linha 1")],
    [sg.In("Input 1", key="-Input1-"), sg.Button("Botão linha 2")]
]

window = sg.Window("Program Name x", layout)

while True:
    event, values = window.read()

    print(event, values)

    if event == sg.WIN_CLOSED:
        break

