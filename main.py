import pygame
import sys

from model import Field, Zombie, Player
from view import CharacterView

pygame.init()
eaten = 0

screen = pygame.display.set_mode((Field.WIDTH, Field.HEIGHT))
pygame.display.set_caption("My Pygame Game")

player = Player(10, Field.HEIGHT - Player.HEIGHT - 70)
playerview = CharacterView(player, screen)

zombie = Zombie(Field.HEIGHT - Player.HEIGHT - 70)
zombieview = CharacterView(zombie, screen)


clock = pygame.time.Clock()
FPS = 60

# Load the background image
background_img = pygame.image.load("background.png").convert()

# Main loop here
while True:
    # This just to be able to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()


    if keys[pygame.K_LEFT]:
        player.move_left()
    if keys[pygame.K_RIGHT]:
        player.move_right()
    if keys[pygame.K_SPACE]:
        player.jump()



    screen.blit(background_img, (0, 0))
    playerview.blit()
    zombieview.blit()

    # Set up the font
    font = pygame.font.SysFont("Arial", 36)
    escaped = zombie.reset_count

    # Render the text
    text = font.render(f"You were eaten {eaten} and escaped {escaped} times", True, (3, 245, 3))

    # Blit the text to the screen
    screen.blit(text, (200, 10))


    if playerview.touches(zombieview):
        eaten += 1
        lost = True
        zombie.reset()
        player.reset()

    clock.tick(FPS) 
    pygame.display.update()

