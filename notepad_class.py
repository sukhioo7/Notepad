import tkinter as tk
from tkinter import filedialog

class Notpad():

    def __init__(self,user_root):
        self.file_path = None
        self.window = user_root
        self.window.title('Notepad')
        self.window.geometry('1400x535')
        self.window.config(bg='#f7f8f3')
        self.window.resizable(0.0,0.0)

        self.text_area = tk.Text(width=135,font=('Bahnschrift SemiLight',13),bg='#f7f8f3',relief='solid')
        self.text_area.grid(row=1,column=2,rowspan=5,padx=15,pady=15)
        # Making button 
        btn_open = tk.Button(text='Open',width=8,font=('Bauhaus 93',18),bg='#f7444e',fg='white',relief='solid',command=self.open)
        btn_save = tk.Button(text='Save',width=8,font=('Bauhaus 93',18),bg='#78bcc4',fg='white',relief='solid',command=self.save)
        btn_save_as = tk.Button(text='Save As',width=8,font=('Bauhaus 93',18),bg='#002c3e',fg='white',relief='solid',command=self.save_as)
        btn_clear = tk.Button(text='Clear',width=8,font=('Bauhaus 93',18),bg='#ff6f3d',fg='white',relief='solid',command=self.clear)
        btn_help = tk.Button(text='Help',width=8,font=('Bauhaus 93',18),bg='#ee3163',fg='white',relief='solid',command=self.help)

        btn_open.grid(row=1,column=1,padx=20,pady=20)
        btn_save.grid(row=2,column=1,padx=20,pady=20)
        btn_save_as.grid(row=3,column=1,padx=20,pady=20)
        btn_clear.grid(row=4,column=1,padx=20,pady=20)
        btn_help.grid(row=5,column=1,padx=20,pady=20)


    def open(self):
        self.file_path = filedialog.askopenfilename()
        with open(self.file_path,'r') as text_file:
            text = text_file.read()
        self.clear()
        self.text_area.insert(0.0,text)
        self.window.title(f'Notepad : {self.file_path}')

    def save(self):
        if self.file_path:
            with open(self.file_path,'w') as text_file:
                text = self.text_area.get(0.0,tk.END)
                text_file.write(text)
        else:
            self.save_as()

    def save_as(self):
        file_options = [('Python file','*.py'),('Bat file','*.bat'),('Text file','*.txt'),('All files','*.*')]
        target_loc = filedialog.asksaveasfilename(defaultextension='.txt',filetypes=file_options)
        with open(target_loc,'w') as text_file:
            text = self.text_area.get(0.0,tk.END)
            text_file.write(text)

    def clear(self):
        self.text_area.delete(0.0,tk.END)

    def help(self):
        help_text = '''
Notepad is a basic text editor that is included with Windows. It is a simple program that can be used to create and 
edit text files. Notepad is not a word processor, so it does not have many of the features that are found in word 
processors, such as the ability to create and edit tables, images, or charts. However, Notepad is a great tool for 
creating simple text files, such as program code, scripts, or notes.

To use Notepad, simply open the program and start typing. You can use the keyboard to type in text, and you can use 
the mouse to select text and perform other actions. Notepad does not have a lot of menus or buttons, so it is very 
easy to learn how to use.

When you are finished editing a text file, you can save it by clicking on the "File" menu and selecting "Save." You 
will be prompted to enter a filename and location for the file. Notepad will save the file as a plain text file with a 
.txt extension.

Here are some of the things you can do with Notepad:

Create and edit text files
Save text files in a variety of formats
Search for text within a text file
Replace text within a text file
Use keyboard shortcuts to perform common tasks
Print text files
Notepad is a very versatile tool that can be used for a variety of tasks. It is a great tool for beginners and experienced 
users alike.

Here are some additional tips for using Notepad:

    # o select a block of text, hold down the left mouse button and drag the mouse over the text you want to select.
    # To copy selected text, press the "Ctrl" key and the "C" key at the same time.
    # To paste copied text, press the "Ctrl" key and the "V" key at the same time.
    # To search for text within a text file, click on the "Edit" menu and select "Find." Enter the text you want to search for and 
    # click on the "Find Next" button.
    # To replace text within a text file, click on the "Edit" menu and select "Replace." Enter the text you want to replace and the 
    # text you want to replace it with. Click on the "Replace" button to replace the first occurrence of the text, or click on the 
    # "Replace All" button to replace all occurrences of the text.
    # To use keyboard shortcuts to perform common tasks, click on the "Help" menu and select "Keyboard shortcuts."
        '''
        self.clear()
        self.text_area.insert(0.0,help_text)


root = tk.Tk()

new = Notpad(root)

root.mainloop()
