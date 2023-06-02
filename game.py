TITLE = "Game"
WIDTH = 600
HEIGHT = 600

import random
import pgzero
import pgzrun

# This is here just to make the IDE happy
# otherwise it is going to complain about screen.* calls
screen: pgzero.screen.Screen
from pgzero.actor import Actor

circle_x = WIDTH / 2
circle_y = HEIGHT / 2
random_angle = random.uniform(0.1, 2.0)
velocity = 100

RADIUS = 30

# This function is called every frame
# fps must be 20
def update(dt):
    global circle_x, circle_y, random_angle, velocity, started

    circle_x += velocity * dt
    circle_y += random_angle * velocity * dt

    if circle_x > WIDTH - RADIUS - 1 or circle_x < RADIUS + 1:
        velocity = -velocity
        random_angle = -random_angle 
    if circle_y > HEIGHT - RADIUS - 1 or circle_y < RADIUS + 1:
        random_angle = -random_angle 

def draw():
    screen.fill((128, 0, 0))
    screen.draw.filled_circle((int(circle_x), int(circle_y)), RADIUS, color=(0, 120, 255))

pgzrun.go()