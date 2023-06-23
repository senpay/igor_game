import random
from pgzero.actor import Actor

WIDTH = 600
HEIGHT = 600

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
            self.velocity = -(self.velocity * random.uniform(1.01, 1.1))
        if self.top < -self.padding or self.bottom > HEIGHT + self.padding:
            self.k = -(self.k + self.angle_randomization)