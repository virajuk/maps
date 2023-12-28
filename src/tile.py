import random

from glob import glob
import pygame


class GreenGrass(pygame.sprite.Sprite):

    def __init__(self, pos, groups):

        super().__init__(groups)
        self.images = glob('graphics/grass/*.png')
        self.image = pygame.image.load(random.choice(self.images)).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        # print(self.rect.center)


class Sand(pygame.sprite.Sprite):

    def __init__(self, pos, groups):

        super().__init__(groups)
        self.images = glob('graphics/sand/*.png')
        self.image = pygame.image.load(random.choice(self.images)).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)


class Water(pygame.sprite.Sprite):

    def __init__(self, pos, groups):

        super().__init__(groups)
        self.images = glob('graphics/water/*.png')
        self.image = pygame.image.load(random.choice(self.images)).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)