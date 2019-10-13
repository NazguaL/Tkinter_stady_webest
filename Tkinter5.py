from tkinter import *


def output(event):
    txt = entry_1.get()
    try:
        if int(txt) < 18:
            label_1["text"] = "You are too yong to enter here!"
        else:
            label_1["text"] = "You are welcome!"
    except ValueError:
        label_1["text"] = "You have entered not an integer!"

root = Tk()
root.title("How old are you?")

entry_1 = Entry(root, width=4, font=15)
button_1 = Button(root, text="Check")
label_1 = Label(root, width=36, font=15, anchor=W)

entry_1.grid(row=0, column=0)
button_1.grid(row=0, column=1)
label_1.grid(row=0, column=2)

button_1.bind("<Button-1>", output)

root.mainloop()
