TITLE = "Game"
WIDTH = 384
HEIGHT = 384

import pgzero
import pgzrun

# This is here just to make the IDE happy
# otherwise it is going to complain about screen.* calls
screen: pgzero.screen.Screen
from pgzero.actor import Actor

circle_x = WIDTH / 2
circle_y = HEIGHT / 2

class Alex(Actor):

    SPRITE_PATH_BASE = "alex"
    FRAMES = 2
    FRAME_INCREMENT = 0.03

    def __init__(self, x, y):
        super().__init__(f"{self.SPRITE_PATH_BASE}/idle/front/0.png")
        self.side = "front"
        self.state = "idle"
        self.x = x
        self.y = y
        self.counter = 0.0
        
    def update(self):
        self.counter += self.FRAME_INCREMENT
        if int(self.counter) >= self.FRAMES:
            self.counter = 0.0
        self.image = f"{self.SPRITE_PATH_BASE}/{self.state}/{self.side}/{int(self.counter)}.png"
        if keyboard.up:
            self.side = "back"
            self.state = "walk"
            self.y -= 0.5
        elif keyboard.down:
            self.side = "front"
            self.state = "walk"
            self.y += 0.5
        elif keyboard.left:
            self.side = "side"
            self.state = "walk"
            self.x -= 0.5
        elif keyboard.right:
            self.side = "side"
            self.state = "walk"
            self.x += 0.5
        else:
            self.state = "idle"


alex = Alex(WIDTH / 2, HEIGHT / 2)

def update():
    alex.update()

def draw():
    screen.fill((100, 150, 100))
    alex.draw()

pgzrun.go()