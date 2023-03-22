import tkinter as tk
from datetime import datetime as dt

def real_clock():
    curr_time = dt.now().strftime("%I:%M:%S %p")
    real_time.config(text=curr_time)

    curr_date = dt.now().strftime("%d-%b-%Y")
    real_date.config(text=curr_date)

    curr_day = dt.now().strftime("%A")
    real_day.config(text=curr_day)

    root.after(1000,real_clock)


root = tk.Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title('Digital Clock')
root.config(padx=25,pady=20,bg='black')
# Fixedsys

heading_digital = tk.Label(text='Digital Clock',font=('Forte',35),fg='white',bg='black')

heading_time = tk.Label(text="Time ",font=('Copperplate Gothic Bold',28),fg='white',bg='black')
heading_date = tk.Label(text="Date ",font=('Copperplate Gothic Bold',28),fg='white',bg='black')
heading_day = tk.Label(text="Day ",font=('Copperplate Gothic Bold',28),fg='white',bg='black')

real_time = tk.Label(text='',font=('Fixedsys',28),fg='#00755E',bg='black')
real_date = tk.Label(text='',font=('Fixedsys',28),fg='#00755E',bg='black')
real_day = tk.Label(text='',font=('Fixedsys',28),fg='#00755E',bg='black')

heading_digital.grid(row=1,column=1,columnspan=2,pady=10,sticky='w')

heading_time.grid(row=2,column=1,sticky='w')
heading_date.grid(row=3,column=1,sticky='w')
heading_day.grid(row=4,column=1,sticky='w')

real_time.grid(row=2,column=2,sticky='w')
real_date.grid(row=3,column=2,sticky='w')
real_day.grid(row=4,column=2,sticky='w')

real_clock()

root.mainloop()
