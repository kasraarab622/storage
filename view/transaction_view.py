from controller.transaction_controller import *
from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg


def reset_form():
    id.set(0)
    person_id.set(0)
    stuff_id.set(0)
    datetime.set("")
    count.set(0)
    type.set("")

    # clear table
    for i in table.get_children():
        table.delete(i)

    # insert into table
    for transaction in find_all:
        table.insert("", END, values=tuple(transaction.values()))


def save_click():
    status, data = save(stuff_id.get(), datetime.get(), count.get(), type.get())
    if status:
        msg.showinfo("Save", data)
        reset_form()
    else:
        msg.showerror("Save Error", data)


def edit_click():
    status, data = edit(id.get(), person_id.get(), stuff_id.get(), datetime.get(), count.get(),
                        type.get())
    if status:
        msg.showinfo("Edit", data)
        reset_form()
    else:
        msg.showerror("Edit Error", data)


def remove_click():
    if msg.askyesno("Are you sure"):
        status, data = remove(id.get())
        if status:
            msg.showinfo("Remove", data)
            reset_form()
        else:
            msg.showerror("Remove Error", data)


def table_select(event):
    transaction = table.item(table.focus())["values"]
    id.set(int(transaction[0]))
    person_id.set(int(transaction[1]))
    stuff_id.set(int(transaction[2]))
    datetime.set(transaction[3])
    count.set(int(transaction[4]))
    type.set(transaction[5])


win = Tk()
win.geometry('750x400')
win.title("Transaction")
win.resizable(0, 0)

# id
Label(win, text="ID").place(x=20, y=20)
id = IntVar()
Entry(win, textvariable=id, state="readonly").place(x=80, y=20)

# person_id
Label(win, text="Person ID").place(x=20, y=50)
person_id = IntVar()
Entry(win, textvariable=person_id).place(x=80, y=50)

# stuff_id
Label(win, text="Stuff ID").place(x=20, y=80)
stuff_id = IntVar()
Entry(win, textvariable=stuff_id).place(x=80, y=80)

# datetime
Label(win, text="DateTime").place(x=20, y=110)
datetime = StringVar()
Entry(win, textvariable=datetime).place(x=80, y=110)

# count
Label(win, text="Count").place(x=20, y=140)
count = IntVar()
Entry(win, textvariable=count).place(x=80, y=140)

# type
Label(win, text="Type").place(x=20, y=170)
type = StringVar()
Entry(win, textvariable=type).place(x=80, y=170)

table = ttk.Treeview(win, columns=(1, 2, 3, 4, 5, 6), show="headings")

table.column(1, width=60)
table.column(2, width=60)
table.column(3, width=60)
table.column(4, width=100)
table.column(5, width=60)
table.column(6, width=100)

table.heading(1, text="ID")
table.heading(2, text="PersonID")
table.heading(3, text="StuffID")
table.heading(4, text="DateTime")
table.heading(5, text="Count")
table.heading(6, text="Type")

table.place(x=250, y=10)

table.bind("<KeyRelease>", table_select)
table.bind("<ButtonRelease>", table_select)

#todo:not working
btn = Button(text="Save", width=8, command=save_click).place(x=50, y=300)
btn = Button(text="Edit", width=8, command=edit_click).place(x=120, y=300)
btn = Button(text="Remove", width=8, command=remove_click).place(x=190, y=300)

reset_form()

win.mainloop()
