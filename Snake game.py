#! /usr/bin/env python

# Move a worm around the screen. Beware of borders and self!

import pygame
from pygame.locals import *
pygame.init()
import random

class Worm:
    """ A worm. """

    def __init__(self, surface):
        self.surface = surface
        self.x = surface.get_width() / 2
        self.y = surface.get_width() / 2
        self.length = 1
        self.grow_to = 50
        self.vx = 0
        self.vy = -1
        self.body = []
        self.crashed = False
        self.color = 111, 53, 26

    def event(self, event):
        """ Handle keyboard events that affect the worm. """
        if event.key == pygame.K_UP:
            if self.vy == 1: return
            self.vx = 0
            self.vy = -1
        elif event.key == pygame.K_DOWN:
            if self.vy == -1: return
            self.vx = 0
            self.vy = 1
        elif event.key == pygame.K_LEFT:
            if self.vx == 1: return
            self.vx = -1
            self.vy = 0
        elif event.key == pygame.K_RIGHT:
            if self.vx == -1: return
            self.vx = 1
            self.vy = 0

    def move(self):
        """ Move the worm. """
        self.x += self.vx
        self.y += self.vy

        if (self.x, self.y) in self.body:
            self.crashed = True

        self.body.insert(0, (self.x, self.y))

        if (self.grow_to > self.length):
            self.length += 1

        if (len(self.body) > self.grow_to):
            pop = self.body.pop(-1)
            pygame.draw.rect(self.surface, (0, 0, 0), (pop[0], pop[1], 3, 3), 0)

        if (len(self.body) > self.length):
            pop = self.body.pop(-1)
            pygame.draw.rect(self.surface, (0, 0, 0), (pop[0], pop[1], 3, 3), 0)

    def draw(self):
        """ Draw the worm """
        x, y = self.body[0]
        pygame.draw.rect(self.surface, self.color, (x, y, 3, 3), 0)
        x, y = self.body[-1]
        pygame.draw.rect(self.surface, (0, 0, 0), (x, y, 3, 3), 0)

    def position(self):
        return self.x, self.y

    def eat(self):
        self.grow_to += 25

    def hurt(self):
#        self.grow_to -= 25
        self.grow_to = self.grow_to - 25
        self.length = self.length - 25

class Food:
    def __init__(self, surface):
        self.surface = surface
        self.x = random.randint(5, surface.get_width()-5)
        self.y = random.randint(5, surface.get_height()-5)
        self.color = 255, 255, 255

    def draw(self):
        pygame.draw.rect(self.surface, self.color, (self.x, self.y, 3, 3), 0)

    def position(self):
        return self.x, self.y

    def check(self, x, y):
        if x < self.x or x > self.x + 3:
            return False
        elif y < self.y or y > self.y + 3:
            return False
        else:
            return True

    def erase(self):
        pygame.draw.rect(self.surface, (0, 0, 0), (self.x, self.y, 3, 3), 0)

class Fire:
    def __init__(self, surface):
        self.surface = surface
        self.x = random.randint(5, surface.get_width()-5)
        self.y = random.randint(5, surface.get_height()-5)
        self.color = 255, 0, 0

    def draw(self):
        pygame.draw.rect(self.surface, self.color, (self.x, self.y, 4, 4), 0)

    def position(self):
        return self.x, self.y

    def check(self, x, y):
        if x < self.x or x > self.x + 4:
            return False
        elif y < self.y or y > self.y + 4:
            return False
        else:
            return True

    def erase(self):
        pygame.draw.rect(self.surface, (0, 0, 0), (self.x, self.y, 4, 4), 0)

# Window dimensions
w = 500
h = 500

screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()

score = 0
worm = Worm(screen)
food1 = Food(screen)
fire1 = Fire(screen)
running = True

while running:
    worm.move()
    worm.draw()
    food1.draw()
    fire1.draw()

    if worm.crashed:
        running = False
    elif worm.x <= 0 or worm.x >= w - 1:
        running = False
    elif worm.y <= 0 or worm.y >= h - 1:
        running = False
    elif food1.check(worm.x, worm.y):
        score += 1
        worm.eat()
        print ("Score: %d") % score
        food1.erase()
        food1 = Food(screen)
    elif fire1.check(worm.x, worm.y):
        score -= 1
        worm.hurt()
        print ("Score: %d") % score
        fire1.erase()
        fire1 = Fire(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            worm.event(event)

    pygame.display.flip()
    clock.tick(100)
