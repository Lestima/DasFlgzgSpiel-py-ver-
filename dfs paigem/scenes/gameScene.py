import pygame
import random
from ui.enemyObject import Enemy
from ui.bullet import Bullet
from scenes.gameOver import GameOverScene  # Import GameOverScene

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("gem")

# Load assets
sky = pygame.image.load('dfs paigem/images/sky.png')
mountain_far = pygame.image.load('dfs paigem/images/far_mountains.png')
mountain = pygame.image.load('dfs paigem/images/grassy_mountains.png')
cloud_mid = pygame.image.load('dfs paigem/images/clouds_mid.png')
cloud_front = pygame.image.load('dfs paigem/images/clouds_front.png')
player_img = pygame.image.load('dfs paigem/images/me262.png')
explosion_img = pygame.image.load('dfs paigem/images/explosion.png')

# Scale assets
sky = pygame.transform.scale(sky, (SCREEN_WIDTH, SCREEN_HEIGHT))
mountain_far = pygame.transform.scale(mountain_far, (SCREEN_WIDTH, SCREEN_HEIGHT))
mountain = pygame.transform.scale(mountain, (SCREEN_WIDTH, SCREEN_HEIGHT))
cloud_mid = pygame.transform.scale(cloud_mid, (SCREEN_WIDTH, SCREEN_HEIGHT))
cloud_front = pygame.transform.scale(cloud_front, (SCREEN_WIDTH, SCREEN_HEIGHT))
player_img = pygame.transform.scale(player_img, (60, 60))
explosion_img = pygame.transform.scale(explosion_img, (32, 32))

# Clock for controlling frame rate
clock = pygame.time.Clock()

class GameScene:
    def __init__(self):
        self.bg_layers = [
            {"image": sky, "speed": 0.1, "x": 0},
            {"image": mountain_far, "speed": 0.4, "x": 0},
            {"image": mountain, "speed": 0.6, "x": 0},
            {"image": cloud_mid, "speed": 1.2, "x": 0},
            {"image": cloud_front, "speed": 2.6, "x": 0},
        ]

        # Calculate size relative to screen
        screen_width = 800
        screen_height = 600
        player_width = int(screen_width * 0.2)  
        player_height = int(screen_height * 0.11) 

        self.player = pygame.sprite.Sprite()
        self.player.image = pygame.transform.scale(player_img, (player_width, player_height))
        self.player.rect = self.player.image.get_rect(center=(200, 300))

        self.player_speed = 5
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.score = 0
        self.last_fired = 0
        self.font = pygame.font.Font(None, 36)



    def spawn_enemy(self):
        """Spawn an enemy at a random position."""
        speed = random.randint(2, 5)
        y = random.randint(50, SCREEN_HEIGHT - 50)
        enemy = Enemy(SCREEN_WIDTH + 50, y, speed)
        self.enemies.add(enemy)

    def handle_input(self, keys, time):
        """Handle player movement and shooting."""
        if keys[pygame.K_LEFT]:
            self.player.rect.x -= self.player_speed
        if keys[pygame.K_RIGHT]:
            self.player.rect.x += self.player_speed
        if keys[pygame.K_UP]:
            self.player.rect.y -= self.player_speed
        if keys[pygame.K_DOWN]:
            self.player.rect.y += self.player_speed

        # Fire bullets
        if keys[pygame.K_SPACE] and time - self.last_fired > 300:
            bullet = Bullet(self.player.rect.centerx, self.player.rect.top)
            self.bullets.add(bullet)
            self.last_fired = time

        # Keep player within screen bounds
        self.player.rect.clamp_ip(screen.get_rect())

    def update_parallax(self):
        """Update the parallax background."""
        for layer in self.bg_layers:
            layer["x"] -= layer["speed"]
            if layer["x"] <= -SCREEN_WIDTH:
                layer["x"] = 0

    def draw_parallax(self):
        """Draw the parallax background."""
        for layer in self.bg_layers:
            screen.blit(layer["image"], (layer["x"], 0))
            screen.blit(layer["image"], (layer["x"] + SCREEN_WIDTH, 0))

    def check_collisions(self):
        """Check for collisions between bullets and enemies or player and enemies."""
        for bullet in pygame.sprite.groupcollide(self.bullets, self.enemies, True, True):
            self.score += 1

        if pygame.sprite.spritecollideany(self.player, self.enemies):
            print("Game Over! Final Score:", self.score)
                # After the game ends, transition to the GameOverScene
            game_scene = GameScene()

            game_over_scene = GameOverScene(screen, score=game_scene.score)  # Pass the final score
            game_over_scene.run()


    def run(self):
        """Main game loop."""
        running = True
        spawn_enemy_event = pygame.USEREVENT + 1
        pygame.time.set_timer(spawn_enemy_event, random.randint(1000, 3000))

        while running:
            time = pygame.time.get_ticks()
            keys = pygame.key.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == spawn_enemy_event:
                    self.spawn_enemy()

            # Update game objects
            self.handle_input(keys, time)
            self.update_parallax()
            self.bullets.update()
            self.enemies.update()
            self.check_collisions()

            # Draw everything
            screen.fill((0, 0, 0))
            self.draw_parallax()
            screen.blit(self.player.image, self.player.rect)
            self.bullets.draw(screen)
            self.enemies.draw(screen)

            # Display score
            score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
            screen.blit(score_text, (10, 10))

            pygame.display.flip()
            clock.tick(60)

        pygame.quit()

if __name__ == "__main__":
    game = GameScene()
    game.run()