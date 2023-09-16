import tkinter as tk
import wikipedia

def wiki_pedia():
    user_search = search_input.get()
    try:
        result = wikipedia.summary(user_search,sentences=3)
        result_label.config(text=result)
    except:
        result_label.config(text='No Data Found',font=('Harlow Solid Italic',25)
                            ,pady=20,fg='#CE0601')


window = tk.Tk()
window.geometry('800x600')
window.title('WikipediA')
window.config(bg='#FCF5E5')

title = tk.Label(text='WikipediA',font=('Harlow Solid Italic',75),fg='#CE0601',bg='#FCF5E5')
title.pack()

sub_title = tk.Label(text='Search Here...',font=('Harlow Solid Italic',25),fg='#B7B9AF',bg='#FCF5E5')
sub_title.pack()


search_input = tk.Entry(font=('Bahnschrift Light Condensed',25),width=30,bg='#B7B9AF')
search_input.pack()

btn = tk.Button(text='Search',font=('Harlow Solid Italic',23)
                ,relief='groove',bg='#4e5454',width=22,fg='white',command=wiki_pedia)
btn.pack(pady=5)

result_label = tk.Label(text='',font=('Bahnschrift Light Condensed',15),bg='#FCF5E5',wraplength=700)
result_label.pack()

window.mainloop()
