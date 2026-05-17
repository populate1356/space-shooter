import pygame

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("pygame shooter")


def main():
    running = True
    surf = pygame.Surface((100, 150))  # <--- 생성
    surf.fill("orange")  # <-- 색상 설정
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display_surface.fill((0, 0, 0))
        display_surface.blit(surf, (100, 100))  # <-- 화면에 붙이기
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
