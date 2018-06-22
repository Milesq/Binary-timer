from display import getDisplayText as display
from time import sleep
from getTime import getTime
import tkinter as tk
import atexit

app = tk.Tk()
app.title("Binary Timer")

x = tk.StringVar()

label = tk.Label(app, textvariable=x)
label.pack( side = tk.BOTTOM )

atexit.register(lambda: label.destroy())

while True:
    x.set(display(getTime()))

    app.update_idletasks()
    app.update()
    sleep(.005)