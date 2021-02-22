from tkinter import *
from tkinter import ttk, messagebox, font
from tkinter.colorchooser import askcolor
from tkinter.filedialog import askopenfilename, asksaveasfile
showStatusBar = True
showToolBar = True
fontFamily = 'Arial'
fontSize = 12
textChanged = False
url = ''
class FindDialog(Toplevel):
    def __init__(self, parent, *args, **kwargs):
        Toplevel.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.geometry('450x200+550+200')
        self.title('Find')
        self.resizable(False, False)
        txtFind = Label(self, text='Find: ')
        txtFind.place(x=20, y=20)
        txtReplace = Label(self, text='Replace: ')
        txtReplace.place(x=20, y=60)
        self.findInput = Entry(self, width=30)
        self.replaceInput = Entry(self, width=30)
        self.findInput.place(x=100, y=20)
        self.replaceInput.place(x=100, y=60)
        self.btnFind = Button(self, text='Find', command=self.parent.findWords)
        self.btnReplace = Button(self, text='Replace', command=self.parent.replaceWords)
        self.btnFind.place(x=200, y=90)
        self.btnReplace.place(x=240, y=90)
class MainMenu(Menu):
    def __init__(self, parent, *args, **kwargs):
        Menu.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        #file
        self.new_icon = PhotoImage(file='texteditoricon1.png')
        self.open_icon = PhotoImage(file='texteditoricon2.png')
        self.open_icon = self.open_icon.zoom(25)
        self.open_icon = self.open_icon.subsample(32)
        self.save_icon = PhotoImage(file='texteditoricon3.png')
        self.save_icon = self.save_icon.zoom(25)
        self.save_icon = self.save_icon.subsample(65)
        self.exit_icon = PhotoImage(file='texteditoricon4.png')
        self.exit_icon = self.exit_icon.zoom(25)
        self.exit_icon = self.exit_icon.subsample(200)
        self.file = Menu(self, tearoff=0)
        self.file.add_command(label='New', image=self.new_icon, compound=LEFT, accelerator='Ctr+N', command=self.parent.newFile)
        self.file.add_command(label='Open', accelerator='Ctrl+O', image=self.open_icon, command=self.parent.openFile)
        self.file.add_command(label='Save', accelerator='Ctrl+S', image=self.save_icon, command=self.parent.saveFile)
        self.file.add_command(label='Save As', accelerator='Ctrl+A+S', image=self.save_icon, command=self.parent.saveAsFile)
        self.file.add_command(label='Exit',image=self.exit_icon, command=self.parent.exitFunc)
        self.add_cascade(label='File', menu=self.file)
        #edit
        self.edit = Menu(self, tearoff=0)
        self.edit.add_command(label='Copy', accelerator='Ctrl+C', command=lambda :self.parent.textEditor.event_generate('<Control c>'))
        self.edit.add_command(label='Paste', accelerator='Ctrl+V', command=lambda :self.parent.textEditor.event_generate('<Control v>'))
        self.edit.add_command(label='Cut', accelerator='Ctrl+X', command=lambda :self.parent.textEditor.event_generate('<Control x>'))
        self.edit.add_command(label='Clear All', accelerator='Ctrl+Command+C', command=lambda :self.parent.textEditor.delete(1.0, END))
        self.edit.add_command(label='Find', accelerator='Ctrl+F', command=self.parent.find)
        self.add_cascade(label='Edit', menu=self.edit)
        #view
        global showToolBar, showStatusBar
        self.view = Menu(self, tearoff=0)
        self.view.add_checkbutton(onvalue=True, offvalue=False, label='Tool Bar', variable=showToolBar, command=self.parent.hideToolbar)
        self.view.add_checkbutton(onvalue=True, offvalue=False, label='Status Bar', variable=showStatusBar, command=self.parent.hideStatusbar)
        self.add_cascade(label='View', menu=self.view)
        #themes
        self.theme = Menu(self, tearoff=0)
        self.color_list = {'Default' : '#000000.#FFFFFF', 'Tomato' : '#ffff00.#ff6347', 'LimeGreen' : '#fffff0.#32cd32', 'Magenta' : '#fffafa.#ff00ff', 'Royal Blue' : '#ffffbb.#4169e1', 'MediumBlue' : '#d1e7e0.#0000cd', 'Dracula' : '#ffffff.#000000'}
        self.theme_choice = StringVar()
        for i in sorted(self.color_list):
            self.theme.add_radiobutton(label=i, variable=self.theme_choice, command=self.changeTheme)
        self.add_cascade(label='Theme', menu=self.theme)
        self.about = Menu(self, tearoff=0)
        self.about.add_command(label='About', command=lambda :messagebox.showinfo('About', 'This was made by Atul Nitin.'))
        self.add_cascade(label='About', menu=self.about)
    def changeTheme(self):
        selected_theme = self.theme_choice.get()
        fg_bg_color = self.color_list.get(selected_theme)
        fg, bg = fg_bg_color.split('.')
        self.parent.textEditor.config(background=bg, foreground=fg)
