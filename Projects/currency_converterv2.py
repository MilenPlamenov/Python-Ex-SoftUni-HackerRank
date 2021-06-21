from tkinter import Tk, IntVar, StringVar, Button, Label, Entry, OptionMenu

expression = ""


def clear():
    amount.set("")


def equalpress():
    try:
        global expression
        current_currency = variable.get()
        if current_currency == "USD":
            total = str(amount.get() * 0.61)
            amount.set(total)
        elif current_currency == "EUR":
            total = str(amount.get() * 0.51)
            amount.set(total)
        elif current_currency == "INR":
            total = str(amount.get() * 46.05)
            amount.set(total)
        elif current_currency == "RUB":
            total = str(amount.get() * 46.23)
            amount.set(total)
        elif current_currency == "TRY":
            total = str(amount.get() * 4.95)
            amount.set(total)
        expression = ""
    except:
        amount.set("Invalid expression")
        expression = ""


OPTIONS = [
    "RUB",
    "USD",
    "TRY",
    "INR",
    "EUR",
]
if __name__ == "__main__":
    window = Tk()
    window.geometry("350x350")
    window.title("Currency converter")
    amount = IntVar()
    variable = StringVar(window)
    variable.set(OPTIONS[4])

    Label(window, text="Currency converter", width=20, font='arial 20 bold').grid(row=0, column=0)
    Label(window, text="Enter your amount:", font="bold").place(x=2, y=57)
    Entry(window, width=20, textvariable=amount, selectborderwidth=10).place(x=150, y=60)
    Label(text="From BGN to:", font="bold").place(x=20, y=100)
    OptionMenu(window, variable, *OPTIONS).place(x=140, y=95)
    Button(window, text="Convert", width=19, font='arial 14 bold', bg="green", bd=5,
           command=equalpress).place(x=45, y=160)
    Button(window, text="Clear", width=19, font='arial 14 bold', bg="red", bd=5,
           command=clear).place(x=45, y=250)

    window.mainloop()
