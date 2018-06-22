from display import getDisplayText as display
from time import sleep
from getTime import getTime
import tkinter as tk

app = tk.Tk()
app.title("Binary Timer")

while True:
    # app.sele
    label = tk.Label(app, text = '')
    label.pack( side = tk.BOTTOM )

    app.update_idletasks()
    app.update()
    sleep(1)