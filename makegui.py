from typing import Iterable
import PySimpleGUI as sg
from numpy import sort

import csv_analyser


sg.theme("LightGrey1")


def create_main_window():
    layout = [
        [
            sg.Text("Selecione o Seu CSV"),
            sg.In(key="-FILE-"),
            sg.FileBrowse("Selecionar"),
        ],
        [
            sg.Button("Analisar", key ="-START-"),
        ]
    ]
    window = sg.Window("Analisador de Planilha", layout)
    return window

def create_second_window(filepath):
    sum_sales = csv_analyser.read_total_value(filepath)
    list_sales = csv_analyser.read_csv_as_list(filepath)
    sales_analisys = csv_analyser.analyse(filepath)
    layout = [
        [
            sg.Text("Vendas no período Selecionado: "),
            sg.Table(
                values=list_sales, 
                headings=["Data", "Valor em vendas"],
                num_rows=min(25, len(list_sales)),
                
               
            )
        ],
        [
            sg.Text(
                f"Valor total de vendas: R$ {sum_sales}"
            ),
        ],
        [
            sg.Text(
                f"Dia com pior valor em vendas: {sales_analisys['min_value']['date']} com R$ {sales_analisys['min_value']['value']} "
            )
        ],
        [
            sg.Text(
                f"Dia com melhor valor em vendas: {sales_analisys['max_value']['date']} com R$ {sales_analisys['max_value']['value']}"
            ),
        ],
        [
            sg.Text(
                f"Dia com menor quantidade de vendas : {sales_analisys['min_qty']['date']} com {sales_analisys['min_qty']['value']} vendas"
            ),
        ],
        [
            sg.Text(
                f"Dia com maior quantidade de vendas: {sales_analisys['max_qty']['date']} com {sales_analisys['max_qty']['value']} vendas "
            ),
        ],
         
    ]

    window = sg.Window("Analisador de Planilha", layout)

    return window

main_window = create_main_window()
active_window = main_window


while True:
    event, values = active_window.read()

    if event == "-START-":
        main_window.hide()
        active_window = create_second_window(values["-FILE-"])

    if event == sg.WIN_CLOSED:
        break

active_window.close()