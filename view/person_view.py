from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from controller.person_controller import *
from model.entity.person import Person

person_list = []


def reset_form():
    id.set(len(person_list) + 1)
    name.set("")
    family.set("")
    phone_number.set("")
    email.set("")
    username.set("")
    password.set("")

    # clean table items
    for item in table.get_children():
        table.delete(item)

    # insert items
    for person in person_list:
        table.insert("", END, values=tuple(person.values()))


def table_click(event):
    index = table.focus()
    person = table.item(index)["values"]
    id.set(int(person[0]))
    name.set(person[1])
    family.set(person[2])
    phone_number.set(person[3])
    email.set(person[4])
    username.set(person[5])
    password.set(person[6])


def save_click():
    person = {
        'id': id.get(),
        "name": name.get(),
        'family': family.get(),
        "phone_number": phone_number.get(),
        "email": email.get(),
        "username": username.get(),
        "password": password.get()
    }
    person_list.append(person)
    table.insert("", END, values=person)
    msg.showinfo("Save", person)
    reset_form()


# def edit_click():
#     status , data =PersonController.edit(id.get(),name.get(),family.get(),phone_number.get(),email.get(),username.get(),password.get())
#     if status:
#         person_list[id.get()-1]=Person
#         msg.showinfo("Edit",data)
#         reset_form()
#     else:
#         msg.showerror("EditError",data)
#
# def remove_click():
#     if msg.askyesno("Are you sure?"):
#         status , data =PersonController.remove(id.get())
#         if status:
#             table.delete(Person)
#             msg.showinfo("Remove",data)
#             reset_form()
#         else:
#             msg.showerror("RemoveError",data)


win = Tk()
win.geometry("800x400")
win.title("Person")

# id
Label(win, text="ID").place(x=20, y=20)
id = IntVar()
Entry(win, textvariable=id, state="readonly").place(x=80, y=20)

# name
Label(win, text="Name").place(x=20, y=50)
name = StringVar()
Entry(win, textvariable=name).place(x=80, y=50)

# family
Label(win, text="Family").place(x=20, y=80)
family = StringVar()
Entry(win, textvariable=family).place(x=80, y=80)

# phone_number
Label(win, text="Phone").place(x=20, y=110)
phone_number = StringVar()
Entry(win, textvariable=phone_number).place(x=80, y=110)

# email
Label(win, text="Email").place(x=20, y=140)
email = StringVar()
Entry(win, textvariable=email).place(x=80, y=140)

# user
Label(win, text="User").place(x=20, y=170)
username = StringVar()
Entry(win, textvariable=username).place(x=80, y=170)

# password
Label(win, text="Password").place(x=20, y=200)
password = StringVar()
Entry(win, textvariable=password).place(x=80, y=200)

table = ttk.Treeview(win, columns=(1, 2, 3, 4, 5), show="headings")

table.heading(1, text="ID")
table.heading(2, text="Name")
table.heading(3, text="Family")
table.heading(4, text="Phone")
table.heading(5, text="Email")

table.column(1, width=70)
table.column(2, width=100)
table.column(3, width=100)
table.column(4, width=100)
table.column(5, width=100)

table.place(x=250, y=20)

table.bind("<ButtonRelease>", table_click)
table.bind("<KeyRelease>", table_click)

Button(win, text="Save", width=10, command=save_click).place(x=20, y=300)
# Button(win, text="Edit", width=10, command=edit_click).place(x=185, y=300)
# Button(win, text="Remove", width=10, command=remove_click).place(x=350, y=300)

reset_form()

win.mainloop()
