import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('dfs paigem/images/laser-bolts.png')  # Load the bullet image
        self.image = pygame.transform.scale(self.image, (32, 32))  # Scale the bullet
        self.rect = self.image.get_rect(center=(x +80, y + 30))  # Set initial position
        self.speed = 250  # Bullet speed in pixels per second

    def update(self):
        # Move the bullet to the right
        self.rect.x += self.speed * 0.016  # Assuming 60 FPS, adjust for frame time
        # Destroy the bullet if it goes off-screen
        if self.rect.right < 0 or self.rect.left > 800:
            self.kill()

    def fire(self, x, y):
        self.rect.center = (x + 90, y - 8)  # Set the bullet's position
        self.add(self.groups())  # Add it back to its groups if needed

    def die(self):
        self.kill()  # Remove the bullet from all groups