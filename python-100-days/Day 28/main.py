from tkinter import *
from datetime import timedelta
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

def set_timer_label(count):
    hh, mm, ss = str(timedelta(seconds=count)).split(":")
    canvas.itemconfig(timer_text, text=f"{mm}:{ss}")

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    reps = 0
    set_timer_label(WORK_MIN * 60)
    remove_threads()
    title_label.config(text="Timer", fg=GREEN)


def remove_threads():
    for th in threads:
        window.after_cancel(th)

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    remove_threads()
    reps += 1

    if reps % 8 == 0:
        minutes = 5
        title_label.config(text="Beak", fg=RED)
        update_timer(minutes)
    elif reps % 2 == 0:
        minutes = 2
        title_label.config(text="Beak", fg=PINK)
        update_timer(minutes)
    else:
        minutes = 3
        title_label.config(text="Work", fg=GREEN)
        update_timer(minutes)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def update_timer(count):
    if count >= 0:
        set_timer_label(count)
        thread_id = window.after(1000, update_timer, count - 1)
        threads.append(thread_id)
    else:
        if reps % 2 == 0:
            check_marks.config(text=f"{check_marks.cget("text")}✔")

        start_timer()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
threads = []

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(text="", fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()