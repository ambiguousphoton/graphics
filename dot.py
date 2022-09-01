from turtle import color
from PIL import *
from tkinter import ttk
from tkinter import *

root = Tk()
root.title("line")
# import turtle
# board = turtle.Turtle()
# board.left(360)

# board.forward(100)
# # board.left(90)
# board.forward(100)
# # board.left(360)
# board.forward(100)
# # board.left(369)
# board.forward()

canvas = Canvas(root)
canvas.pack()
canvas.config(width=450,height=450)

line  = canvas.create_line(225,225,300,330,fill='blue',width=1)

root.mainloop()