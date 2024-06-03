from tkinter import *

global first_num
global op


# To add numbers to text box
def button_click(num):
    e.insert(END, num)


def button_clr():
    e.delete(0, END)


def button_back():
    b = e.get()
    e.delete(0, END)
    e.insert(0, b[:-1])


def button_add():
    global first_num
    global op
    op = "add"
    first_num = e.get()
    e.delete(0, END)


def button_sub():
    global first_num
    global op
    op = "sub"
    first_num = e.get()
    e.delete(0, END)


def button_multiply():
    global first_num
    global op
    op = "mul"
    first_num = e.get()
    e.delete(0, END)


def button_divide():
    global first_num
    global op
    op = "div"
    first_num = e.get()
    e.delete(0, END)


def button_modu():
    global first_num
    global op
    op = "mod"
    first_num = e.get()
    e.delete(0, END)


def button_sqr():
    global first_num
    global op
    op = "sq"
    first_num = e.get()
    e.delete(0, END)


def button_root():
    global first_num
    global op
    op = "rt"
    first_num = e.get()
    e.delete(0, END)


def button_equal():
    second_num = e.get()
    e.delete(0, END)
    global op
    if op == "add":
        e.insert(0, str(float(first_num) + float(second_num)))
    elif op == "sub":
        e.insert(0, str(float(first_num) - float(second_num)))
    elif op == "mul":
        e.insert(0, str(float(first_num) * float(second_num)))
    elif op == "div":
        e.insert(0, str(float(first_num) / float(second_num)))
    elif op == "mod":
        e.insert(0, str(float(first_num) % float(second_num)))
    elif op == "sq":
        e.insert(0, str(float(first_num) ** float(second_num)))
    elif op == "rt":
        e.insert(0, str(float(first_num) ** (1 / float(second_num))))


# Creating window
w = Tk()
w.title("Simple Calculator")
w.iconbitmap("D:\\Programming\\Projects\\images\\calc.ico")

# Textbox
e = Entry(w, width=50, borderwidth=7, fg="white", bg="black", font=("Times", 10, "bold"),
          justify="right")
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Defining buttons
button0 = Button(w, text="0", bg="cyan", padx=40, pady=20, command=lambda: button_click(0))
button1 = Button(w, text="1", bg="cyan", padx=40, pady=20, command=lambda: button_click(1))
button2 = Button(w, text="2", bg="cyan", padx=40, pady=20, command=lambda: button_click(2))
button3 = Button(w, text="3", bg="cyan", padx=40, pady=20, command=lambda: button_click(3))
button4 = Button(w, text="4", bg="cyan", padx=40, pady=20, command=lambda: button_click(4))
button5 = Button(w, text="5", bg="cyan", padx=40, pady=20, command=lambda: button_click(5))
button6 = Button(w, text="6", bg="cyan", padx=40, pady=20, command=lambda: button_click(6))
button7 = Button(w, text="7", bg="cyan", padx=40, pady=20, command=lambda: button_click(7))
button8 = Button(w, text="8", bg="cyan", padx=40, pady=20, command=lambda: button_click(8))
button9 = Button(w, text="9", bg="cyan", padx=40, pady=20, command=lambda: button_click(9))

button_plus = Button(w, text="+", fg="black", bg="gray", padx=41, pady=20, command=button_add)
button_minus = Button(w, text="-", fg="black", bg="gray", padx=42, pady=20, command=button_sub)
button_mul = Button(w, text="*", fg="black", bg="gray", padx=42, pady=20, command=button_multiply)
button_div = Button(w, text="/", fg="black", bg="gray", padx=42, pady=20, command=button_divide)

button_clear = Button(w, text="Clear", fg="white", bg="black", padx=78, pady=20, command=button_clr)
button_bkspc = Button(w, text="Backspace", fg="white", bg="black", padx=64, pady=20, command=button_back)
button_mod = Button(w, text="%", fg="black", bg="gray", padx=38, pady=20, command=button_modu)
button_sq = Button(w, text="power", fg="black", bg="gray", padx=27, pady=20, command=button_sqr)
button_rt = Button(w, text="root", fg="black", bg="gray", padx=32, pady=20, command=button_root)
button_dec = Button(w, text=".", fg="black", bg="gray", padx=41, pady=20, command=lambda: button_click("."))
button_eq = Button(w, text="=", padx=89, pady=20, bg="orange", command=button_equal)

# Putting buttons on screen
button0.grid(row=6, column=0)
button1.grid(row=5, column=0)
button2.grid(row=5, column=1)
button3.grid(row=5, column=2)
button4.grid(row=4, column=0)
button5.grid(row=4, column=1)
button6.grid(row=4, column=2)
button7.grid(row=3, column=0)
button8.grid(row=3, column=1)
button9.grid(row=3, column=2)

button_plus.grid(row=5, column=3)
button_minus.grid(row=4, column=3)
button_mul.grid(row=3, column=3)
button_div.grid(row=2, column=3)

button_clear.grid(row=1, column=0, columnspan=2)
button_bkspc.grid(row=1, column=2, columnspan=2)

button_mod.grid(row=2, column=0)
button_sq.grid(row=2, column=1)
button_rt.grid(row=2, column=2)

button_dec.grid(row=6, column=1)
button_eq.grid(row=6, column=2, columnspan=2)

w.mainloop()
