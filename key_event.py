import pgzrun,random
WIDTH=700
HEIGHT=500
TITLE="Catch Maui the demi god"

maui=Actor("maui_resized")
maui.pos=random.randint(0,WIDTH),random.randint(0,HEIGHT)
moana=Actor("moana1")
moana.pos=random.randint(0,WIDTH),random.randint(0,HEIGHT)

def draw():
    screen.blit("b1",(0,0))
    maui.draw()
    moana.draw()

def update():
    if keyboard.left:
        moana.x-=5
    if keyboard.right:
        moana.x=moana.x+5
    if keyboard.up:
        moana.y=moana.y-5
    if keyboard.down:
        moana.y=moana.y+5
    if moana.colliderect(maui):
        maui.pos=random.randint(0,WIDTH),random.randint(0,HEIGHT)












pgzrun.go()