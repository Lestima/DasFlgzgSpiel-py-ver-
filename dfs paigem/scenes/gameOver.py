import pygame
import sys

class GameOverScene:
    def __init__(self, screen, score):
        self.screen = screen
        self.score = score
        self.replay_button = None

    def preload(self):
        # Load images
        self.background = pygame.image.load('dfs paigem/images/fullcolor.png')
        self.gameover = pygame.image.load('dfs paigem/images/gameover.png')
        self.replay = pygame.image.load('dfs paigem/images/replay-button.png')
        self.name = pygame.image.load('dfs paigem/images/game-name.png')

        # Scale images
        self.background = pygame.transform.scale(self.background, (800, 600))
        # self.gameover = pygame.transform.scale(self.gameover, (300, 100))
        # self.replay = pygame.transform.scale(self.replay, (160, 64))
        # self.name = pygame.transform.scale(self.name, (240, 80))

    def create(self):
        # # Draw background
        self.screen.blit(self.background, (0, 0))

        # # Draw game name
        # self.screen.blit(self.name, (382 - self.name.get_width() // 2, 215 - self.name.get_height() // 2))

        # # Draw replay button
        # self.replay_button_rect = self.replay.get_rect(center=(382, 330))
        # self.screen.blit(self.replay, self.replay_button_rect)

        # Display score
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.score}", True, (0, 0, 0), (255, 255, 255))
        self.screen.blit(score_text, (340, 270))

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
                        print("Restarting level one...")  # Replace with actual scene transition
                        running = False


# Example usage
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Game Over")

    # Pass the score to the GameOverScene
    game_over_scene = GameOverScene(screen, score=123)
    game_over_scene.run()
    