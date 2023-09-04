import PySimpleGUI as sg
import toggle
import keyboard
import confusecntrl

sg.theme('DarkTanBlue')

# This is an assortment of keybinds
options = ['Escape', 'Space', 'BackSpace', 'Tab', 'Linefeed', 'Clear', 'Return', 'Pause', 'Scroll_Lock', 'Sys_Req', 'Delete', 'Home', 'Left', 'Up', 'Right', 'Down', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
speeds = ['20','30','40','50']
layout = [
    [sg.Checkbox('Auto Nexus', key='-AUTONEXUS-')],
    [sg.Checkbox('Slow Move', key='-SLOWMOVE-')],
    [sg.Combo(speeds, key='-SPEED-', default_value='50', size=(10, 5))],
    [sg.Checkbox('Confuse Controls/(ctrl+`)', key='-CONFUSECNTRL-')],
    [sg.Checkbox('Toggle/(ctrl+shift)', key='-TOGGLE-')],
    [sg.Combo(options, key='-KEY-', default_value='space', size=[10, 5], readonly=True)],
    [sg.Text('Interval (s)'), sg.InputText('6.5', key='-INTERVAL-', size=(5, 5))],
    [sg.Button('Exit')]
]

window = sg.Window('clicker', layout, keep_on_top=True)

def toggle_checkbox():
    window['-TOGGLE-'](not window['-TOGGLE-'].Get())

def confuse_checkbox():
    window['-CONFUSECNTRL-'](not window['-CONFUSECNTRL-'].Get())

keyboard.add_hotkey('ctrl+shift', toggle_checkbox)
keyboard.add_hotkey('ctrl+`', confuse_checkbox)

def get_gui_input():
    while True:
        event, values = window.read(timeout=100)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        toggle.set_toggle_state(values['-TOGGLE-'])
        toggle.set_interval(values['-INTERVAL-'])
        toggle.set_keyb(values['-KEY-'])
        confusecntrl.set_cntrl_state(values['-CONFUSECNTRL-'])
        checkbox2_value = values['-SLOWMOVE-']
        selected_option = values['-SPEED-']

    window.close()

if __name__ == "__main__":
    toggle.start_space_thread()  

    get_gui_input()