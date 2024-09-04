import tkinter as tk

def fetch_video_info():
    link = link_entry.get()

    info_window = tk.Toplevel(window)
    info_window.title('Video Information')
    info_window.geometry('1000x700')
    info_window.config(bg='white')

    heading = tk.Label(info_window,text='Video Information',
                    font=('Harlow Solid Italic', 55), bg='white', fg='#C63C51')
    heading.grid(row=1, column=1,padx=63,pady=30,columnspan=2)

    heading = tk.Label(info_window,text='Arithmetic & Assignment Operators | Python Practice Playlist | Python tutorial for beginners in 2024',
                    font=('Helvetica', 23,'bold'),wraplength=950,justify='left' ,bg='white', fg='#173B45')
    heading.grid(row=2, column=1,padx=10,columnspan=2)



    # author = yt.author
    # length = f"{yt.length // 60} minutes {yt.length % 60} seconds"
    # views = f"{yt.views:,}"  # Add commas to the view count

    gernal_info = f'''
Author : Punjabi CodeX
Length : 8 minutes 45 seconds
Views : 3434
'''
    
    gernal_heading = tk.Label(info_window,text=gernal_info,font=('Helvetica',14),bg='white',
                              justify='left',anchor='e')
    gernal_heading.grid(row=3, column=1,padx=10)

    keyword_area = tk.Text(info_window,width=60,height=4,font=('Helvetica',14),relief='solid',
                    )
    keyword_area.grid(row=3, column=2,padx=10)

    description_area = tk.Text(info_window,width=88,height=14,font=('Helvetica',14),relief='solid',
                    )
    description_area.grid(row=4, column=1,padx=10,columnspan=2)


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
                         bg='#522258',fg='white',width=20,relief='solid')
get_info_btn.grid(row=4, column=1)

download_btn = tk.Button(text='Download Video',font=('Harlow Solid Italic',20),
                         bg='#8C3061',fg='white',width=20,relief='solid')
download_btn.grid(row=5, column=1,pady=10)


window.mainloop()
