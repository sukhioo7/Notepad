import tkinter as tk 
from tkinter import filedialog


class Notepad():
    def __init__(self,root):
        self.file_path = None

        self.window = root
        root.geometry('902x515')  
        root.resizable(0,0)     
        self.window.title('Notepad')
        root.config(background='#A67B5B')

        open_file = tk.Button(root,text="Open",bg='#79443B',fg='white',font=('Segoe UI',11),padx=15,pady=8,relief='groove',command=self.open_file)
        save_file = tk.Button(root,text="Save",bg='#79443B',fg='white',font=('Segoe UI',11),padx=15,pady=8,relief='groove',command=self.save_file)
        save_as_file = tk.Button(root,text="Save As",bg='#79443B',fg='white',font=('Segoe UI',11),padx=15,pady=8,relief='groove',command=self.save_as_file)
        clear_file = tk.Button(root,text="Clear",bg='#79443B',fg='white',font=('Segoe UI',11),padx=15,pady=8,relief='groove',command=self.clear_text)       
        help_file = tk.Button(root,text="Help",bg='#79443B',fg='white',font=('Segoe UI',11),padx=15,pady=8,relief='groove',command=self.help_notepad)

        self.text_area = tk.Text(root,font=('Segoe UI',15),relief='sunken',borderwidth=10,height=15,width=80)
        # palacing text area in window 
        self.text_area.grid(row=1,column=0,columnspan=5)
            
        # placing buttons in main window
        open_file.grid(row=0,column=0,padx=10,pady=12)
        save_file.grid(row=0,column=1,padx=10,pady=12)
        save_as_file.grid(row=0,column=2,padx=10,pady=12)
        clear_file.grid(row=0,column=3,padx=10,pady=12)       
        help_file.grid(row=0,column=4,padx=10,pady=12)


    def open_file(self):
        self.file_path = filedialog.askopenfilename()
        if self.file_path:
            with open(self.file_path,'r') as f:
                file_text = f.read()
            self.text_area.delete(0.0,tk.END)
            self.text_area.insert(tk.END,file_text)
            root.title(f'Notepad - {self.file_path}')

    def save_file(self):
        if self.file_path:
            file_text = self.text_area.get(0.0,tk.END)
            with open(self.file_path,'w') as f:
                f.write(file_text)
        else:
            self.save_as_file()

    def save_as_file(self):
        file_options = [('.txt','*.txt'),('.bat','*.bat'),('All files','*.*')]
        file_save = filedialog.asksaveasfilename(defaultextension='.txt',filetypes=file_options)
        if file_save:
            file_text = self.text_area.get(0.0,tk.END)
            with open(file_save,'w') as f:
                f.write(file_text)

    def clear_text(self):
        self.text_area.delete(0.0,tk.END)

    def help_notepad(self):
        self.text_area.delete(0.0,tk.END)
        what_is_notepad = '''   Notepad is a generic text editor that lets you create, open, and read plaintext files with a .txt file 
extension. If the file contains special formatting or is not a plaintext file, it cannot be read in Notepad. The image shown here is a small example of what the Notepad may look like while running.'''
        self.text_area.insert(tk.END,what_is_notepad)


root = tk.Tk()
note = Notepad(root)
root.mainloop()