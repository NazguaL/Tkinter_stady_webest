from tkinter import *
from tkinter import messagebox as mb


def ask_question(event):
    answer = mb.askquestion("Ask Question", "Question 1")
    label1.configure(text=answer)


def ask_ok_cancel(event):
    answer = mb.askokcancel("Ask Ok Cancel", "Question 2")
    label2.configure(text=answer)


def ask_yes_no(event):
    answer = mb.askyesno("Ask Ok Cancel", "Question 3")
    label3.configure(text=answer)


def ask_retry_cancel(event):
    answer = mb.askretrycancel("Ask Retry Cancel", "Question 4")
    label4.configure(text=answer)


root = Tk()

btn1 = Button(root, text="Ask Question", font="Ubuntu 20", width=20)
btn1.grid(row=0, column=0, sticky="w")

label1 = Label(root, font="Ubuntu 20", width=20)
label1.grid(row=0, column=1)

btn1.bind("<Button-1>", ask_question)


btn2 = Button(root, text="Ask Ok Cancel", font="Ubuntu 20", width=20)
btn2.grid(row=1, column=0, sticky="w")

label2 = Label(root, font="Ubuntu 20", width=20)
label2.grid(row=1, column=1)

btn2.bind("<Button-1>", ask_ok_cancel)


btn3 = Button(root, text="Ask Yes No", font="Ubuntu 20", width=20)
btn3.grid(row=2, column=0, sticky="w")

label3 = Label(root, font="Ubuntu 20", width=20)
label3.grid(row=2, column=1)

btn3.bind("<Button-1>", ask_yes_no)


btn4 = Button(root, text="Ask Retry Cancel", font="Ubuntu 20", width=20)
btn4.grid(row=3, column=0, sticky="w")

label4 = Label(root, font="Ubuntu 20", width=20)
label4.grid(row=3, column=1)

btn4.bind("<Button-1>", ask_retry_cancel)


root.mainloop()
