# Python GUI Demo
# Quick Python GUI with PySimpleGUI
# Yu Hin Hau
# 11/2/2021

import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Column

import threading


# Custom Thread
def func_custom(val1, val2):
    global result
    global custom_callback

    import time

    result = 0

    time.sleep(5)

    for i  in range(5):
        for j in range(int(val1)):
            for k in range(int(val2)):
                result += val1 * val2 / 3.14

    custom_callback = True


# Main Method
def main():

    # Set GUI Theme
    sg.theme("DarkBlue")
    

    #Set GUI Layout and Create Window

    col_layout = sg.Column( [
            [sg.In(size=(10,10), font='Arial 20', key='-IN1-')],
            [sg.In(size=(10,5), font='Arial 20', key='-IN2-')]
        ])

    layout = [[
        Column([
        [sg.Text('Python GUI Demo', font='Arial 12 bold')],
        [sg.HorizontalSeparator()],
        [col_layout, sg.Listbox(values=['ADD','SUBTRACT','MULTIPLY','DIVIDE', 'CUSTOM'], default_values=['ADD'], size=(10,5), key='-ACTION-')],
        [sg.Multiline(size=(35,5), key='-OUT-', disabled=True)],
        [sg.Button('Calculate', size=(32,2), key='-CALC-')]
    ], element_justification='center')]]


    window = sg.Window('Hello World', layout=layout, resizable=True)

    # Get GUI Elements
    IN1 = window.find_element('-IN1-')
    IN2 = window.find_element('-IN2-')
    OUT = window.find_element('-OUT-')
    ACTION = window.find_element('-ACTION-')

    # Define Global Callback Var
    global custom_callback    
    custom_callback = False

    while True:
        event, values = window.read(timeout=100)
        
        if event == sg.WIN_CLOSED:
            exit()

        # Execution Actions when Calculate Button is Pressed
        if event == '-CALC-':
            OUT.update(disabled=False)

            val1 = float(IN1.get())
            val2 = float(IN2.get())
            
            if ACTION.get()[0] == 'ADD':
                sum = float(val1) + float(val2)
                OUT.update(f'The sum of {val1} and {val2} is {sum}')

            if ACTION.get()[0] == 'SUBTRACT':
                diff = float(val1) - float(val2)
                OUT.update(f'The differences of {val1} and {val2} is {diff}')


            if ACTION.get()[0] == 'MULTIPLY':
                prod = float(val1) * float(val2)
                OUT.update(f'The product of {val1} and {val2} is {prod}')


            if ACTION.get()[0] == 'DIVIDE':
                quotient = float(val1) / float(val2)
                OUT.update(f'The quotient of {val1} and {val2} is {quotient}')


            if ACTION.get()[0] == 'CUSTOM':

                # Start Custom Thread to Avoid Frozen GUI
                x = threading.Thread(target=func_custom, args={val1, val2})
                x.start()

                OUT.update('Please wait... custom function is running!')


        # Callback to Main Loop When Custom Function is Done
        if custom_callback:
            global result 
            custom_callback = False
            OUT.update(f'The result of the custom function applied to {val1} and {val2} is {result}')

            


# Run Main 
if __name__ == "__main__":
    main()