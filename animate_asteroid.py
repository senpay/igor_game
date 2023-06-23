TITLE = "My cool game"
WIDTH = 600
HEIGHT = 600
BG_COLOR = (0, 51, 102)
RED = 200, 0, 0
WHITE = 255, 255, 255

import pgzero, pgzrun
from pgzero import music
from pygame import Rect
import datetime


# This is here just to make the IDE happy
# otherwise it is going to complain about screen.* calls
screen: pgzero.screen.Screen
keyboard: pgzero.keyboard.Keyboard

box = Rect(((WIDTH/2 - 100), 50), (200, 100))

from model.asteroid import Asteroid
from model.spaceship import Spaceship
from model.explosion import Explosion

music.play('music.mp3')


sprites = []
game_started = False
highscore = 0
now = datetime.datetime.now()
latest_score = now - now
start_time = 0

def update():
    global game_started
    global highscore
    global latest_score
    if len(sprites) and sprites[0].destroyed and game_started:
        latest_score = datetime.datetime.now() - start_time
        highscore = max(highscore, latest_score.total_seconds())
        game_started = False
    if game_started:
        for sprite in sprites:
            sprite.update()

def on_mouse_down(pos):
    global game_started
    global start_time
    global latest_score

    if box.collidepoint(pos):
        game_started = True
        start_time = datetime.datetime.now()
        latest_score = 0

        explosion = Explosion()
        asteroid = Asteroid()

        space_ship = Spaceship(WIDTH / 2, HEIGHT / 2, asteroid, explosion, keyboard)
        sprites.clear()
        sprites.append(space_ship)
        sprites.append(asteroid)
        sprites.append(explosion)

def draw():
    screen.fill(BG_COLOR)
    if not game_started:
        screen.draw.rect(box, RED)
        screen.draw.textbox("Start new game", box, color="orange")
        screen.draw.text(f"Don't let an asteroid to hit your spaceship!\nUse arrows to move the spaceship", (30, 500), color="white")
        screen.draw.text(f"You survived for: {int(latest_score.total_seconds())} seconds", (30, 550), color="white")
        screen.draw.text(f"Highscore: {int(highscore)} seconds", (30, 570), color="white")
    else:
        for sprite in sprites:
            sprite.draw()
        screen.draw.text(f"Power: {sprites[0].power}%", (30, 500), color="white")

pgzrun.go()