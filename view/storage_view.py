from tkinter import *
import tkinter.ttk as ttk
from controller.storage_conntroller import *
import tkinter.messagebox as msg


def reset_from():
    id.set(0)
    stuff_id.set(0)
    count.set(0)

    # clear table
    for item in table.get_children():
        table.delete(item)

    for storage in find_all():
        table.insert("", END, values=tuple(storage.values()))


def save_click():
    status, data = save(stuff_id.get(), count.get())
    if status:
        msg.showinfo("Save", data)
        reset_from()
    else:
        msg.showerror("SaveError", data)


def edit_click():
    status, data = edit(id.get(), stuff_id.get(), count.get())
    if status:
        msg.showinfo("Edit", data)
        reset_from()
    else:
        msg.showerror("EditError", data)


def remove_click():
    if msg.askyesno("Are you sure?"):
        status, data = remove(id.get())
        if status:
            msg.showinfo("Remove", data)
            reset_from()
        else:
            msg.showerror("RemoveError")


def table_select(event):
    storage = table.item(table.focus())["values"]
    id.set(storage[0])
    stuff_id.set(storage[1])
    count.set(storage[2])


win = Tk()
win.geometry("550x400")
win.title("Storage")

# id
Label(win, text="ID").place(x=20, y=40)
id = IntVar()
Entry(win, textvariable=id, state="readonly").place(x=80, y=40)

# stuff_id
Label(win, text="StuffID").place(x=20, y=70)
stuff_id = IntVar()
Entry(win, textvariable=stuff_id).place(x=80, y=70)

# count
Label(win, text="Count").place(x=20, y=100)
count = IntVar()
Entry(win, textvariable=count).place(x=80, y=100)

table = ttk.Treeview(win, columns=(1, 2, 3), show='headings')

table.column(1, width=60)
table.column(2, width=60)
table.column(3, width=60)

table.heading(1, text="ID")
table.heading(2, text="StuffID")
table.heading(3, text="Count")

table.place(x=300, y=30)

table.bind('<KeyRelease>', table_select)
table.bind('<ButtonRelease>', table_select)

#todo:buttons not working
btn = Button(win, text="Save", width=8, command=save_click).place(x=20, y=250)
btn = Button(win, text="Edit", width=8, command=save_click).place(x=90, y=250)
btn = Button(win, text="Remove", width=8, command=save_click).place(x=160, y=250)

reset_from()

win.mainloop()
