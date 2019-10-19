from tkinter import *


class Question:

    def __init__(self, main):
        self.entry_1 = Entry(main, width=3, font=15)
        self.button_1 = Button(main, text="Check")
        self.label_1 = Label(root, width=36, font=15)

        self.entry_1.grid(row=0, column=0)
        self.button_1.grid(row=0, column=1)
        self.label_1.grid(row=0, column=2)

        self.button_1.bind("<Button-1>", self.answer)


    def answer(self, event):
        txt = self.entry_1.get()

        try:
            if int(txt) < 18:
                self.label_1["text"] = "You are too yong to enter here!"
            else:
                self.label_1["text"] = "You are welcome!"
        except ValueError:
            self.label_1["text"] = "You have entered not an integer!"

root = Tk()
root.title("How old are you?")

q = Question(root)

root.mainloop()