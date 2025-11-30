import math

import pygame
from Box2D.b2 import polygonShape
from settings import *
import Box2D

class Box():
    def __init__(self, x_, y_, world):

        self.x = x_
        self.y = y_
        self.w = 16
        self.h = 16

        self.display_surface = pygame.display.get_surface()
        self.body = world.CreateDynamicBody(
            position=(coordPixelsToWorld((self.x, self.y)))
        )

        bodyW = scalarPixelToWorld(self.w / 2)
        bodyH = scalarPixelToWorld(self.h / 2)
        ps = polygonShape(
            box = (bodyW, bodyH)
        )

        self.body.CreateFixture(
            shape=ps,
            friction = 0.3,
            density = 0.1,
            restitution = 0.8
        )

    def display(self):
        color = (0, 255, 0)
        border = (255, 255, 255)
        rect_surface = pygame.Surface((self.w, self.h), pygame.SRCALPHA)
        pygame.draw.rect(rect_surface, color, (0, 0, self.w, self.h))
        pygame.draw.rect(rect_surface, border, (0, 0, self.w, self.h), 2)
        angle_degree = -math.degrees(self.body.transform.angle)

        rotated_surface = pygame.transform.rotate(rect_surface, angle_degree)
        rotated_rect = rotated_surface.get_rect(center= coordWorldToPixel(self.body.transform.position))


        self.display_surface.blit(rotated_surface, rotated_rect)


    def killBody(self, world):
        world.DestroyBody(self.body)
