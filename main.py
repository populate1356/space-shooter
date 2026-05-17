import pygame
from os.path import join

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1290, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("space shooter")


class Player(pygame.sprite.Sprite):
    path: str = join("images", "player.png")
    speed: float = 100
    velocity: pygame.Vector2 = pygame.Vector2(0, 0)

    def __init__(self, group: pygame.sprite.Group):
        super().__init__(group)
        self.image = pygame.image.load(Player.path).convert_alpha()
        self.rect: pygame.FRect = self.image.get_frect(
            center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
        )

    def update(self, dt: float):
        keys = pygame.key.get_pressed()
        self.velocity.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
        self.velocity.y = int(keys[pygame.K_s]) - int(keys[pygame.K_w])

        if self.velocity.length() > 0:
            self.velocity.normalize_ip()

        self.rect.center += self.velocity * Player.speed * dt
        self.rect.clamp_ip(pygame.Rect(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT))


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
