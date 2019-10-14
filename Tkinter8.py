from tkinter import *

root = Tk()

root.title("StopWatch")

label_1 = Label(root, width=5, font="Ubuntu 100", text="00:00")
label_1.grid(row=0, columnspan=2)

root.mainloop()
