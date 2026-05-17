import pygame
from os.path import join
from settings import WINDOW_WIDTH, WINDOW_HEIGHT


class Background(pygame.sprite.Sprite):
    path: str = join("images", "background.png")
    speed: float = 100
    velocity: pygame.Vector2 = pygame.Vector2(0, 0)

    def __init__(self, group: pygame.sprite.Group):
        super().__init__(group)
        self.image = pygame.transform.scale(
            pygame.image.load(Background.path).convert_alpha(),
            (WINDOW_WIDTH, WINDOW_HEIGHT),
        )
        self.rect = self.image.get_frect()

    def update(self, dt: float):
        pass
