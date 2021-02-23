import translators
lang_key = {'english' : 'en', 'tamil' : 'ta', 'french' : 'fr', 'spanish' : 'es'}
from tkinter import *
window = Tk()
window.title('Translator')
show = Label(window, text='No Translations Have Occurred Yet')
show.grid(row=0, column=0)
options = list(lang_key.keys())
Label(window, text='Text to translate:').grid(row=1, column=0)
txt = Entry(window)
txt.grid(row=1, column=1)
Label(window, text='Language').grid(row=2, column=0)
lang = StringVar()
lang.set(options[0])
OptionMenu(window, lang, *options).grid(row=2, column=1)
Button(window, text='Close', command=window.destroy).grid(row=3, column=0, sticky=E)
def translate():
    result = translators.google(str(txt.get()), if_use_cn_host=True, to_language=lang_key[lang.get()])
    show.config(text=result)
    show.update()
Button(window, text='Translate', command=translate).grid(row=3, column=0, sticky=W)
window.mainloop()