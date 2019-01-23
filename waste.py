from turtle import *
from tkinter import messagebox
messagebox.showinfo("RULES TO BE FOLLOWED","F10 - start/stop , spacebar - speed controller")
state = {'turn': 0}

def spinner():
    "draw fidget spinner."
    clear()
    angle = state['turn'] / 10
    right(angle)
    forward(100)
    dot(120, 'RED')
    back(100)
    right(120)
    forward(100)
    dot(120, 'GREEN')
    back(100)
    right(120)
    forward(100)
    dot(120, 'YELLOW')
    back(100)
    right(120)
   
    update()

def animate():
    if state['turn'] == 0:
        state['turn'] +=50

    spinner()
    ontimer(animate, 10)

def flick():
    state['turn'] -= 10

setup(500, 500, 370,0)
hideturtle()
tracer(False)
width(100)
onkey(flick,'space')
listen()
animate()
done()