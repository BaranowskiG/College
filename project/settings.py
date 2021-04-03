import pygame as pg
import random
vec = pg.Vector2


SCALE = 2
MAP = [16, 10]
BIT = 16
BG_SIZE = [MAP[0] * BIT * SCALE * 2, MAP[1] * BIT * SCALE]
SCREEN = pg.display.set_mode(BG_SIZE)

HERO_FRICTION = -0.22
HERO_ACC = 1.5
