import math
from tkinter import *
import random

TIME = 60
with open("words") as f:
    wordlist = []
    for line in f:
        wordlist.append(line.strip())


def start():
    global score
    score = 0
    canvas.itemconfig(label, text=f"")
    canvas.delete(logo_image)
    generate_text()
    count_down(TIME)


def generate_text():
    global input_text, random_text
    random_text = ''
    for i in range(3):
        random_text += f" {random.choice(wordlist)}"

    random_text = random_text[1:]
    canvas.itemconfig(test_text, text=random_text, fill="#3A3845")
    print(random_text)
    input_text = Entry(window, width=30, font='Arial 20')
    input_text.bind('<Return>', get_answer)
    input_text.grid(column=0, row=0, columnspan=2)


def get_answer(event=None):
    global score
    answer = input_text.get()
    if answer == random_text:
        score += 1
        canvas.itemconfig(label, text="Correct", fill="green")
    else:
        canvas.itemconfig(label, text="Wrong", fill="red")
    generate_text()


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    elif count == 0:
        end()


def end():
    canvas.itemconfig(label, text=f"Score: {score*3} Words per minute!", fill="#525E75")
    input_text.delete(0, END)
    input_text.insert(0, "Press Start to start again.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Speed-Test APP")
window.config(padx=20, pady=20, bg="#C5D8A4", width=500, height=300)
window.resizable(False, False)

canvas = Canvas(window, width=500, height=300, bg="#C5D8A4", highlightbackground='#FDFFA9', bd=10)
canvas.grid(column=0, row=0, columnspan=2)

canvas.create_text(250, 50, text="Typing Speed Test", font='Helvetica 20 bold', fill="#3A3845")

logo = PhotoImage(file="logo-removebg-preview.png")
logo_image = canvas.create_image(250, 150, image=logo)

start_button = Button(text="Start", width=10, height=2, bg='#F4FCD9', command=start, highlightthickness=0)
start_button.grid(column=0, row=1)

exit_button = Button(text="Exit", width=10, height=2, bg='#F4FCD9', command=window.destroy, highlightthickness=0)
exit_button.grid(column=1, row=1)

label = canvas.create_text(250, 270, text="", fill="white", font=("Helvetica", 25, "bold"))
test_text = canvas.create_text(250, 200, text='', font=("Helvetica", 25, "bold"))
timer_text = canvas.create_text(250, 110, text="", fill="white", font=("Helvetica", 25, "bold"))

window.mainloop()
