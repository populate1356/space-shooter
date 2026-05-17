import pygame
from os.path import join

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1290, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("space shooter")

player_path = join("images", "player.png")
player_surf = pygame.image.load(player_path).convert_alpha()
player_rect = player_surf.get_frect(
    center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
)  # <-- 새로운 코드

bg_path = join("images", "background.png")
bg_surf = pygame.transform.scale(
    pygame.image.load(bg_path).convert_alpha(), (WINDOW_WIDTH, WINDOW_HEIGHT)
)


def main():
    running = True
    direction = 1  # <--- 방향
    speed = 1  # <--- 속력
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if (
            player_rect.right >= WINDOW_WIDTH or player_rect.left <= 0
        ):  # <-- 방향 바꾸는 조건
            direction *= -1

        player_rect.right += speed * direction  # <-- 위치 업데이트
        display_surface.blit(bg_surf, (0, 0))
        display_surface.blit(player_surf, player_rect)  # <--- 위치 업데이트

        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
