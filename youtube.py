import customtkinter as ctk
from pytubefix import YouTube
from pytubefix.cli import on_progress

ctk.set_appearance_mode('system')

def download_video_file():
    link = user_input.get()
    try:
        yt = YouTube(link, on_progress_callback =on_progress)
        text = f"Downloaded Successfully\n\nTitle : {yt.title}\n\nDescription : {yt.description[:100]}..."
        video = yt.streams.get_highest_resolution()
        video.download(r"C:\Users\deeps\Downloads")
        output.configure(text=text,fg_color=('#C4DAD2','#16423C'),pady=15,padx=10)
    except Exception as e:
        output.configure(text=f"ERROR : {e}",fg_color=('#C4DAD2','#16423C'),pady=15,padx=10)

def download_audio_file():
    link = user_input.get()
    try:
        yt = YouTube(link, on_progress_callback =on_progress)
        text = f"Downloaded Successfully\n\nTitle : {yt.title}\n\nDescription : {yt.description[:100]}..."
        video = yt.streams.get_audio_only()
        video.download(r"C:\Users\deeps\Downloads",mp3=True)
        output.configure(text=text,fg_color=('#C4DAD2','#16423C'),pady=15,padx=10)
    except Exception as e:
        output.configure(text=f"ERROR : {e}",fg_color=('#C4DAD2','#16423C'),pady=15,padx=10)



window = ctk.CTk()
window.title('YouTube Downloader')
window.geometry('800x550')

heading = ctk.CTkLabel(window,text='YouTube Downloader',font=('Script MT Bold',80),
                       text_color='#D91656')
heading.grid(row=1,column=1,pady=50,columnspan=2)

sub_heading = ctk.CTkLabel(window,text='Paste your link here...',font=('Script MT Bold',30),
                           text_color=('#333644','#EEEEEE'))
sub_heading.grid(row=2,column=1,columnspan=2)

user_input = ctk.CTkEntry(window,placeholder_text='Ex : http://www.youtube.com/sdfs',
                          font=("Bahnschrift",22),width=600,
                          placeholder_text_color='#90A4AE',height=40)
user_input.grid(row=3,column=1,pady=15,columnspan=2)

download_video = ctk.CTkButton(window,text='Download Video',font=('Script MT Bold',30),
                           width=300,fg_color=('#055E68'),hover_color='#006159',
                           command=download_video_file)

download_video.grid(row=4,column=1)

download_audio = ctk.CTkButton(window,text='Download Audio',font=('Script MT Bold',30),
                           width=300,fg_color=('#055E68'),hover_color='#006159'
                           ,command=download_audio_file)

download_audio.grid(row=4,column=2)

output = ctk.CTkLabel(window,text='',font=('Script MT Bold',18),
                      wraplength=700,corner_radius=10)
output.grid(row=5,column=1,columnspan=2,pady = 10)

window.mainloop()


