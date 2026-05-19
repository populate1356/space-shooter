import pygame
from settings import (
    display_surface,
    all_sprite_group,
    meteor_sprite_group,
    missile_sprite_group,
)
from entity.bg import Background
from entity.meteor import Meteor
from entity.player import Player

clock = pygame.time.Clock()


def main():
    running = True
    direction = pygame.Vector2(0, 0)

    Background()
    player = Player()
    meteor_event = pygame.event.custom_type()
    pygame.time.set_timer(meteor_event, 400)

    while running:
        dt = clock.tick(30) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == meteor_event:
                Meteor.spawn(3)

        if direction.length() > 0:
            direction.normalize_ip()
        pygame.sprite.groupcollide(
            meteor_sprite_group, missile_sprite_group, True, True
        )

        if pygame.sprite.spritecollide(player, meteor_sprite_group, False):
            running = False

        display_surface.fill("gray")

        all_sprite_group.update(dt)
        all_sprite_group.draw(display_surface)

        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
