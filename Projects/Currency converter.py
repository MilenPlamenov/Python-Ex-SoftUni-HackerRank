from tkinter import *
expression = ""


def clear():
        amount.set("")


def equalpress():
    try:
        global expression
        total = str(amount.get() * 0.61)
        amount.set(total)
        expression = ""
    except:
        amount.set("Invalid expression")
        expression = ""


window = Tk()
window.geometry("350x350")
window.title("Currency converter")
amount = IntVar()
Label(window, text="Currency converter",width=19, font ='arial 20 bold').grid(row=0,column=0)
Label(window, text="Enter your amount", font="bold").place(x = 2, y = 57)
amount_enter = Entry(window, width = 20,textvariable = amount).place(x = 140, y = 60)
Label(text="From BGN to:", font="bold").place(x = 10, y = 100)
Label(window,text="USD",font="bold").place(x=140, y=100)
Button(window,text="Convert",width=19, font ='arial 14 bold',
       command=equalpress).place(x=45, y=160)


Button(window,text="Clear",width=19, font ='arial 14 bold',
       command=clear).place(x=45, y=280)
window.mainloop()


