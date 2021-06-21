from canvas import tk
from tkinter import Button, Label, Entry
from gui_shop_by_milen.helpers import clean_screen


def register():
    pass


def login(user, pword):
    pass

def render_register():
    clean_screen()
    username = Entry(tk)
    username.grid(row=0, column=0)
    password = Entry(tk)
    password.grid(row=1, column=0)
    first_name = Entry(tk)
    first_name.grid(row=2, column=0)
    last_name = Entry(tk)
    last_name.grid(row=3, column=0)
    # Make validations for names lenght and username to be unique and with no special chars
    Button(
        tk,
        text="Register", bg="green",
        command=lambda: register(username=username.get(), password=password.get(), first_name=first_name.get(),
                                 last_name=last_name.get())).grid(row=4,
                                                                  column=0)


def render_login(error=None):
    clean_screen()
    username = Entry(tk)
    username.grid(row=0, column=0)
    password = Entry(tk)
    password.grid(row=1, column=0)

    if error is not None:
        Label(tk, text="Invalid username or password").grid(row=3, column=0)
    Button(tk, text="Enter", bg="green", command=lambda: login(username.get(), password.get())).grid(row=2, column=0)


def render_register():
    clean_screen()
    Label(tk, text="Username").place(x=30, y=20)
    Entry(tk)
    Label(tk, text="Password").place(x=30, y=40)
    Entry(tk)
    Label(tk, text="First Name").place(x=30, y=60)


def render_main_enter_screen():
    Button(tk, text="Login",
           command=render_login).place(x= 30, y= 20)
    Button(tk, text="Register",
           command=render_register).place(x=80, y=20)
