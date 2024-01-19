from subprocess import Popen
from pywinauto import Desktop
from pywinauto.application import Application
import os

# Types the filter text into the mp3tag window
def automate(filter):
    try:
        # Connect to the mp3tag window
        app = Application().connect(path=os.environ.get("MP3TAG_PATH"))
    except:
        # TODO: send this to a gui messaging system
        print('Are you sure mp3tag is open before you connect?')
        exit()

    # Open the window
    window =  app.top_window()
    window.maximize()

    # Get filter ready
    filter = filter.replace( ')' ,  '{)}') \
        .replace( '(' ,  '{(}') \
        .replace( ' ' ,  '{ }') \
        .replace( '%' ,  '{%}')

    # Clear the existing content in the ComboBox
    combo_box = window['Filte&r:ComboBox']
    combo_box.set_focus()
    combo_box.type_keys('^a')  # Ctrl+A to select all
    combo_box.type_keys('{BACKSPACE}')  # Clear the selected text

    # Send the filter to mp3tag
    window['Filte&r:ComboBox'].send_chars(filter)
