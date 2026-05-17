import pygame
from os.path import join


class Missile(pygame.sprite.Sprite):
    path: str = join("images", "missile.png")

    def __init__(self, group: pygame.sprite.Group):
        super().__init__(group)
        self.image = pygame.image.load(Missile.path).convert_alpha()
        self.rect = self.image.get_frect(center=(100, 100))

    def update(self, dt: float):
        pass
