import pygame
import sys

class GameScene:
    def __init__(self, screen):
        self.screen = screen
        self.replay_button = None
        self.score = 0  # Placeholder for score, as data.score is passed in Phaser

    def preload(self):
        # Load images
        self.background = pygame.image.load('dfs paigem/images/fullcolor.png')
        self.play_button = pygame.image.load('dfs paigem/images/play-button.png')
        self.name = pygame.image.load('dfs paigem/images/game-name.png')

        # Scale images
        self.background = pygame.transform.scale(self.background, (800, 600))
        self.play_button = pygame.transform.scale(self.play_button, (160, 64))  # Adjusted scale
        self.name = pygame.transform.scale(self.name, (240, 80))  # Adjusted scale

    def create(self):
        # Draw background
        self.screen.blit(self.background, (0, 0))

        # Draw game name
        self.screen.blit(self.name, (382 - self.name.get_width() // 2, 215 - self.name.get_height() // 2))

        # Create replay button
        self.replay_button_rect = self.play_button.get_rect(center=(382, 330))
        self.screen.blit(self.play_button, self.replay_button_rect)

    def run(self):
        self.preload()
        running = True

        while running:
            self.create()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONUP:
                    if self.replay_button_rect.collidepoint(event.pos):
                        print("Starting level one...")  # Replace with actual scene transition
                        running = False


# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Start Scene")

# Run the game scene
game_scene = GameScene(screen)
game_scene.run()