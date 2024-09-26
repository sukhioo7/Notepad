import customtkinter as ctk

ctk.set_appearance_mode('light')

def say_hello():
    print('Hello')

window = ctk.CTk()
window.title('WikipediA')
window.geometry('800x650')

heading = ctk.CTkLabel(window,text='WikipediA',font=('Forte',100),
                       text_color='#055E68')
heading.pack(pady=50)

sub_heading = ctk.CTkLabel(window,text='Search Here...',font=('Script MT Bold',30),
                           text_color=('#333644','#EEEEEE'))
sub_heading.pack()

user_input = ctk.CTkEntry(window,placeholder_text='Ex : Samsung',
                          font=("Bahnschrift",22),width=400,
                          placeholder_text_color='#90A4AE',height=40)
user_input.pack(pady=15)

search_btn = ctk.CTkButton(window,text='Search',font=('Script MT Bold',30),
                           width=400,fg_color='#055E68',hover_color='#006159',
                           command=say_hello)

search_btn.pack()

window.mainloop()
