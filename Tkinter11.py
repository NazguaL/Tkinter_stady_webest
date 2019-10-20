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

toolbar = Frame(root)
toolbar.pack(side=TOP, fill=X)

btn1 = Button(toolbar, text="Cut")
btn1.grid(row=0, column=0, padx=2, pady=2)
btn2 = Button(toolbar, text="Copy")
btn2.grid(row=0, column=1, padx=2, pady=2)
btn3 = Button(toolbar, text="Paste")
btn3.grid(row=0, column=2, padx=2, pady=2)

status_bar = Label(root, relief=SUNKEN, anchor=W, text="Mission complete")
status_bar.pack(side=BOTTOM, fill=X)

root.mainloop()
