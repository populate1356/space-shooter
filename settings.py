import pygame

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
all_sprite_group = pygame.sprite.Group()  # <-- 추가
meteor_sprite_group = pygame.sprite.Group()  # <-- 추가
missile_sprite_group = pygame.sprite.Group()
pygame.init()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("space shooter")
