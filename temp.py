# ----------------------------------------YOUTUBE DOWNLOADER-------------------------------------------------------------


import tkinter as tk
from tkinter import messagebox,filedialog,ttk
from pytubefix import YouTube
from pytubefix.cli import on_progress
from PIL import Image, ImageTk
import requests
from io import BytesIO

def download_video():
    link = video_link.get()
    if not link:
        messagebox.showerror("Error", "Please enter a valid YouTube Link")
        return
    
    
    folder = filedialog.askdirectory()
    if not folder:
        return


    try:
        youtube = YouTube(link, on_progress_callback = on_progress)
    
        ys = youtube.streams.get_highest_resolution()
        ys.download(output_path=folder)
        messagebox.showinfo('Success',f'Downloaded {youtube.title} successfully')
    except Exception as e:
        messagebox.showerror('Error',f'Failed to download video.\n{e}')
        
    
def download_audio():
    link = video_link.get()
    if not link:
        messagebox.showerror("Error", "Please enter a valid YouTube Link")
        return
    
    
    folder = filedialog.askdirectory()
    if not folder:
       return
    
    try:
        youtube = YouTube(link, on_progress_callback = on_progress)
    
        ys = youtube.streams.filter(only_audio=True).first()  
        ys.download(output_path=folder)
        messagebox.showinfo('Success',f'Downloaded audio of {youtube.title} successfully')
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download audio.\n{e}")
    


def fetch_video_info():
    link = video_link.get()
    if not link:
        messagebox.showwarning("Input Error", "Please enter a YouTube URL")
        return
    
    try:
        yt = YouTube(link)
        title = yt.title
        author = yt.author
        length = f"{yt.length // 60} minutes {yt.length % 60} seconds"
        views = f"{yt.views:,}"  # Add commas to the view count
        
        info_text = f"Title: {title}\nAuthor: {author}\nLength: {length}\nViews: {views}\n"

        info_window = tk.Toplevel(window)
        info_window.title("Video Information")
        info_window.geometry("400x200")
        
        info_label = tk.Label(info_window, text=info_text,font = ("Arial",6,'bold'),bg="#f0f0f0",justify=tk.LEFT)
        info_label.pack(pady=10)

        thumbnail_url = yt.thumbnail_url
        response = requests.get(thumbnail_url)
        img_data = BytesIO(response.content)
        img = Image.open(img_data)
        img = img.resize((160, 80), Image.Resampling.LANCZOS)
        
        img_tk = ImageTk.PhotoImage(img)
        
        thumbnail_label = tk.Label(info_window, image=img_tk)
        thumbnail_label.image = img_tk  # Keep a reference to prevent garbage collection
        thumbnail_label.pack(pady=10)

    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch video information: {e}")


window =  tk.Tk()
window.title("Youtube Audio and Video Downloader")
window.geometry("700x600")
window.config(bg = '#FFF6EA')

heading = tk.Label(text = 'Free YouTube Video Downloader',font = ('Georgla Pro',30,'bold','underline'),bg='white',fg='#E85C0D')
heading.pack(pady=20)

heading1 = tk.Label(text = ' Enter YouTube Video URL :',font = ('Arial',20,'bold'),bg='white',fg='black')
heading1.pack(pady=20)

video_link = tk.Entry(font = ('Arial',20),width=50,bg = 'light gray',highlightbackground ='#F7EED3',highlightthickness = 1)
video_link.pack(pady=10)

info_button = tk.Button(text="Video Info",font=('Arial',15,'bold'),width=50,fg='white',bg='#E85C0D', command=fetch_video_info,relief='ridge')
info_button.pack(pady=30)


quality_label = tk.Label(window , text="Select Video Quality :", font=("Arial", 14,'bold'),bg='blue')
quality_label.pack(anchor='s',pady=20)

quality_choice = tk.StringVar()
quality_dropdown = ttk.Combobox(textvariable=quality_choice, font=("Arial", 14))
quality_dropdown['values'] = ('1080p', '720p', '480p', '360p', '240p', '144p')
quality_dropdown.current(1)  # Default to 720p
quality_dropdown.pack(padx=10, pady=1)

video_btn = tk.Button(text = 'Download Video',font = ('Arial',15),width=15,fg='white',bg='green',command=download_video)
video_btn.pack(pady=15)

audio_btn = tk.Button(text = 'Download Audio',font = ('Arial',15),width=15,fg='white',bg='green',command=download_audio)
audio_btn.pack(pady=10)

window.mainloop()
