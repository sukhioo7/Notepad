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
window.title('YouTube Downloader')
window.geometry('800x550')

heading = ctk.CTkLabel(window,text='YouTube Downloader',font=('Script MT Bold',80),
                       text_color='#D91656')
heading.grid(row=1,column=1,pady=50)

sub_heading = ctk.CTkLabel(window,text='Paste your link here...',font=('Script MT Bold',30),
                           text_color=('#333644','#EEEEEE'))
sub_heading.grid(row=2,column=1)

user_input = ctk.CTkEntry(window,placeholder_text='Ex : http://www.youtube.com/sdfs',
                          font=("Bahnschrift",22),width=400,
                          placeholder_text_color='#90A4AE',height=40)
user_input.grid(row=3,column=1,pady=15)

download_video = ctk.CTkButton(window,text='Download Video',font=('Script MT Bold',30),
                           width=400,fg_color=('#055E68'),hover_color='#006159',
                           command=get_wikipedia_data)

download_video.grid(row=4,column=1)

download_audio = ctk.CTkButton(window,text='Download Audio',font=('Script MT Bold',30),
                           width=400,fg_color=('#055E68'),hover_color='#006159',
                           command=get_wikipedia_data)

download_audio.grid(row=5,column=1)

output = ctk.CTkLabel(window,text='',font=('Script MT Bold',21),
                      wraplength=700,corner_radius=10)
output.grid(row=6,column=1,pady = 10)

window.mainloop()


