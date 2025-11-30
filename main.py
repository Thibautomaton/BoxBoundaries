# This is a sample Python script.
import sys

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pygame
import Box2D
from Box2D.b2 import world
from settings import *
from box import Box
from boundary import Boundary

pygame.init()

display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Box Boundary")


world = world(GRAVITY=(0, -10),  doSleep=True)



clock = pygame.time.Clock()



boundaries = []
bo1 = Boundary(0, HEIGHT-15, WIDTH/2, 15, world)
bo2 = Boundary(WIDTH/2, HEIGHT-100, WIDTH/2, 15, world)
boundaries.append(bo1)
boundaries.append(bo2)

boxes = []



boxesToDestroy = []
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

    display_surface.fill((0, 0, 0))

    if pygame.mouse.get_pressed()[0]:
        x, y = pygame.mouse.get_pos()
        b = Box(x, y, world)

        boxes.append(b)

    nbActivBoxes = 0

    for p in boxes:
        nbActivBoxes+=1
        p.display()
        if not 0<p.body.transform.position[0]<WIDTH or not 0<p.body.transform.position[1]<HEIGHT:
            boxesToDestroy.append(p)
            boxes.remove(p)

    print(nbActivBoxes)

    for b in boundaries:
        b.display()

    world.Step(STEP, 6, 2)

    for p in boxesToDestroy:
        p.killBody(world)

        boxesToDestroy.remove(p)

    clock.tick(TARGET_FPS)
    pygame.display.update()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
