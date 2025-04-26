import pygame
import sys
from scenes.gameScene import GameScene  # Import GameScene directly
from scenes.gameOver import GameOverScene  # Import GameOverScene

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600),pygame.RESIZABLE)
    pygame.display.set_caption("Game")

    # Initialize the game scene
    game_scene = GameScene()
    game_scene.run()

    # After the game ends, transition to the GameOverScene
    game_over_scene = GameOverScene(screen, score=game_scene.score)  # Pass the final score
    game_over_scene.run()
