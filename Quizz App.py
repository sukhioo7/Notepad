import tkinter as tk
import random

questions = [
    ("what function is used to print something to the console in python?", "print"),
    ("how do you create a list in python?", "using square brackets"),
    ("what is the symbol for a comment in python?", "#"),
    ("how do you create a string variable in python?", "using single or double quotes"),
    ("what function is used to get the length of a list?", "len"),
    ("how do you add an element to a list?", "append"),
    ("what is the keyword to define a function in python?", "def"),
    ("how do you start a for loop in python?", "for"),
    ("how do you start an if statement in python?", "if"),
    ("how do you check for equality in python?", "=="),
    ("what is the keyword to import a module in python?", "import"),
    ("how do you create a dictionary in python?", "using curly braces"),
    ("how do you create a tuple in python?", "using parentheses"),
    ("how do you check the type of a variable in python?", "type")
]

random.shuffle(questions)

current_question_number = 1
question_index = 0
correct_ans = 0
def show_questions():
    global current_question_number
    global question_index
    global correct_ans

    ans_area.delete(0.0,tk.END)

    if question_index<len(questions):
        sub_heading.config(text=f'Question {current_question_number} of {len(questions)}')
        question.config(text=f'Q) {questions[question_index][0]}')

        question_index = question_index + 1
        current_question_number = current_question_number + 1
    else:
        question.pack_forget()
        ans_area.pack_forget()
        submit_btn.pack_forget()
        sub_heading.config(text=f'Quiz Completed')
        secore_heading = tk.Label(text=f'Your Secore is {correct_ans}/{len(questions)}',
                                  font=('Harlow Solid Italic',25),fg='#084c61')
        secore_heading.pack(pady=30)

def check_ans():
    global correct_ans
    user_ans = ans_area.get(0.0,tk.END)
    user_ans = user_ans.lower()
    user_ans = user_ans.strip()

    # print(questions[question_index-1][1])

    if user_ans==questions[question_index-1][1]:
        correct_ans = correct_ans + 1
        print(correct_ans)

    show_questions()



    

window = tk.Tk()
window.title('Python Quiz')
window.geometry('600x700')

heading = tk.Label(text='Python Quiz',font=('Harlow Solid Italic',60),fg='#084c61')
heading.pack(pady=40)

sub_heading = tk.Label(text='Question 1 of 20',font=('Harlow Solid Italic',20),fg='#323031')
sub_heading.pack()

question = tk.Label(text='Q) What is python?',font=('Bahnschrift',15),wraplength=600)
question.pack(pady=13,anchor='w',padx=13)

ans_area = tk.Text(font=('Bahnschrift',13),relief='solid',width=63,height=10)
ans_area.pack()

submit_btn = tk.Button(text='Next',font=('Harlow Solid Italic',25),width=26,relief='solid',
                       bg='#db3a34',command=check_ans)
submit_btn.pack(pady=12)

show_questions()
window.mainloop()
