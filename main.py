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
lost = False

# Set up the font
font = pygame.font.SysFont("Arial", 36)

# Main loop here
while True:
    # This just to be able to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    if lost:
        lost_text = font.render(f"You lost, hahaha! (press space to restart)", True, (234, 12, 3))
        screen.blit(lost_text, (50, 200))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            lost = False
            zombie.reset()
            player.reset()
        clock.tick(FPS) 
        pygame.display.update()
        continue

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


    escaped = 1

    # Render the text
    text = font.render(f"Eaten {eaten}; Escaped {escaped} ", True, (3, 255, 3))

    # Blit the text to the screen
    screen.blit(text, (200, 10))


    if playerview.touches(zombieview) or lost:
        eaten += 1
        lost = True

    clock.tick(FPS) 
    pygame.display.update()

