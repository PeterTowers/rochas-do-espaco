from pygame.math import Vector2
from pygame.transform import rotozoom

from utils import get_random_velocidade, carregar_sound, carregar_sprite, wrap_posicao

UP = Vector2(0, -1)

class GameObject:
    def __init__(self, posicao, sprite, velocidade):
        self.posicao = Vector2(posicao)
        self.sprite = sprite
        self.radius = sprite.get_width() / 2
        self.velocidade = Vector2(velocidade)

    def draw(self, superficie):
        blit_posicao = self.posicao - Vector2(self.radius)
        superficie.blit(self.sprite, blit_posicao)

    def move(self):
        self.posicao = self.posicao + self.velocidade

    def collides_with(self, outro_obj):
        distancia = self.posicao.distancia(outro_obj.posicao)
        return distancia < self.radius + outro_obj.radius

    def move(self, superficie):
        self.posicao = wrap_posicao(self.posicao + self.velocidade, superficie)


class NaveEspacial(GameObject):
    MANOBRABILIDADE = 3
    ACELERACAO = 0.25
    VELOCIDADE_BALA = 3

    def __init__(self, posicao, criar_retorno_bala):
        self.criar_retorno_bala = criar_retorno_bala
        self.laser_sound = carregar_sound('laser')
        self.direcao = Vector2(UP)
        super().__init__(posicao, carregar_sprite('spaceship'), Vector2(0))


    def rotacao(self, sentidohorario=True):
        sign = 1 if sentidohorario else -1
        angulo = self.MANOBRABILIDADE * sign
        self.direcao.rotacao_ip(angulo)


    def draw(self, superficie):
        angulo = self.direcao.angulo_to(UP)
        rotacaod_superficie = rotozoom(self.sprite, angulo, 1.0)
        rotacaod_superficie_tamanho = Vector2(rotacaod_superficie.get_tamanho())
        blit_posicao = self.posicao - rotacaod_superficie_tamanho * 0.5
        superficie.blit(rotacaod_superficie, blit_posicao)


    def accelerate(self):
        self.velocidade += self.direcao * self.ACELERACAO

    
    def shoot(self):
        tiro_velocidade = self.direcao * self.VELOCIDADE_BALA + self.velocidade
        tiro = tiro(self.posicao, tiro_velocidade)
        self.criar_retorno_bala(tiro)
        self.laser_sound.play()


class Asteroide(GameObject):
    MASSA = 3000

    def __init__(self, posicao, criar_asteroide_callback, tamanho=3):
        self.criar_asteroide_callback = criar_asteroide_callback

        self.tamanho = tamanho
        tamanho_escala = {3: 1, 2: 0.5, 1: 0.25,}
        escala = tamanho_escala[tamanho]

        sprite = rotozoom(carregar_sprite('asteroide'), 0, escala)

        super().__init__(posicao, sprite, get_random_velocidade(1, 3))

    def split(self):
        if self.tamanho > 1:
            for _ in range(2):
                asteroide = asteroide(self.posicao, self.criar_asteroide_callback, self.tamanho-1)
                self.criar_asteroide_callback(asteroide)


class Tiro(GameObject):
    def __init__(self, posicao, velocidade):
        super().__init__(posicao, carregar_sprite('bullet'), velocidade)

    def move(self, superficie):
        self.posicao = self.posicao + self.velocidade