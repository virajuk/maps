import random

from glob import glob
import pygame


class GreenGrass(pygame.sprite.Sprite):

    def __init__(self, pos, groups, id):

        super().__init__(groups)
        self.images = glob('graphics/grass/*.png')
        self.image = pygame.image.load(random.choice(self.images)).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.id = id


class Sand(pygame.sprite.Sprite):

    def __init__(self, pos, groups, id):

        super().__init__(groups)
        self.images = glob('graphics/sand/*.png')
        self.image = pygame.image.load(random.choice(self.images)).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.id = id


class Water(pygame.sprite.Sprite):

    def __init__(self, pos, groups, id):

        super().__init__(groups)
        self.images = glob('graphics/water/*.png')
        self.image = pygame.image.load(random.choice(self.images)).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.id = id


class Grid(pygame.sprite.Sprite):

    def __init__(self, pos, groups):

        super().__init__(groups)
        self.images = glob('graphics/grid/*.png')
        self.image = pygame.image.load('graphics/grid/grid.png').convert_alpha()
        self.image.set_alpha(40)
        self.rect = self.image.get_rect(topleft=pos)