# seddik7591@gmail.com
from tkinter import *

app = Tk()
app.title("Calculator")
app.iconbitmap('calc.ico')


e = Entry(app, width=34, font = "Helvetica 14 bold", fg="#555", bg="#ccc", borderwidth=5)

e.grid(row=0, column=0, columnspan=4, pady=5, ipady=5)

def button_click(number):
	current = e.get()
	e.delete(0, END)
	e.insert(0, str(current) + str(number))

def button_clear():
	e.delete(0, END)

def button_add():
	global firstNumber
	firstNumber = float(e.get())
	global math
	math = "add"
	e.delete(0, END)

def button_subtract():
	global firstNumber
	firstNumber = float(e.get())
	global math
	math = "subtract"
	e.delete(0, END)

def button_multiply():
	global firstNumber
	firstNumber = float(e.get())
	global math
	math = "multiply"
	e.delete(0, END)

def button_divide():
	global firstNumber
	firstNumber = float(e.get())
	global math
	math = "divide"
	e.delete(0, END)

def button_equal():
	secondNumber = float(e.get())
	e.delete(0, END)
	if math == "add":
		e.insert(0, firstNumber+secondNumber)
	if math == "subtract":
		e.insert(0, firstNumber-secondNumber)
	if math == "multiply":
		e.insert(0, firstNumber*secondNumber)
	if math == "divide":
		e.insert(0, firstNumber/secondNumber)

button_0 = Button(app, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_1 = Button(app, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(app, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(app, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(app, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(app, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(app, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(app, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(app, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(app, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_add = Button(app, text="+", padx=38, pady=20, command=button_add)
button_equal = Button(app, text="=", padx=39, pady=20, command=button_equal)
button_clear = Button(app, text="C", padx=39, pady=20, command=button_clear)
button_subtract = Button(app, text="-", padx=40, pady=20, command=button_subtract)
button_multiply = Button(app, text="*", padx=40, pady=20, command=button_multiply)
button_divide = Button(app, text="/", padx=40, pady=20, command=button_divide)

button_clear.grid(row=4 ,column=0)
button_0.grid(row=4 ,column=1)
button_equal.grid(row=4 ,column=2)
button_divide.grid(row=4 ,column=3)

button_1.grid(row=3 ,column=0)
button_2.grid(row=3 ,column=1)
button_3.grid(row=3 ,column=2)
button_multiply.grid(row=3 ,column=3)

button_4.grid(row=2 ,column=0)
button_5.grid(row=2 ,column=1)
button_6.grid(row=2 ,column=2)
button_subtract.grid(row=2 ,column=3)

button_7.grid(row=1 ,column=0)
button_8.grid(row=1 ,column=1)
button_9.grid(row=1 ,column=2)
button_add.grid(row=1 ,column=3)

app.mainloop()
