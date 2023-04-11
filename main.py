import pygame
import sys

from model import Field, Food, Player

pygame.init()

screen = pygame.display.set_mode((Field.WIDTH, Field.HEIGHT))
pygame.display.set_caption("My Pygame Game")

player = Player(10, Field.HEIGHT - Player.HEIGHT - 70)
player_sprite = pygame.image.load(player.SPRITE_NAME)
player_rect = player_sprite.get_rect()
player_rect.x = player.x
player_rect.y = player.y

food = Food(Field.HEIGHT - Player.HEIGHT - 40)
food_sprite = pygame.image.load(food.SPRITE_NAME)
food_rect = food_sprite.get_rect()
food_rect.x = food.x
food_rect.y = food.y


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


    player_rect.x = player.x
    player_rect.y = player.y

    screen.blit(background_img, (0, 0))
    screen.blit(player_sprite, player_rect)
    screen.blit(food_sprite, food_rect)


    if food_rect.colliderect(player_rect):
        # Set up the font
        font = pygame.font.SysFont("Arial", 36)

        # Render the text
        text = font.render("yammie niam niam", True, (3, 245, 3))

        # Blit the text to the screen
        screen.blit(text, (200, 10))

    clock.tick(FPS) 
    pygame.display.update()

