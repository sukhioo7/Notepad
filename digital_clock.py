import tkinter as tk 
from datetime import datetime

def real_time_date():
    current_time = datetime.now().strftime('%I : %M : %S %p')
    real_time.config(text=current_time)

    current_day = datetime.now().strftime('%A')
    real_day.config(text=current_day)

    current_date = datetime.now().strftime(' %d - %b - %Y')
    real_date.config(text=current_date)
    
    root.after(1000,real_time_date)


root = tk.Tk()
root.title('Digital Clock')
root.geometry('500x300')
root.config(padx=30,pady=30,bg='#00BFFF')

main_heading = tk.Label(root,text='Digital Clock',font=('MV Boli',34),bg='#00BFFF',fg='#ffdf00')

time_label = tk.Label(root,text="Time : ",font=('Verdana',23),bg='#00BFFF',fg='white')
day_label = tk.Label(root,text="Day : ",font=('Verdana',23),bg='#00BFFF',fg='white')
date_label = tk.Label(root,text="Date : ",font=('Verdana',23),bg='#00BFFF',fg='white')

real_time = tk.Label(root,text='',font=('Yu Gothic UI Semibold',23),bg='#00BFFF',fg='white')
real_day = tk.Label(root,text='',font=('Yu Gothic UI Semibold',23),bg='#00BFFF',fg='white')
real_date = tk.Label(root,text='',font=('Yu Gothic UI Semibold',23),bg='#00BFFF',fg='white')

main_heading.grid(row=0,column=0,columnspan=2,padx=30)
time_label.grid(row=1,column=0,padx=30)
day_label.grid(row=2,column=0,padx=30)
date_label.grid(row=3,column=0,padx=30)

real_time.grid(row=1,column=1)
real_day.grid(row=2,column=1)
real_date.grid(row=3,column=1)


real_time_date()
root.mainloop()