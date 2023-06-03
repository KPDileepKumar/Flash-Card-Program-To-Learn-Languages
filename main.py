from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
try:
    data_file = pd.read_csv("data/to_learn.csv")
except FileNotFoundError:
    data_file = pd.read_csv("data/french_words.csv")
to_learn = data_file.to_dict(orient="records")
print(to_learn)
current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(canvas_image, image=image_front)
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(language_text, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, flip_card)


def is_known():
    to_learn.remove(current_card)
    data_frame = pd.DataFrame(to_learn)
    data_frame.to_csv("data/words_to_learn.csv", index=False)
    next_card()


def flip_card():
    canvas.itemconfig(canvas_image, image=image_back)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(language_text, text=current_card["English"], fill="black")


window = Tk()
window.title("Flashy")
window.configure(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
image_front = PhotoImage(file="./images/card_front.png")
image_back = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=image_front)
language = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
language_text = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()
