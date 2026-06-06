from pygame import *

window = display.set_mode((700, 500))
window.fill((50, 240, 240))


game = True
FPS = 60
clock = time.Clock()


while game == True:
    for e in event.get():
        if e.type == QUIT:
            game = False



    display.update()
    clock.tick(FPS)