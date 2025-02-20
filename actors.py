import pgzrun  
from random import randint
WIDTH=800
HEIGHT=800
TITLE="Catch Rapaunzel"
msg=""
rapaunzel=Actor("rapaunzel_resized.png")
rapaunzel.pos=150,200

def draw():
    screen.fill("light blue")
    rapaunzel.draw()
    screen.draw.text(msg,center=(400,200),fontsize=30,color="purple")

def on_mouse_down(pos):
    global msg
    if rapaunzel.collidepoint(pos):
        rapaunzel.x=randint(50, WIDTH-50)
        rapaunzel.y=randint(50,HEIGHT-50)
        msg="yay you caught rapaunzel"
    else:
        msg="oops you missed it, try again"
    

pgzrun.go()
