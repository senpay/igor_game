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

class SpaceShip(Actor):
    pass

space_ship = SpaceShip("spaceship.png")
space_ship.pos = (WIDTH/2, HEIGHT/2)

# This function is called every frame
# fps must be 60
def update(dt):
    pass

def draw():
    screen.fill((0, 51, 102))
    space_ship.draw() 

pgzrun.go()