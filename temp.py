import tkinter as tk 

window = tk.Tk()
window.title('MY title')
window.geometry('700x600')
window.config(bg='#E1F7F5')


heading = tk.Label(text='Calculator',font=('Bauhaus 93',52),bg='#E1F7F5',fg='#0E46A3')
heading.pack(pady=20)

label1 = tk.Label(text='Enter Number 1: ',font=('HP Simplified Hans',20),bg='#E1F7F5',
                  fg='#1E0342')
label1.pack(pady=5)

user_input1 = tk.Entry(font=('HP Simplified Hans',20),highlightbackground='#0E46A3',highlightthickness=1)
user_input1.pack()

label2 = tk.Label(text='Enter Number 2: ',font=('HP Simplified Hans',20),bg='#E1F7F5',
                  fg='#1E0342')
label2.pack(pady=5)

user_input2 = tk.Entry(font=('HP Simplified Hans',20),highlightbackground='#0E46A3',highlightthickness=1)
user_input2.pack()

add_btn = tk.Button(text='SUM',font=('Bauhaus 93',20),width=20,bg='#0E46A3',fg='white',relief='solid')
add_btn.pack(pady=5)

window.mainloop()
