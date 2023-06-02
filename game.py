TITLE = "Game"
WIDTH = 600
HEIGHT = 600
RADIUS = 30
VELOCITY = 70

import random
import pgzero
import pgzrun

RANDOM_ANGLE = random.uniform(0.1, 2.0)

# This is here just to make the IDE happy
# otherwise it is going to complain about screen.* calls
screen: pgzero.screen.Screen

class Circle:
    def __init__(self, x, y, radius):
        self._x = float(x)
        self._y = float(y)
        self._radius = radius
        self.velocity = VELOCITY
        self.angle = RANDOM_ANGLE

    @property
    def x(self):
        return int(self._x)
    
    @property
    def y(self):
        return int(self._y)
    
    @property
    def radius(self):
        return self._radius
    
    def move(self, dt):
        dx = self.velocity * dt
        
        self._x += dx
        self._y += self.angle * dx

        if self.x > WIDTH - RADIUS - 1 or self.x < RADIUS + 1:
            self.velocity = -self.velocity
            self.angle = -self.angle 
        if self.y > HEIGHT - RADIUS - 1 or self.y < RADIUS + 1:
            self.angle = -self.angle 

    
circle = Circle(HEIGHT / 2, WIDTH / 2, 30)


# This function is called every frame
# fps must be 20
def update(dt):
    circle.move(dt)
    

def draw():
    screen.fill((128, 0, 0))
    screen.draw.filled_circle((int(circle.x), int(circle.y)), circle.radius, color=(0, 120, 255))

pgzrun.go()