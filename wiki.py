import tkinter as tk
import wikipedia 

def result():
    query = user_search.get()
    print(query)
    try:
        result = wikipedia.summary(query,sentences = 2)
        result_label.config(text=result,font=('Bell MT',17),wraplength=600,relief='ridge',padx=20,pady=20,fg='black')
    except:
        result_label.config(text='No Data Found',fg='#B22222',font=('Bell MT',17),wraplength=600,relief='ridge',padx=20,pady=20)
        

window = tk.Tk()
window.title('Wikipedia')
window.geometry('650x700')
window.resizable(0.0,0.0)

heading = tk.Label(text='WikipediA',font=('Bell MT',80),fg='#2E8B57')
heading.pack(pady=15)

search = tk.Label(text='Search Here',font=('Bell MT',28))
search.pack()

user_search = tk.Entry(font=('Bell MT',18),width=35)
user_search.pack(pady=8)


search_btn = tk.Button(text='Search',font=('Bell MT',18,'bold'),padx=170,bg='#2E8B57',fg='white',relief='ridge',command=result)
search_btn.pack()

result_label = tk.Label(text='')
result_label.pack(pady=20)

window.mainloop()
