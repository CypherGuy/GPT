import summarize
from summarize import summarizeNews

import PySimpleGUI as sg      

sg.theme('DarkGrey3')

linkQuestionFont = ("Arial", 21)
AnswerFont = ("Arial", 15)


layout = [[sg.Text('Enter article link', font=linkQuestionFont)],      
          [sg.Input(key='-LINK-', font=AnswerFont, pad=20), sg.Submit(), sg.Exit()], 
          [sg.Checkbox('Bullet point form', default=True, key = 'BP')],
          [sg.HSeparator()], 
          [sg.Multiline(
            size=(50,30), 
            pad=50, 
            font=AnswerFont, 
            key='-SUMMARY-', 
            auto_size_text=True
            )
        ]]

window = sg.Window('Tosko - summarize an article!', layout, resizable=True, finalize=True) 

#Allows you to find a particular part of a window
summaryBar = window.find_element("-SUMMARY-")
#Disables editing it
summaryBar.Update(disabled = True)

while True:
    event, values = window.read() 
    print(event, values)   
    if event == 'Submit':
        BP_form = values["BP"]
        print(BP_form)
        summaryBar.Update(disabled = False)
        newText = summarize.summarizeNews(values["-LINK-"])
        text = window['-SUMMARY-']
        text.update(newText)
        summaryBar.Update(disabled=True)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break      


window.close()
