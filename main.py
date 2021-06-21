from tkinter import *
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
check_mark = "✔"
rep = 0
timer_continue = None


# minute=StringVar()
# second=StringVar()
# minute.set("00")
# second.set("00")
# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    global rep
    countdown(-1)
    rep = 0
    timer_label.config(text="Timer", fg="blue", font=(FONT_NAME, 40, "bold"))
    check_marks.config(text='', fg="green", font=(FONT_NAME, 15, "bold"))


# ---------------------------- TIMER MECHANISM ------------------------------- #
def timer_start():
    global check_mark
    global rep
    rep += 1
    if rep in range(1, 6, 2):
        countdown(WORK_MIN*60)
        timer_label.config(text='WORK', fg = GREEN)

    elif rep in range(2, 7, 2):
        countdown( SHORT_BREAK_MIN*60)
        timer_label.config(text='SHORT BREAK', fg=PINK)
        check_marks.configure(text=check_mark)
        check_mark += check_mark

    elif rep == 7:
        countdown( LONG_BREAK_MIN*60)
        timer_label.config(text='LONG BREAK', fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(t):
    global timer_continue
    mins, secs = divmod(t, 60)
    canvas.itemconfigure(timer_text, text=f'{mins:2}:{secs:02}')
    if t > 0:
        timer_continue = window.after(1000, countdown, t - 1)
    elif t ==-1:
        window.after_cancel(timer_continue)
        mins,secs = 0,0
        canvas.itemconfigure(timer_text, text=f'{mins:2}:{secs:02}')
    else:
        timer_start()


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)
window.after(1000, )
canvas = Canvas(width=200, height=230, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 115, image=tomato_img)
timer_text = canvas.create_text(100, 120, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(row=2, column=1)

timer_label = Label(text="Timer", fg="blue", font=(FONT_NAME, 40, "bold"))
timer_label.grid(row=0, column=1)

start_button = Button(text='Start', font=(FONT_NAME, 15, "bold"), command=timer_start)
start_button.grid(row=3, column=0)

reset_button = Button(text='Reset', font=(FONT_NAME, 15, "bold"), command=timer_reset)
reset_button.grid(row=3, column=3)

check_marks = Label(text='', fg="green", font=(FONT_NAME, 15, "bold"))
check_marks.grid(row=3, column=1)
pomodoro = True

window.mainloop()
