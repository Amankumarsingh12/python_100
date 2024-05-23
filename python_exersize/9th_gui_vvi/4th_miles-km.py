import tkinter

window = tkinter.Tk()
window.title("Miles to Km convert")
window.minsize(width=400, height=100)
window.config(padx=10, pady=10)


#entry
inp = tkinter.Entry(width=20)
inp.grid(column=2, row=0, padx=10, pady=10)


#lable_1 Miles
lable_miles = tkinter.Label(text="Miles", font=("Arial", 14, "bold"))
lable_miles.grid(column=3, row=0, padx=10, pady=10)

#lable is equal to
lable_equal = tkinter.Label(text="is equal to", font=("Arial", 14, "bold"))
lable_equal.grid(column=0, row=2, padx=10, pady=10)

#change Km final#
lable_final = tkinter.Label(text="0", font=("Arial", 24, "bold"))
lable_final.grid(column=2, row=2, padx=10, pady=10)

#lable km#
lable_km = tkinter.Label(text="KM", font=("Arial", 14, "bold"))
lable_km.grid(column=3, row=2, padx=10, pady=10)

#button

def button_1():
    km = float(inp.get()) * 1.6
    km = str(round(km))
    lable_final.config(text=km)
    print("click")

button = tkinter.Button(text="Calculatate", command=button_1)
button.grid(column=2, row=3, padx=10, pady=10)

window.mainloop()