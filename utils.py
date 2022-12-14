import math
import random

from pathlib import Path
from pygame import Color

from pygame.image import load
from pygame.math import Vector2
from pygame.mixer import Sound

def load_sprite(name, with_alpha=True):
    p = Path(f"rochas-do-espaco/assets/sprites/{name}.png")
    loaded_sprite = load(p)

    if with_alpha:
        return loaded_sprite.convert_alpha()
    else:
        return loaded_sprite.convert()

def wrap_position(position, surface):
    x, y = position
    w, h = surface.get_size()

    return Vector2(x % w, y % h)

def get_random_position(surface):
    return Vector2(
        random.randrange(surface.get_width()),
        random.randrange(surface.get_height())
    )

def get_random_velocity(min_speed, max_speed):
    speed = random.randint(min_speed, max_speed)
    angle = random.randrange(0, 360)

    return Vector2(speed, 0).rotate(angle)


def load_sound(name):
    return (Sound(Path(f"rochas-do-espaco/assets/sounds/{name}.wav")))


def print_text(surface, text, font, color=Color('tomato')):
    text_surface = font.render(text, True, color)

    rect = text_surface.get_rect()
    rect.center = Vector2(surface.get_size()) / 2

    surface.blit(text_surface, rect)

def colisao(asteroide1, asteroide2):
    theta = math.atan2(asteroide1.position.y - asteroide2.position.y, asteroide1.position.x - asteroide2.position.x)

    angulo1 = 2 * tan - math.atan2(asteroide1.position.y, asteroide1.position.x)
    angulo2 = 2 * tan - math.atan2(asteroide2.position.y, asteroide2.position.x)

        