# https://www.youtube.com/watch?v=3sf2MRgLNN0&list=PLfAlku7WMht4Vm6ewLgdP9Ou8SCk4Zhar
from tkinter import *

root = Tk()

top_frame = Frame(root)
top_frame.pack()

bottom_frame = Frame(root)
bottom_frame.pack(side=BOTTOM)

button_1 = Button(top_frame, text="Button1", fg="red")
button_2 = Button(top_frame, text="Button2", fg="blue")
button_3 = Button(top_frame, text="Button3", fg="green")
button_4 = Button(bottom_frame, text="Button4", fg="grey")
button_5 = Button(bottom_frame, text="Button5", fg="grey")

button_1.pack(side=LEFT)
button_2.pack(side=LEFT)
button_3.pack(side=LEFT)
button_4.pack(side=LEFT)
button_5.pack(side=BOTTOM)

root.mainloop()
