from tkinter import *

root = Tk()

text_label = Label(root, text="Text!!!", fg="red", bg="yellow")
text_label.pack()

text_label = Label(root, text="Text!!!", fg="green", bg="yellow")
text_label.pack(fill=X)

text_label = Label(root, text="Text!!!", fg="blue", bg="yellow")
text_label.pack(side=LEFT, fill=Y)

root.mainloop()
