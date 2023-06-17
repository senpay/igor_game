TITLE = "Game"
WIDTH = 600
HEIGHT = 600

import random
import pgzero
import pgzrun


# This is here just to make the IDE happy
# otherwise it is going to complain about screen.* calls
screen: pgzero.screen.Screen
keyboard: pgzero.keyboard.Keyboard
from pgzero.actor import Actor

class Fire(Actor):
    RELATIVE_POSITION = (0, 60)

    def __init__(self, spaceship: Actor, relative_position: tuple = RELATIVE_POSITION):
        super().__init__("fire.png")
        self.relative_position = relative_position
        self.spaceship = spaceship
        self.align_with_spaceship()
        self.visible = False

    def update(self):
        if keyboard.left or keyboard.right or keyboard.up or keyboard.down:
            self.visible = True
            self.align_with_spaceship()
        else:
            self.visible = False

    def align_with_spaceship(self):
            self.x = self.spaceship.x + self.relative_position[0]
            self.y = self.spaceship.y + self.relative_position[1]

    def draw(self):
        if self.visible:
            super().draw()


class SpaceShip(Actor):
    VELOCITY = 2

    def __init__(self):
        super().__init__("spaceship.png")
        self.pos = (WIDTH/2, HEIGHT/2)

    def update(self):
        if keyboard.left:
            self.x -= self.VELOCITY
            if self.x < 0:
                self.x = 0
        if keyboard.right:
            self.x += self.VELOCITY
            if self.x > WIDTH:
                self.x = WIDTH
        if keyboard.up:
            self.y -= self.VELOCITY
            if self.y < 0:
                self.y = 0
        if keyboard.down:
            self.y += self.VELOCITY
            if self.y > HEIGHT:
                self.y = HEIGHT

space_ship = SpaceShip()
fire_left = Fire(space_ship, (-15, 18))
fire_right = Fire(space_ship, (15, 18))

sprites = [space_ship, fire_left, fire_right]

# This function is called every frame
# fps must be 60
def update(dt):
    for sprite in sprites:
        sprite.update()

def draw():
    screen.fill((0, 51, 102))
    for sprite in sprites:
        sprite.draw()

pgzrun.go()