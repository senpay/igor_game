import random

class Field:
    
    WIDTH = 640
    HEIGHT = 480


class Movable:
    '''A movable object that can move around the screen.'''

    SPEED = 4

    SPRITE_NAME_IDLE = None
    SPRITE_NAMES_MOVING = None

    def __init__(self, x, y):
        self._reset = 0
        self._x = x
        self._init_x = x
        self._y = y
        self._init_y = y

    def _move(self, dx, dy):
        self._x += dx
        self._y += dy

    def reset(self):
        self._reset += 1
        self._x = self._init_x
        self._y = self._init_y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y
    
    @property
    def reset_count(self):
        return self._reset
    
    def move_left(self):
        if self._x > 0:
            self._move(-self.SPEED, 0)

    def move_right(self):
        if self._x < Field.WIDTH - Player.WIDTH:
            self._move(self.SPEED, 0)


class Zombie(Movable):

    WIDTH = 45
    HEIGHT = 45
    SPRITE_NAMES_MOVING = ["zombie1.png", "zombie2.png"]
    SPRITE_NAME_IDLE = "zombie2.png"
    SPEED = 1

    def __init__(self, y):
        super().__init__(Field.WIDTH - Zombie.WIDTH, y)

    @property
    def x(self):
        self._x -= self.SPEED
        if self._x == 0:
            self._x = Field.WIDTH - Zombie.WIDTH
        return self._x
    


class Player(Movable):
    '''A zombie that can move around the screen. Sprite - zombie.png'''

    WIDTH = 45
    HEIGHT = 75
    SPRITE_NAMES_MOVING = ["man1.png", "man2.png"]
    SPRITE_NAME_IDLE = "man2.png"
    SPEED = 4

    JUMP_SPEED = 25

    GRAVITY_ACCELERATION = 1

    def __init__(self, x, y):
        super().__init__(x, y)
        self._resting_y = y
        self._jumping = False
        self._jumping_speed = 0

    def jump(self):
        if self._jumping:
            return
        self._jumping = True
        self._jumping_speed = Player.JUMP_SPEED
    
    @property
    def y(self):
        if self._jumping:
            self._jumping_speed -= Player.GRAVITY_ACCELERATION
            self._move(0, -self._jumping_speed)

            if self._y >= self._resting_y:
                self._jumping = False

        return self._y
    
    



    


