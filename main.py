import summarize
from summarize import summarizeNews

import PySimpleGUI as sg      

sg.theme('DarkBlue2')    # Keep things interesting for your users

linkQuestionFont = ("Arial", 21)
AnswerFont = ("Arial", 15)


layout = [[sg.Text('Enter article link', font=linkQuestionFont)],      
          [sg.Input(key='-LINK-', font=AnswerFont, pad=20), sg.Submit(), sg.Exit()], 
          [sg.HSeparator()], 
          [sg.Multiline(size=(50,30), pad=50, font=AnswerFont, key='-SUMMARY-')]]

window = sg.Window('Tosko - summarize an article!', layout, resizable=True, finalize=True)      

while True:
    event, values = window.read() 
    print(event, values)   
    if event == 'Submit':
        newText = summarize.summarizeNews(values["-LINK-"])

        text = window['-SUMMARY-']
        text.update(newText)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break      


window.close()
