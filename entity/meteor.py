import pygame
from os.path import join
import random

from settings import WINDOW_HEIGHT, WINDOW_WIDTH


class Meteor(pygame.sprite.Sprite):
    path = join("images", "meteor.png")

    def __init__(self, group: pygame.sprite.Group):  # <-- 수정하기
        super().__init__(group)
        self.image = pygame.image.load(Meteor.path).convert_alpha()
        self.rect: pygame.FRect = self.image.get_frect(
            center=(
                random.randint(0, WINDOW_WIDTH),
                random.randint(-100, 0),
            )  # <-- 위치 설정
        )
        self.speed: float = random.randint(300, 500)  # <-- 비행속도
        self.direction: pygame.Vector2 = pygame.Vector2(random.randint(-1, 1), 1)

    def update(self, dt: float):
        self.rect.center += self.direction * dt * self.speed
        if self.rect.top > WINDOW_HEIGHT:
            self.kill()

    @classmethod
    def spawn(cls, group: pygame.sprite.Group, n: int):
        if n <= 0:
            raise ValueError("n must be greater than 0")
        for _ in range(n):
            Meteor(group)
