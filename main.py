from tkinter import *
import logic as r
import os

root = Tk()
frame = Frame(root, bg='grey')
frame.pack()
root.geometry('300x300')
root.title('login')
root.configure(bg='grey')
usr_var = StringVar()
pas_var = StringVar()


def lg(u, p):
    r.login(u, p)
    ent1.delete(0, END)
    ent2.delete(0, END)
    for widget in frame.winfo_children():
        widget.destroy()

    if r.hel == 'true':
        Label(frame, text=f'Hi welcome {u}').pack()
    elif r.hel == 'false':
        Label(frame, text='enter proper userid and password').pack()
    else:
        Label(frame, text='enter proper userid and password').pack()

    return


def reg(u, p):
    r.reg(u, p)
    ent1.delete(0, END)
    ent2.delete(0, END)
    for widget in frame.winfo_children():
        widget.destroy()
    if r.he == 'true':
        Label(frame, text=f'Hi welcome {u}').pack()
    elif r.he == 'false':
        Label(frame, text='enter proper userid and password').pack()
    else:
        Label(frame, text='enter proper userid and password').pack()

    return


Label(frame, text='Enter the following ', bg='grey', height=4, width=300).pack()

lab1 = Label(frame, text='Username', bg='grey').pack()
ent1 = Entry(frame, textvariable=usr_var)
ent1.pack()

Label(frame, text='', bg='grey').pack()
lab2 = Label(frame, text='Password', bg='grey').pack()
ent2 = Entry(frame, textvariable=pas_var)
ent2.pack()
btn1 = Button(frame, text='Login', command=lambda: lg(usr_var.get(), pas_var.get())).pack()
btn2 = Button(frame, text='Register', command=lambda: reg(usr_var.get(), pas_var.get())).pack()

root.mainloop()
