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
    speed = 200
    direction = pygame.Vector2(0, 0)
    while running:
        dt = clock.tick(30) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
        direction.y = int(keys[pygame.K_s]) - int(keys[pygame.K_w])
        if direction.length() > 0:
            direction.normalize_ip()
        player_rect.center += direction * speed * dt
        player_rect.clamp_ip(pygame.Rect(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT))
        display_surface.blit(bg_surf, (0, 0))
        display_surface.blit(player_surf, player_rect)

        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
