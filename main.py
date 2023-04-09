import pygame
import sys

from model import Field, Player

pygame.init()

screen = pygame.display.set_mode((Field.WIDTH, Field.HEIGHT))
pygame.display.set_caption("My Pygame Game")

player = Player(10, Field.HEIGHT - Player.HEIGHT - 10)
player_sprite = pygame.image.load(player.SPRITE_NAME)
player_rect = player_sprite.get_rect()
player_rect.x = player.x
player_rect.y = player.y

clock = pygame.time.Clock()
FPS = 60

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


    player_rect.x = player.x
    player_rect.y = player.y

    screen.fill((255, 255, 255))
    screen.blit(player_sprite, player_rect)

    clock.tick(FPS) 

    # if sprite1_rect.colliderect(sprite2_rect):
    #     # Set up the font
    #     font = pygame.font.SysFont("Arial", 36)

    #     # Render the text
    #     text = font.render("yammie zombie", True, (3, 3, 3))

    #     # Blit the text to the screen
    #     screen.blit(text, (200, 10))

    pygame.display.update()
