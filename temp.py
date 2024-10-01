import customtkinter as ctk
from googletrans import Translator

def lang_translation(lang):
    user_input = text_area.get(0.0,ctk.END)
    translator = Translator()
    result = translator.translate(user_input,dest=lang)
    output.configure(text=result.text,fg_color='#B7E0FF')

window  = ctk.CTk()
window.geometry('845x650')

dark_btn = ctk.CTkButton(window,text='Dark Mode',font=('Arial',12,'bold'),height=30,width=90,
                              fg_color='black',command=lambda : ctk.set_appearance_mode('dark'))
dark_btn.grid(row=0,column=1,pady=10)

light_btn = ctk.CTkButton(window,text='light Mode',font=('Arial',12,'bold'),height=30,width=90,
                              fg_color='black',command=lambda : ctk.set_appearance_mode('light'))
light_btn.grid(row=0,column=3,pady=10)

heading = ctk.CTkLabel(window,text='Google Translator',font=('Arial',50))
heading.grid(row=1,column=1,pady=20,columnspan=3)

text_area = ctk.CTkTextbox(window,border_width=2,font=('Arial',17),width=800)
text_area.grid(row=2,column=1,padx=20,pady=20,columnspan=3)

translate_btn = ctk.CTkButton(window,text='Translate',font=('Arial',30,'bold'),height=60,width=200,
                              fg_color='#34A853',command=lambda : lang_translation('english'))
translate_btn.grid(row=3,column=1)

hindi_btn = ctk.CTkButton(window,text='Hindi',font=('Arial',30,'bold'),height=60,width=200,
                          fg_color='#4285F4',command=lambda : lang_translation('hindi'))
hindi_btn.grid(row=3,column=2)

punjabi_btn = ctk.CTkButton(window,text='punjabi',font=('Arial',30,'bold'),height=60,width=200,
                            fg_color='#EA4335',command=lambda : lang_translation('punjabi'))
punjabi_btn.grid(row=3,column=3)

sub_heading = ctk.CTkLabel(window,text='Translation',font=('Arial',20))
sub_heading.grid(row=4,column=1,columnspan=3,pady=24)

output = ctk.CTkLabel(window,text='',font=('Arial',20),padx=20,pady=20,
                      corner_radius=10,wraplength=700)
output.grid(row=5,column=1,columnspan=3)

window.mainloop()
