import tkinter as tk


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
