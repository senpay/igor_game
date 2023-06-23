from pgzero.actor import Actor

WIDTH = 600
HEIGHT = 600

class Fire(Actor):
    def __init__(self, relative_position: tuple):
        super().__init__("fire.png")
        self.relative_position = relative_position
        self.visible = False

    def show(self, x, y):
        self.x = x + self.relative_position[0]
        self.y = y + self.relative_position[1]
        self.visible = True
    
    def draw(self):
        if self.visible:
            super().draw()

    def hide(self):
        self.visible = False

class Spaceship(Actor):

    def __init__(self, x, y, asteroid, explosion, keyboard):
        super().__init__("spaceship.png")
        self.x = x
        self.y = y
        self.destroyed = False
        self.asteroid = asteroid
        self.explosion = explosion
        self.fire_left = Fire((-15, 20))
        self.fire_right = Fire((15, 20))
        self.keyboard = keyboard
        self._power = 100

    def update(self):
        self._handle_fires()
        self._update_power()
        self._move()
        self._check_walls()
        self._handle_collision()

    def draw(self):
        if not self.destroyed:
            self.fire_left.draw()
            self.fire_right.draw()
            super().draw()
    
    @property
    def velocity(self):
        if self._power > 0:
            return 5
        return 0.5
    
    @property
    def power(self):
        return int(self._power)

    def _handle_fires(self):
        if (self.keyboard.left or self.keyboard.right or
            self.keyboard.up or self.keyboard.down):
            self._show_fires()
        else:
            self._hide_fires()

    def _update_power(self):
        if ((self.keyboard.left or self.keyboard.right or
             self.keyboard.up or self.keyboard.down) and self._power > 0):
            self._power -= 0.5
        elif self._power < 100:
            self._power += 0.1

    def _move(self):
        if self.keyboard.left:
            self.x -= self.velocity
        if self.keyboard.right:
            self.x += self.velocity
        if self.keyboard.up:
            self.y -= self.velocity
        if self.keyboard.down:
            self.y += self.velocity
    
    def _check_walls(self):
        if self.x < 0:
            self.x = 0
        if self.x > WIDTH:
            self.x = WIDTH
        if self.y < 0:
            self.y = 0
        if self.y > HEIGHT:
            self.y = HEIGHT


    def _handle_collision(self):
        if self.collidepoint(self.asteroid.pos) and not self.destroyed:
            self.destroyed = True
            self.explosion.pos = self.pos
            self.explosion.show()

    def _show_fires(self):
        self.fire_left.show(self.x, self.y)
        self.fire_right.show(self.x, self.y)

    def _hide_fires(self):
        self.fire_left.hide()
        self.fire_right.hide()
