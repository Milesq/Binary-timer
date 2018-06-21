# from getTime import getTime

# init window
import tkinter as tk
def _create_circle(self, x, y, r, **args):
    return self.create_oval(x-r, y-r, x+r, y+r, **args)
tk.Canvas.create_circle = _create_circle

root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=500,bg="white")
canvas.grid()

canvas.create_circle(100,200,300, bgcolor="black")

root.mainloop()