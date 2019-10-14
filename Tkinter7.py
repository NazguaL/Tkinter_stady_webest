# https://www.youtube.com/watch?v=bh9zsbaLaGs&list=PLfAlku7WMht4Vm6ewLgdP9Ou8SCk4Zhar&index=7
from tkinter import *


def print_char(event):
    label_1.configure(text=event.char)

root = Tk()

label_1 = Label(root, width=12, font="ubuntu 12")
label_1.pack()

for i in range(61, 127):
    root.bind(chr(i), print_char)

root.mainloop()
