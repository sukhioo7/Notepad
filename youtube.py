import tkinter as tk 
from pytube import YouTube

def download_video():
    link = video_link.get()
    try:
        YouTube(link).streams.first().download(r'C:\Users\Sukh-e\Desktop\YT videos')
        done_heading.config(text='Your video is downloaded at : Desktop/YT videos')
    except:
        done_heading.config(text="Sorry :( we can't download this video")


root = tk.Tk()
root.title('Youtube Downloader')
root.geometry('1000x500')
root.config(bg='#FCF5E5')

heading = tk.Label(text='YouTube Downloader',font=('Harlow Solid Italic',60),bg='#FCF5E5',fg='#CE0601')
heading.pack(pady=20)

sub_heading = tk.Label(text='Paste your link here...',font=('Harlow Solid Italic',30),fg='#B7B9AF',bg='#FCF5E5')
sub_heading.pack(pady=20)

video_link = tk.Entry(font=('Bahnschrift Light Condensed',20),width=60,bg='#B7B9AF')
video_link.pack()

btn = tk.Button(text='Download',font=('Harlow Solid Italic',20),relief='groove',bg='#4e5454',width=22,fg='white'
                ,command=download_video)
btn.pack(pady=20)

done_heading = tk.Label(text='',font=('Harlow Solid Italic',25),fg='#CE0601',bg='#FCF5E5')
done_heading.pack(pady=20)

root.mainloop()
