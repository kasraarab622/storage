from tkinter import *
from controller.stuffgroup_controller import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg

def reset_form():
    id.set(0)
    title.set("")
    parent_id.set(0)

    # clear table
    for i in table.get_children():
        table.delete(i)

    # insert into table
    for stuffgroup in find_all():
        table.insert("", END, values=tuple(stuffgroup.values()))

def save_click():
    status , data = save(title.get(),parent_id.get())
    if status:
        msg.showinfo("Save",data)
        reset_form()
    else:
        msg.showerror("SaveError",data)

def edit_click():
    status , data = edit(id.get(),title.get(),parent_id.get())
    if status:
        msg.showinfo("Edit",data)
        reset_form()
    else:
        msg.showerror("EditError",data)
def remove_click():
    if msg.askyesno("Are you sure?"):
        status , data = remove(id.get())
        if status:
            msg.showinfo("Remove",data)
            reset_form()
        else:
            msg.showerror("RemoveError")

def table_select(event):
    stuffgroup = table.item(table.focus())["values"]
    id.set(stuffgroup[0])
    title.set(stuffgroup[1])
    parent_id.set(stuffgroup[2])

win = Tk()
win.geometry("550x400")
win.title("Stuffgroup")

# id
Label(win, text="ID").place(x=20, y=20)
id = IntVar()
Entry(win, textvariable=id, state="readonly").place(x=80, y=20)

# title
Label(win, text="Title").place(x=20, y=50)
title = StringVar()
Entry(win, textvariable=title).place(x=80, y=50)

# parent_id
Label(win, text="ParentID").place(x=20, y=80)
parent_id = IntVar()
Entry(win, textvariable=parent_id).place(x=80, y=80)

table = ttk.Treeview(win, columns=(1, 2, 3), show="headings")

table.column(1, width=60)
table.column(2, width=60)
table.column(3, width=60)

table.heading(1, text="ID")
table.heading(2, text="Title")
table.heading(3, text="ParentID")

table.place(x=300, y=10)

table.bind("<KeyRelease>",table_select)
table.bind("<ButtonRelease>",table_select)

#todo:not working
btn = Button(win, text="Save", width=8, command=save_click).place(x=20, y=250)
btn = Button(win, text="Edit", width=8, command=edit_click).place(x=90, y=250)
btn = Button(win, text="Remove", width=8, command=remove_click).place(x=160, y=250)

reset_form()

win.mainloop()
