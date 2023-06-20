TITLE = "My cool game"
WIDTH = 600
HEIGHT = 600
BG_COLOR = (0, 51, 102)

import random
import pgzero, pgzrun
from pgzero.actor import Actor

# This is here just to make the IDE happy
# otherwise it is going to complain about screen.* calls
screen: pgzero.screen.Screen
keyboard: pgzero.keyboard.Keyboard

class Fire(Actor):
    def __init__(self, spaceship: Actor, relative_position: tuple):
        super().__init__("fire.png")
        self.spaceship = spaceship
        self.relative_position = relative_position
        self.visible = False
    
    def update(self):
        if keyboard.up or keyboard.down or keyboard.left or keyboard.right:
            self.visible = True
        else:
            self.visible = False

        self.x = self.spaceship.x + self.relative_position[0]
        self.y = self.spaceship.y + self.relative_position[1]

    def draw(self):
        if self.visible:
            super().draw()

class Asteroid(Actor):

    def __init__(self):
        super().__init__("asteroid.png")
        self.x = self.width + 10
        self.y = self.height + 10
        self.k = random.uniform(0.1, 2.0)
        self.velocity = 3
        self.angle_randomization = random.uniform(0.01, 0.09)
        self.padding = 15

    def update(self):
        self.x += self.velocity
        self.y += self.velocity * self.k
        self.angle += 1

        if self.left < -self.padding or self.right > WIDTH + self.padding:
            self.k = -(self.k + self.angle_randomization)
            self.velocity = -self.velocity
        if self.top < -self.padding or self.bottom > HEIGHT + self.padding:
            self.k = -(self.k + self.angle_randomization)

class Spaceship(Actor):

    VELOCITY = 5

    def __init__(self, asteroid):
        super().__init__("spaceship.png")
        self.x = WIDTH / 2
        self.y = HEIGHT / 2
        self.destroyed = False
        self.asteroid = asteroid

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
        if self.collidepoint(asteroid.pos):
            self.destroyed = True

    def draw(self):
        if not self.destroyed:
            super().draw()

asteroid = Asteroid()
space_ship = Spaceship(asteroid)
fire_right = Fire(space_ship, (15, 20))
fire_left = Fire(space_ship, (-15, 20))

sprites = [space_ship, fire_right, fire_left, asteroid]

def update():
    for sprite in sprites:
        sprite.update()
    

def draw():
    screen.fill(BG_COLOR)
    for sprite in sprites:
        sprite.draw()

pgzrun.go()