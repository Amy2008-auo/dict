import pgzrun
from random import randint
WIDTH=800
HEIGHT=800
TITLE="Catch Maui and Moana"
msg=""

Moana= Actor("moana1.png")
Moana.pos=150,200

Maui= Actor("maui_resized.png")
Maui.pos=100,100

def draw():
    screen.fill("light blue")
    Moana.draw()
    Maui.draw()
    screen.draw.text(msg,center=(400,200),fontsize=30,color="orange")

def on_mouse_down(pos):
    global msg 
    Moana.pos=pos
    if Moana.collidepoint(pos):
        print
        Moana.x = randint(50, WIDTH - 50)
        Moana.y = randint(50, HEIGHT - 50)
        msg = "Yay! You caught Moana!"
    elif Maui.collidepoint(pos):
        Maui.x = randint(50, WIDTH - 50)
        Maui.y = randint(50, HEIGHT - 50)
        msg = "Yay! You caught Maui!"
    else:
        msg = "Oops, you missed it! Try again."

pgzrun.go()
