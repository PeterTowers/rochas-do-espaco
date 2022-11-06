import math
import random

from pathlib import Path
from pygame import Color

from pygame.image import load
from pygame.math import Vector2
from pygame.mixer import Sound

# Carrega as imagens (sprites) do jogo
def carregar_sprite(nome, with_alpha=True):
    sprite = load(Path(f"rochas-do-espaco/assets/sprites/{nome}.png"))

    if with_alpha:
        return sprite.convert_alpha()
    else:
        return sprite.convert()


# Faz um elemento sair de um lado da tela e aparecer no outro
def wrap_position(posicao, superficie):
    x, y = posicao
    w, h = superficie.get_size()

    return Vector2(x % w, y % h)


# Gera uma posicao aleatoriamente para os asteroides
def gerar_posicao_aleatoria(superficie):
    return Vector2(
        random.randrange(superficie.get_width()),
        random.randrange(superficie.get_height())
    )


# Gera um valor de velocidade e angulo de direcao para os asteroides
def gerar_velocidade_aleatoria(velocidade_min, velocidade_max):
    velocidade = random.randint(velocidade_min, velocidade_max)
    angulo = random.randrange(0, 360)

    return Vector2(velocidade, 0).rotate(angulo)


# Carrega os sons do jogo
def carregar_som(nome):
    return (Sound(Path(f"rochas-do-espaco/assets/sounds/{nome}.wav")))


# Mostra textos na tela
def imprimir_texto(superficie, texto, fonte, cor=Color('tomato')):
    superficie_texto = fonte.render(texto, True, cor)

    retangulo = superficie_texto.get_rect()
    retangulo.center = Vector2(superficie.get_size()) / 2

    superficie.blit(superficie_texto, retangulo)


def colisao(asteroide1, asteroide2):
    theta = math.atan2(asteroide1.position.y - asteroide2.position.y, asteroide1.position.x - asteroide2.position.x)

    angulo1 = 2 * tan - math.atan2(asteroide1.position.y, asteroide1.position.x)
    angulo2 = 2 * tan - math.atan2(asteroide2.position.y, asteroide2.position.x)

        