import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Column
sg.theme("DarkBlue")

layout = [[
    Column([
    [sg.Text('Python GUI Demo', font='Arial 12 bold')],
    [sg.HorizontalSeparator()],
    [sg.Column( [[sg.In(size=(10,10), font='Arial 20')],[sg.In(size=(10,5), font='Arial 20')]]), sg.Listbox(values=['ADD','SUBTRACT','MULTIPLY','DIVIDE'], size=(10,5))],
    [sg.Multiline(size=(35,5))],
    [sg.Button('Calculate', size=(32,2))]
], element_justification='center')]]

event, values = sg.Window('Hello World', layout=layout, resizable=True).read()


print(values)