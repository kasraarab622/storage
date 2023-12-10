from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from controller.stuff_controller import StuffController

stuff_list = []


def reset_form():
    id.set(0)
    name.set("")
    brand.set("")
    description.set("")
    groupid.set(0)

    # clear table rows
    for item in table.get_children():
        table.delete(item)

        # insert persons to table

    for stuff in find_all():
        table.insert("", END, values=stuff)


def save_click():
    status, data = save(name.get(), brand.get(), description.get(), groupid.get())
    if status:
        msg.showinfo("Save", data)
        reset_form()
    else:
        msg.showerror("Save Error", data)


def edit_click():
    status, data = edit(id.get(), name.get(), brand.get(), description.get(), groupid.get())
    if status:
        msg.showinfo("Edit", data)
        reset_form()

    else:
        msg.showerror("Edit Error", data)


def remove_click():
    if msg.askyesno("Remove""Are you sure?"):
        status, data = remove(id.get())
        if status:
            msg.showinfo("Remove", data)
            reset_form()
        else:
            msg.showerror("Remove Error", data)


def table_click(event):
    row_index = table.focus()
    stuff = table.item(row_index)["values"]
    id.set(int(stuff[0]))
    name.set(stuff[1])
    brand.set(stuff[2])
    description.set(stuff[3])
    groupid.set(stuff[4])


def close_from():
    if msg.askyesno("Exit", "Are you sure?"):
        win.destroy()


win = Tk()
win.title("Stuff Info")
win.geometry("800x400")
win.protocol("WM_DELETE_WINDOW", close_from)
win.resizable(0, 0)

# id
Label(win, text="Id").place(x=20, y=20)
id = IntVar()
Entry(win, textvariable=id, state="readonly").place(x=90, y=20)

# name
Label(win, text="Name").place(x=20, y=60)
name = StringVar()
Entry(win, textvariable=name).place(x=90, y=60)

# brand
Label(win, text="Brand").place(x=20, y=100)
brand = StringVar()
Entry(win, textvariable=brand).place(x=90, y=100)

# description
Label(win, text="Description").place(x=20, y=140)
description = StringVar()
Entry(win, textvariable=description).place(x=90, y=140)

# groupid
Label(win, text="GroupId").place(x=20, y=180)
groupid = IntVar()
Entry(win, textvariable=groupid).place(x=90, y=180)

table = ttk.Treeview(win, columns=(1, 2, 3, 4, 5), show="headings")

table.column(1, width=60)
table.column(2, width=100)
table.column(3, width=100)
table.column(4, width=100)
table.column(5, width=60)

table.heading(1, text="Id")
table.heading(2, text="Name")
table.heading(3, text="Brand")
table.heading(4, text="Description")
table.heading(5, text="GroupId")

table.place(x=300, y=20)

table.bind("<ButtonRelease>", table_click)
table.bind("<KeyRelease>", table_click)
Button(win, text="Save", width=8, command=save_click).place(x=300, y=300)
Button(win, text="Edit", width=8, command=edit_click).place(x=400, y=300)
Button(win, text="Remove", width=8, command=remove_click).place(x=500, y=300)

reset_form()

win.mainloop()
