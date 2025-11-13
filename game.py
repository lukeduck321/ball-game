from tkinter import *
from random import randint
from animation import *

def game_start(window):
    mousex = 1
    mousey = 1
    x = 1
    y = 1

    ca = Canvas(window, width = 400, height = 600, background = "white")
    ca.pack()

    def spawn():
        npcball = randint(0, 400)
        ca.create_oval(npcball-5,npcball-5,npcball+5,npcball+5)

    def click(e):

        nonlocal x, y
        
        ballx = e.x
        bally = e.y
    
        print(ballx,bally)

        shoot_anim(canvas = ca ,window = window, ball_start = str(200)+","+str(600), ball_end = str(x)+","+str(y))  

    def callback(e):
        global x, y
        nonlocal mousex, mousey
    
        ca.create_line(mousex,mousey,200,600, fill ="white")

        x = e.x
        y = e.y

        mousex = x
        mousey = y

        if mousey < 500:
            mousey = 500
        
        ca.create_line(mousex,mousey,200,600)
        print(x,y)

    spawn()

    ca.bind('<Motion>', callback)
    ca.bind('<Button-1>', click)
