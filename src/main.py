from display import getDisplayText as display
from time import sleep
from getTime import getTime
import tkinter as tk
import atexit as atExit

app = tk.Tk()
app.title("Binary Timer")

x = tk.StringVar()

label = tk.Label(app, textvariable=x, font=('Helvetica', 90))
label.pack(side = tk.BOTTOM)

while True:
    x.set(display(getTime()))
    try:
        app.update_idletasks()
        app.update()
    except Exception as error:
        if app:
            exit()
    sleep(.005)