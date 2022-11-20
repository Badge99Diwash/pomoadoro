import math
from tkinter import *

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
def click_reset():
    global reps
    windows.after_cancel(timer)
    canvas.itemconfig(Timer, text="00:00")
    label.config(text="TIMER")
    reps=0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def click_start():
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        label.config(text='Long-Beak')
    if reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        label.config(text='Break', fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        label.config(text='Work', fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    min = math.floor(count / 60)
    sec = count % 60
    if sec < 10:
        sec = f'0{sec}'
    canvas.itemconfig(Timer, text=f'{min}:{sec}')
    if count > 0:
        global timer

        timer = windows.after(1000, count_down, count - 1)
    else:
        click_start()
        mark = ''
        for i in range(math.floor(reps / 2)):
            mark += ' ✔'
            check.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
windows = Tk()
windows.title("pomodoro")
windows.config(padx=100, pady=50, bg=YELLOW)
label = Label(text='TIMER', font=(FONT_NAME, 20, 'bold'), fg=GREEN, bg=YELLOW, highlightthickness=0)
label.grid(column=1, row=0)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_image)
Timer = canvas.create_text(100, 120, text='00:00', font=(FONT_NAME, 20, 'bold'))
canvas.grid(column=1, row=1)
start = Button(text="START", font=(FONT_NAME, 10, 'normal'), command=click_start)
start.grid(column=0, row=3)
reset = Button(text='RESET', font=(FONT_NAME, 10, 'normal'), command=click_reset)
reset.grid(column=2, row=3)
check = Label(text=' ', font=(FONT_NAME, 20, 'normal'), fg=GREEN, bg=YELLOW, highlightthickness=0)
check.grid(column=1, row=3)
windows.mainloop()
