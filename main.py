import pygame
import random

pygame.init()

WHITE = (225, 225, 225)
BLACK = (0, 0, 0)
RED = (225, 0, 0)
GREEN = (0, 225, 0)
BLUE = (0, 0, 225)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./images/wukong.jpg")
        self.image = pygame.transform.scale(self.image, (50, 44))
        self.rect = self.image.get_rect()

class Block(pygame.sprite.Sprite):
    def __init__(self):
        super().__int__()
