import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk

BACKGROUND_COLOR = "#B1DDC6"

root = ThemedTk(theme="breeze")
root.title("Flashy")
root.geometry("800x600")
root.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

frame = ttk.Frame(root)
frame.grid(row=0, column=0, sticky="nsew")

card_front_img = ttk.PhotoImage(file="images/card_front.png")
ttk.Label(frame, image=card_front_img).grid(row=0, column=0, columnspan=2, padx=10, pady=10)
ttk.Label(frame, text="Title", font=("Arial", 40, "italic")).grid(row=1, column=0, padx=10, pady=10)
ttk.Label(frame, text="Word", font=("Arial", 60, "italic")).grid(row=2, column=0, padx=10, pady=10)

cross_image = ttk.PhotoImage(file="images/wrong.png")
unknown_button = ttk.Button(frame, image=cross_image)
unknown_button.grid(row=3, column=0, padx=10, pady=10)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop()
