from tkinter import *

def shoot_anim(canvas, window, ball_start, ball_end):
    loop = 1
    ballx = str()
    bally = str()
    print(ball_start, ball_end)

    for i in ball_start:
        if loop == 2:
            bally += i
        if i == ",":
            loop = 2
        if loop == 1:
            ballx += i
    loop = 1

    for i in ball_end:
        if loop == 2:
            bally_end += i
        if i == ",":
            loop = 2
        if loop == 1:
            ballx_end += i
    loop = 1
    
    ballx = int(ballx)
    bally = int(bally)
    
    canvas.create_oval(ballx-5,bally-5,ballx+5,bally+5)
    
