class Field:
    
    WIDTH = 640
    HEIGHT = 480

class Player:
    '''A zombie that can move around the screen. Sprite - zombie.png'''

    WIDTH = 45
    HEIGHT = 75
    SPRITE_NAME = "zombie.png"
    SPEED = 4

    JUMP_SPEED = 15

    GRAVITY_ACCELERATION = 1

    def __init__(self, x, y):
        self._resting_y = y
        self._x = x
        self._y = y
        self._jumping = False
        self._jumping_speed = 0

    def _move(self, dx, dy):
        self._x += dx
        self._y += dy

    def move_left(self):
        if self._x > 0:
            self._move(-self.SPEED, 0)

    def move_right(self):
        if self._x < Field.WIDTH - Player.WIDTH:
            self._move(self.SPEED, 0)

    def jump(self):
        if self._jumping:
            return
        self._jumping = True
        self._jumping_speed = Player.JUMP_SPEED


    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        if self._jumping:
            self._jumping_speed -= Player.GRAVITY_ACCELERATION
            self._move(0, -self._jumping_speed)

            if self._y >= self._resting_y:
                self._jumping = False

        return self._y

    


