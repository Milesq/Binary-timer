import tkinter as tk
from time import sleep

from gettime import gettime
from display import getdisplaytext as display

app = tk.Tk()
app.title("Binary Timer")

x = tk.StringVar()

label = tk.Label(app, textvariable=x, font=('Helvetica', 90))
label.pack(side=tk.BOTTOM)

while True:
    x.set(display(gettime()))
    try:
        app.update_idletasks()
        app.update()
    except Exception as error:
        if app:
            exit()
    sleep(.005)
