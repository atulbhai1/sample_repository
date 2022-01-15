from morse_code_translator.translator import translate_to_lat, translate_to_morse
from helpful_stuff.functions import get_dropdown, get_entry
from tkinter.messagebox import showinfo
def to_english(string=""):
    return translate_to_lat(string)
def to_morse(string=""):
    return translate_to_morse(string)
cont = True
while cont:
    response = get_dropdown("Do you want to translate to english or to morse?", ["english", "morse"], "Morse Code Translator")
    if response == "english":
        func = to_english
        alt = "morse"
    else:
        func = to_morse
        alt = "english"
    to_translate = get_entry(f"What do you want to translate to {response}?", "Morse Code Translator")
    showinfo(f"Translated Text From {alt} to {response}",func(to_translate))
    continue1 = get_dropdown("Do you want to continue?", ["Yes", "No"], "Morse Code Translator")
    if continue1.lower() == 'yes':
        cont = True
    else:
        cont = False