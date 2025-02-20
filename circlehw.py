import random, pgzrun
WIDTH=500
HEIGHT=500
TITLE="Wonderful circles"

def draw():
    screen.fill((173,216,230))
    radius =WIDTH/2
    r=random.randint(0,255)
    g=0
    b=random.randint(0,255)

    for i in range(15):
        screen.draw.filled_circle((WIDTH / 2, HEIGHT / 2), radius, (r, g, b))
        radius-= 10  
        g+=10
        

pgzrun.go()