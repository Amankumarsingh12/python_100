import tkinter

#oops
window = tkinter.Tk()
#title
window.title("my first")
#size
window.minsize(width=500, height=300)

#lable
my_lable = tkinter.Label(text="i am label", font=("Arial", 24, "bold"))
my_lable.pack()

#button
def button_click():
    print("i got click")
    my_lable["text"] = inp.get()

button = tkinter.Button(text="click", command=button_click)
button.pack()

#entry
inp = tkinter.Entry(width=10)
inp.pack()

window.mainloop()