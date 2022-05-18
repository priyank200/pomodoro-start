from tkinter import *
import math

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
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global timer
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer", font=(FONT_NAME, 30, "bold"), bg=YELLOW, fg=GREEN)
    check.config(text=" ")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps == 8:
        countdown(long_break)
        label.config(text="Long Break", font=(FONT_NAME, 30, "bold"), bg=YELLOW, fg=RED)
    elif reps % 2 == 1:
        countdown(work_sec)
        label.config(text="Working Time", font=(FONT_NAME, 30, "bold"), bg=YELLOW, fg=GREEN)
    elif reps % 2 == 0 and reps != 8:
        countdown(short_break)
        label.config(text="Short Break", font=(FONT_NAME, 30, "bold"), bg=YELLOW, fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global reps
    global timer
    minute = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = "0" + str(seconds)
    if minute < 10:
        minute = "0" + str(minute)
    canvas.itemconfig(timer_text, text=f"{minute}:{seconds}")
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        work_session = math.floor(reps / 2)
        check.config(text=f"{checkmark * work_session}", font=(FONT_NAME, 20, "bold"))


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()

window.title("pomodore timer")
window.minsize(width=300, height=350)
window.config(padx=100, pady=50, bg=YELLOW)
checkmark = "✔"

# title
label = Label(text="Timer", font=(FONT_NAME, 30, "bold"), bg=YELLOW, fg=GREEN)
label.grid(row=0, column=1)

# image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(row=1, column=1)

# button
start_button = Button(text="Start", fg="red", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)
reset_button = Button(text="Reset", fg="red", highlightthickness=0, command=reset)
reset_button.grid(row=2, column=2)
check = Label(bg=YELLOW, fg=GREEN)
check.grid(row=3, column=1)

window.mainloop()
