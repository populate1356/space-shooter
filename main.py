import pygame
from settings import WINDOW_WIDTH, WINDOW_HEIGHT  # <-- 추가하기
from os.path import join
from entity.player import Player

pygame.init()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("space shooter")


bg_path = join("images", "background.png")
bg_surf = pygame.transform.scale(
    pygame.image.load(bg_path).convert_alpha(), (WINDOW_WIDTH, WINDOW_HEIGHT)
)

clock = pygame.time.Clock()


def main():
    running = True
    direction = pygame.Vector2(0, 0)
    all_sprite_group = pygame.sprite.Group()

    Player(all_sprite_group)

    while running:
        dt = clock.tick(30) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if direction.length() > 0:
            direction.normalize_ip()

        display_surface.fill("gray")

        all_sprite_group.update(dt)
        all_sprite_group.draw(display_surface)

        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