class TextEditor(Text):
    def __init__(self, parent, *args, **kwargs):
        Text.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.config(wrap='word')
        self.pack(expand=YES, fill=BOTH)
        self.config(relief=FLAT)
        yScrollBar = Scrollbar(self, orient=VERTICAL, command=self.yview)
        yScrollBar.pack(side=RIGHT, fill=Y)
        self.config(yscrollcommand=yScrollBar.set)
        self.configure(font='arial 12')
        self.bind('<<Modified>>', self.parent.changed)
class StatusBar(Label):
    def __init__(self, parent, *arg, **kwargs):
        Label.__init__(self, parent, *arg, **kwargs)
        self.parent = parent
        self.pack(side=BOTTOM)
        self.config(text='Status Bar')
class ToolBar(Label):
    def __init__(self, parent, *args, **kwargs):
        Label.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.pack(side=TOP, fill=X)
        self.cbFont = ttk.Combobox(self)
        self.cbFontSize = ttk.Combobox(self)
        self.cbFont.pack(side=LEFT, padx=(5, 10))
        self.cbFontSize.pack(side=LEFT)
        self.boldIcon = PhotoImage(file='texteditoricons5.png')
        self.boldIcon = self.boldIcon.zoom(25)
        self.boldIcon = self.boldIcon.subsample(150)
        btnBold = Button(self, image=self.boldIcon, command=self.parent.changeBold)
        btnBold.pack(side=LEFT, padx=5)
        self.italicIcon = PhotoImage(file='texteditoricons6.png')
        self.italicIcon = self.italicIcon.zoom(25)
        self.italicIcon = self.italicIcon.subsample(175)
        btnItalic = Button(self, image=self.italicIcon, command=self.parent.changeItalic)
        btnItalic.pack(side=LEFT, padx=5)
        self.underIcon = PhotoImage(file='texteditoricon7.png')
        self.underIcon = self.underIcon.zoom(25)
        self.underIcon = self.underIcon.subsample(125)
        btnUnder = Button(self, image=self.underIcon, command=self.parent.changeUnderline)
        btnUnder.pack(side=LEFT, padx=5)
        self.fontColorIcon = PhotoImage(file='texteditoricon8.png')
        self.fontColorIcon = self.fontColorIcon.zoom(25)
        self.fontColorIcon = self.fontColorIcon.subsample(144)
        btnFontColor = Button(self, image=self.fontColorIcon, command=self.parent.changeFontColor)
        btnFontColor.pack(side=LEFT, padx=5)
        self.alignLeftIcon = PhotoImage(file='texteditoricons9.png')
        self.alignLeftIcon = self.alignLeftIcon.zoom(25)
        self.alignLeftIcon = self.alignLeftIcon.subsample(200)
        btnAlignLeft = Button(self, image=self.alignLeftIcon, command=self.parent.alignLeft)
        btnAlignLeft.pack(side=LEFT, padx=5)
        self.alignCenterIcon = PhotoImage(file='texteditoricons11.png')
        self.alignCenterIcon = self.alignCenterIcon.zoom(25)
        self.alignCenterIcon = self.alignCenterIcon.subsample(200)
        btnAlignCenter = Button(self, image=self.alignCenterIcon, command=self.parent.alignCenter)
        btnAlignCenter.pack(side=LEFT, padx=5)
        self.alignRightIcon = PhotoImage(file='texteditoricons10.png')
        self.alignRightIcon = self.alignRightIcon.zoom(25)
        self.alignRightIcon = self.alignRightIcon.subsample(125)
        btnAlignRight = Button(self, image=self.alignRightIcon, command=self.parent.alignRight)
        btnAlignRight.pack(side=LEFT, padx=5)
        self.trashIcon = PhotoImage(file='texteditoricon12.png')
        self.trashIcon = self.trashIcon.zoom(25)
        self.trashIcon = self.trashIcon.subsample(125)
        btnTrash = Button(self, image=self.trashIcon, command=self.parent.trash)
        btnTrash.pack(side=LEFT, padx=5)
        self.closeIcon = PhotoImage(file='texteditoricon13.png')
        self.closeIcon = self.closeIcon.zoom(25)
        self.closeIcon = self.closeIcon.subsample(150)
        btnClose = Button(self, image=self.closeIcon, command=self.parent.exitFunc)
        btnClose.pack(side=LEFT, padx=5)
        fonts = font.families()
        fontList = []
        fontSizeList=[]
        for i in range(8, 101):
            fontSizeList.append(i)
        for i in fonts:
            fontList.append(i)
        self.fontVar = StringVar()
        self.cbFont.config(values=fontList, textvariable=self.fontVar)
        self.cbFont.current(0)
        self.fontSizeVar = StringVar()
        self.cbFontSize.config(values=fontSizeList, textvariable=self.fontSizeVar)
        self.cbFontSize.current(4)
        self.cbFont.bind('<<ComboboxSelected>>', self.parent.getFont)
        self.cbFontSize.bind('<<ComboboxSelected>>', self.parent.getFontSize)
