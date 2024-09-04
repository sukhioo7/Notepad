import tkinter as tk
from pytubefix import YouTube
from pytubefix.cli import on_progress

def fetch_video_info():
    link = link_entry.get()
    yt = YouTube(link, on_progress_callback = on_progress)

    title = yt.title
    author = yt.author
    length = f"{yt.length // 60} minutes {yt.length % 60} seconds"
    views = f"{yt.views:,}"  # Add commas to the view count

    info_window = tk.Toplevel(window)
    info_window.title('Video Information')
    info_window.geometry('1000x700')
    info_window.config(bg='white')

    heading = tk.Label(info_window,text='Video Information',
                    font=('Harlow Solid Italic', 55), bg='white', fg='#C63C51')
    heading.grid(row=1, column=1,padx=63,pady=30,columnspan=2)

    heading = tk.Label(info_window,text=title,
                    font=('Helvetica', 23,'bold'),wraplength=950,justify='left' ,bg='white', fg='#173B45')
    heading.grid(row=2, column=1,padx=10,columnspan=2)

    gernal_info = f'''
Author : {author}
Length : {length}
Views : {views}
'''
    
    gernal_heading = tk.Label(info_window,text=gernal_info,font=('Helvetica',14),bg='white',
                              justify='left',anchor='e')
    gernal_heading.grid(row=3, column=1,padx=10)

    keyword_area = tk.Text(info_window,width=60,height=4,font=('Helvetica',14),relief='solid',
                    )
    keyword_area.grid(row=3, column=2,padx=10)

    keyword_area.delete(0.0,tk.END)
    keyword_area.insert(0.0, yt.keywords)

    description_area = tk.Text(info_window,width=88,height=14,font=('Helvetica',14),relief='solid',
                    )
    description_area.grid(row=4, column=1,padx=10,columnspan=2)

    description_area.delete(0.0,tk.END)
    description_area.insert(0.0, yt.description)



window = tk.Tk()
window.title('YoyTube Downloader')
window.geometry('800x500')
window.config(bg='white')

heading = tk.Label(text='YouTube Downloader',
                    font=('Harlow Solid Italic', 55), bg='white', fg='#C63C51')
heading.grid(row=1, column=1,padx=63,pady=50)

sub_heading = tk.Label(text='Paste your link here...',font=('Helvetica',22,'italic'),
                       bg='white',fg='#758694')
sub_heading.grid(row=2, column=1,padx=63)

link_entry = tk.Entry(font=('Helvetica', 18), width=40, bg='lightgray', relief='flat')
link_entry.grid(row=3, column=1,pady=20)

get_info_btn = tk.Button(text='Get info',font=('Harlow Solid Italic',20),
                         bg='#522258',fg='white',width=20,relief='solid',command=fetch_video_info)
get_info_btn.grid(row=4, column=1)

download_btn = tk.Button(text='Download Video',font=('Harlow Solid Italic',20),
                         bg='#8C3061',fg='white',width=20,relief='solid')
download_btn.grid(row=5, column=1,pady=10)


window.mainloop()
