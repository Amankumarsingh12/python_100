import requests
from tkinter import *


def get_quote():
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(quote_text, text = quote)




########## this will create a screen #########

window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

#################################################



############ this will create a img on windows ###############

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
## this create txt in that picture ###########
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 15, "bold"), fill="white")
#######################################
canvas.grid(row=0, column=0)

##########################################################################################


#####  this will add button #############

kenya_img = PhotoImage(file="kanye.png")
kenya_button = Button(image=kenya_img, highlightthickness=0, command=get_quote)
kenya_button.grid(row=1, column=0)

#####   #############

window.mainloop()
