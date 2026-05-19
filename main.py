import pygame
from settings import WINDOW_WIDTH, WINDOW_HEIGHT  # <-- 추가하기
from entity.player import Player
from entity.bg import Background
from entity.meteor import Meteor

pygame.init()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("space shooter")


clock = pygame.time.Clock()


def main():
    running = True
    direction = pygame.Vector2(0, 0)
    all_sprite_group = pygame.sprite.Group()

    Background(all_sprite_group)
    Player(all_sprite_group)
    Meteor.spawn(all_sprite_group, 10)
    meteor_event = pygame.event.custom_type()
    pygame.time.set_timer(meteor_event, 400)

    while running:
        dt = clock.tick(30) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == meteor_event:
                Meteor.spawn(all_sprite_group, 3)

        if direction.length() > 0:
            direction.normalize_ip()

        display_surface.fill("gray")

        all_sprite_group.update(dt)
        all_sprite_group.draw(display_surface)

        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
