import customtkinter as ctk
import wikipedia

ctk.set_appearance_mode('system')

def get_wikipedia_data():
    query = user_input.get() # same as input() 
    try:
        data = wikipedia.summary(query,sentences=3)
        output.configure(text=data,fg_color=('#C4DAD2','#16423C'),pady=15,padx=10)
    except:
        output.configure(text='No Data Found',fg_color=('#C4DAD2','#16423C'),pady=15,padx=10)


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
                           width=400,fg_color=('#055E68'),hover_color='#006159',
                           command=get_wikipedia_data)

search_btn.pack()

output = ctk.CTkLabel(window,text='',font=('Script MT Bold',21),
                      wraplength=700,corner_radius=10)
output.pack(pady = 10)

window.mainloop()


