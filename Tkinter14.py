from tkinter.filedialog import *
from tkinter import *
from tkinter.messagebox import *


def open_file():
    of = askopenfilename()
    file = open(of, "r")
    txt.insert(END, file.read())
    file.close()


def save_file():
    sf = asksaveasfilename()
    final_text = txt.get(1.0, END)
    file = open(sf, "w")
    file.write(final_text)
    file.close()

root = Tk()

main_menu = Menu(root)
root.configure(menu=main_menu)

first_item = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="File", menu=first_item)

first_item.add_command(label="Open", command=open_file)
first_item.add_command(label="Save", command=save_file)
first_item.add_command(label="Exit", command=lambda: root.quit())

txt = Text(root, width=40, height=15, font=12)
txt.pack(expand=YES, fill=BOTH)

root.mainloop()
