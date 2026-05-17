import pygame
from os.path import join

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1290, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("space shooter")

player_path = join("images", "player.png")
player_surf = pygame.image.load(player_path).convert_alpha()
pos = pygame.Vector2(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
player_rect = player_surf.get_frect(center=(pos))

bg_path = join("images", "background.png")
bg_surf = pygame.transform.scale(
    pygame.image.load(bg_path).convert_alpha(), (WINDOW_WIDTH, WINDOW_HEIGHT)
)

clock = pygame.time.Clock()


def main():
    running = True
    speed = pygame.Vector2(20, 10)
    while running:
        dt = clock.tick(30) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        player_rect.center += speed * dt
        display_surface.blit(bg_surf, (0, 0))
        display_surface.blit(player_surf, player_rect)

        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
