from tkinter import *


def new_win():
    win = Toplevel(root)
    label_1 = Label(win, text="Some text", font=20)
    label_1.pack()


def exit_app():
    root.destroy()


root = Tk()

main_menu = Menu(root)
root.configure(menu=main_menu)

first_item = Menu(main_menu)
main_menu.add_cascade(label="File", menu=first_item)
first_item.add_command(label="New", command=new_win)
first_item.add_command(label="Exit", command=exit_app)

second_item = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="edit", menu=second_item)
second_item.add_command(label="item_1")
second_item.add_command(label="item_2")
second_item.add_command(label="item_3")
second_item.add_separator()
second_item.add_command(label="item_4")

root.mainloop()