class MainApplication(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.pack(fill=BOTH, expand=True)
        self.main_menu = MainMenu(self)
        self.parent.config(menu=self.main_menu)
        self.toolbar = ToolBar(self)
        self.textEditor = TextEditor(self)
        self.textEditor.focus()
        self.statusBar = StatusBar(self)
    # noinspection PyUnusedLocal
    def getFont(self, *args):
        global fontFamily
        fontFamily = self.toolbar.cbFont.get()
        self.textEditor.configure(font=(fontFamily, fontSize))
    # noinspection PyUnusedLocal
    def getFontSize(self, *args):
        global fontSize
        fontSize = self.toolbar.cbFontSize.get()
        self.textEditor.configure(font=(fontFamily, fontSize))
    def changeBold(self):
        text_pro = font.Font(font=self.textEditor['font'])
        if text_pro.actual('weight') == 'normal':
            self.textEditor.configure(font=(fontFamily, fontSize, 'bold'))
        elif text_pro.actual('weight') == 'bold':
            self.textEditor.configure(font=(fontFamily, fontSize, 'normal'))
    def changeItalic(self):
        text_pro = font.Font(font=self.textEditor['font'])
        if text_pro.actual('slant') == 'roman':
            self.textEditor.configure(font=(fontFamily, fontSize, text_pro.actual('weight'), 'italic'))
        elif text_pro.actual('slant') == 'italic':
            self.textEditor.configure(font=(fontFamily, fontSize, text_pro.actual('weight'), 'roman'))
    def changeUnderline(self):
        text_pro = font.Font(font=self.textEditor['font'])
        if text_pro.actual('underline') == 0:
            self.textEditor.configure(font=(fontFamily, fontSize, text_pro.actual('weight'), text_pro.actual('slant'), 'underline'))
        elif text_pro.actual('underline') == 1:
            self.textEditor.configure(font=(fontFamily, fontSize, text_pro.actual('weight'), text_pro.actual('slant'), 'normal'))
    def changeFontColor(self):
        self.textEditor.configure(fg=askcolor()[1])
    def alignLeft(self):
        content = self.textEditor.get(1.0, 'end')
        self.textEditor.tag_config('left', justify=LEFT)
        self.textEditor.delete(1.0, END)
        self.textEditor.insert(INSERT, content, 'left')
    def alignCenter(self):
        content = self.textEditor.get(1.0, 'end')
        self.textEditor.tag_config('center', justify=CENTER)
        self.textEditor.delete(1.0, END)
        self.textEditor.insert(INSERT, content, 'center')
    def alignRight(self):
        content = self.textEditor.get(1.0, 'end')
        self.textEditor.tag_config('right', justify=RIGHT)
        self.textEditor.delete(1.0, END)
        self.textEditor.insert(INSERT, content, 'right')
    def trash(self):
        self.textEditor.delete(1.0, END)
    # noinspection PyUnusedLocal
    def changed(self, *args):
        global textChanged
        flag = self.textEditor.edit_modified()
        textChanged = True
        if flag:
            word = len(self.textEditor.get(1.0, 'end-1c').split())
            letters = len(self.textEditor.get(1.0, 'end-1c'))
            self.statusBar.config(text=f'Characters : {letters}    Words : {word}')
        self.textEditor.edit_modified(False)
    def newFile(self):
        global url
        try:
            url = ''
            self.textEditor.delete(1.0, END)
        except:pass
    def openFile(self):
        global url
        url = askopenfilename(title='Select a file to open')
        try:
            with open(url, 'r') as file:
                self.textEditor.delete(1.0, END)
                self.textEditor.insert(1.0, file.read())
        except:return
        self.parent.title(f'Text Editor - Now Editing {url.split("/")[-1]}')
    def saveFile(self):
        global url
        try:
            if url == '':
                url=asksaveasfile(mode='w', defaultextention='.txt')
                url.write(str(self.textEditor.get(1.0, END)))
                url.close()
            else:
                with open(url, 'w', encoding='utf-8') as file:
                    file.write(self.textEditor.get(1.0, END))
        except:return
    def saveAsFile(self):
        global url
        cont = str(self.textEditor.get(1.0, END))
        url = asksaveasfile(mode='w')
        url.write(cont)
        url.close()
        self.parent.title(f'Text Editor - Now Editing {url.split("/")[-1]}')
    def exitFunc(self):
        global url, textChanged
        try:
            if textChanged:
                mBox = messagebox.askyesnocancel('Warning', 'Do You Want To Save?')
                if mBox is True:
                    if url != '':
                        cont = str(self.textEditor.get(1.0, END))
                        with open(url, 'w', encoding='utf-8') as file:
                            file.write(cont)
                            self.parent.destroy()
                    else:
                        cont = self.textEditor.get(1.0, END)
                        url = asksaveasfile(mode='w')
                        url.write(cont)
                        url.close()
                        self.parent.destroy()
                elif mBox is False:
                    self.parent.destroy()
            else:
                self.parent.destroy()


        except:return
    #noinspection PyUnusedLocal
    def find(self, *args):
        # noinspection PyAttributeOutsideInit
        self.find = FindDialog(parent=self)
    # noinspection PyUnusedLocal
    def findWords(self, *args):
        word = self.find.findInput.get()
        self.textEditor.tag_remove('match', '1.0', END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = self.textEditor.search(word, start_pos, stopindex=END)
                if not start_pos:
                    break
                end_pos = f'{start_pos}+{len(word)}c'
                self.textEditor.tag_add('match', start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                self.textEditor.tag_config('match', foreground='red', background='yellow')
    # noinspection PyUnusedLocal
    def replaceWords(self, *args):
        replaceText = self.find.replaceInput.get()
        word = self.find.findInput.get()
        content = self.textEditor.get(1.0, END)
        newValue = content.replace(word, replaceText)
        self.textEditor.delete(1.0, END)
        self.textEditor.insert(1.0, newValue)
    def hideToolbar(self):
        global showToolBar
        if showToolBar:
            self.toolbar.pack_forget()
            showToolBar = False
        else:
            self.textEditor.pack_forget()
            self.statusBar.pack_forget()
            self.toolbar.pack(side=TOP, fill=X)
            self.textEditor.pack(expand=YES, fill=BOTH)
            self.statusBar.pack(side=BOTTOM)
            showToolBar = True
    def hideStatusbar(self):
        global showStatusBar
        if showStatusBar:
            self.statusBar.pack_forget()
            showStatusBar = False
        else:
            self.statusBar.pack()
            showStatusBar = True
if __name__ == '__main__':
    window = Tk()
    window.title('Text Editor')
    MainApplication(window).pack(side=TOP, fill=BOTH, expand=True)
    window.geometry('1250x850')
    window.mainloop()