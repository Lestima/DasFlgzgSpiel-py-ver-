import pygame
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        original_image = pygame.image.load('dfs paigem/images/p51D.png').convert_alpha()
        scaled_image = pygame.transform.scale(original_image, (SCREEN_WIDTH * 0.15, SCREEN_HEIGHT * 0.075))
        self.image = pygame.transform.flip(scaled_image, True, False)  # Flip horizontally
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed

    def spawn(self, positionX, positionY):
        """Set the enemy's position and make it active."""
        self.rect.center = (positionX, positionY)

    def die(self):
        """Remove the enemy from all sprite groups."""
        self.kill()

    def update(self):
        """Update the enemy's position and check if it goes off-screen."""
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.die()

    def enemy_animate(self):
        """Placeholder for animations (Pygame doesn't have built-in animations)."""
        pass
