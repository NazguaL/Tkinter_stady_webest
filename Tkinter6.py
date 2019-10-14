from tkinter import *


def left_click(event):
    frame_1.configure(bg="red")
    frame_2.configure(bg="white")
    frame_3.configure(bg="white")


def central_click(event):
    frame_1.configure(bg="white")
    frame_2.configure(bg="red")
    frame_3.configure(bg="white")


def right_click(event):
    frame_1.configure(bg="white")
    frame_2.configure(bg="white")
    frame_3.configure(bg="red")

root = Tk()

root.configure(bg="black")

frame_1 = Frame(root, width=250, height=250, bg="white")
frame_2 = Frame(root, width=250, height=250, bg="white")
frame_3 = Frame(root, width=250, height=250, bg="white")

frame_1.grid(row=0, column=0)
frame_2.grid(row=0, column=1, padx=1)
frame_3.grid(row=0, column=2)

root.bind("<Button-1>", left_click)
root.bind("<Button-2>", central_click)
root.bind("<Button-3>", right_click)

root.mainloop()
