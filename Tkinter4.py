from tkinter import *

root = Tk()

text_label_1 = Label(root, text="name")
text_label_2 = Label(root, text="password")

entry_1 = Entry(root)
entry_2 = Entry(root)

text_label_1.grid(row=0, column=0, sticky=E)
text_label_2.grid(row=1, column=0)

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)


c = Checkbutton(root, text="Stay logged in")

c.grid(columnspan=2)

root.mainloop()
