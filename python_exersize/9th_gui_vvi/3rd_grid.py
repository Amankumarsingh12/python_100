import tkinter

###     setup    ####
window = tkinter.Tk()
window.title("FIRST")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

###     lable   ###
my_lable = tkinter.Label(text="i am label", font=("Arial", 24, "bold"))
my_lable.pack()
my_lable.grid(column=0, row=0)


## button ##
def button_click():
    print("clicked")
    print(inp.get()) #from entry

button = tkinter.Button(text="click", command=button_click)
button.grid(column=1, row=1)

###challenfe###

def button_click_1():
    print("2")

button_2 = tkinter.Button(text="click", command=button_click_1)
button_2.grid(column=2, row=0)


#entry
inp = tkinter.Entry(width=10)
inp.grid(column=3, row=3)

window.mainloop()