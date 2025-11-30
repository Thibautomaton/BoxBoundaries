import math

import pygame
from Box2D.b2 import polygonShape
from settings import *
import Box2D


class Boundary():
    def __init__(self, x_, y_, w_, h_, world):

        self.x = x_
        self.y = y_
        self.w = w_
        self.h = h_

        self.display_surface = pygame.display.get_surface()

        self.body= world.CreateStaticBody(
            position=(coordPixelsToWorld((self.x, self.y)))
        )

        box2dW = scalarPixelToWorld(self.w/2)
        box2dH = scalarPixelToWorld(self.h/2)

        ps = polygonShape(
            box=(box2dW, box2dH)
        )

        self.body.CreateFixture(
            shape = ps,
            restitution=0.2
        )

    def display(self):
        color = (0, 0, 255)

        rect_surface = pygame.Surface((self.w, self.h), pygame.SRCALPHA)
        pygame.draw.rect(rect_surface, color, (0, 0, self.w, self.h))

        angle_degree = -math.degrees(self.body.transform.angle)

        rotated_surface = pygame.transform.rotate(rect_surface, angle_degree)
        rotated_rect = rotated_surface.get_rect(center= coordWorldToPixel(self.body.transform.position))


        self.display_surface.blit(rotated_surface, rotated_rect)

