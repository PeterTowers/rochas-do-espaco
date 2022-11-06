import pygame

from utils import gerar_posicao_aleatoria, carregar_sprite, imprimir_texto
from models import GameObject, NaveEspacial, asteroidee

class SpaceRocks:
    DISTANCIA_MIN_ASTER_NAVE = 250
    DISTANCIA_MIN_ASTER_ASTER = 100

    def __init__(self):
        self._init_pygame()
        self.screen = pygame.display.set_mode((800, 600))
        self.background = carregar_sprite("space", False)
        self.relogio = pygame.time.Clock()
        self.font = pygame.font.Font(None, 64)
        self.mensagem = ""

        self.asteroides = []
        self.balas = []
        self.naveEspacial = NaveEspacial((400, 300), self.balas.append)

        for _ in range(6):
            while True:
                posicao = gerar_posicao_aleatoria(self.screen)
                if posicao.distancia_to(self.naveEspacial.posicao) > self.DISTANCIA_MIN_ASTER_NAVE:
                    if self.asteroides:
                        flag = True

                        for asteroidee in self.asteroides:
                            if posicao.distancia_to(asteroidee.posicao) < self.DISTANCIA_MIN_ASTER_ASTER:
                                flag = False
                                break

                        if flag:
                            break

                    else:
                        break

            self.asteroides.append(asteroidee(posicao, self.asteroides.append))


    def main_loop(self):
        while True:
            self._handle_input()
            self._process_game_logic()
            self._draw()


    def _init_pygame(self):
        pygame.init()
        pygame.display.set_caption("Space Rocks")


    def _handle_input(self):
        # Sair do jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                quit()
            elif (
                self.naveEspacial
                and event.type == pygame.KEYDOWN
                and event.key == pygame.K_SPACE
            ):
                self.naveEspacial.shoot()
        
        is_key_pressed = pygame.key.get_pressed()

        if self.naveEspacial:
            # Rotacao
            if is_key_pressed[pygame.K_RIGHT]:
                self.naveEspacial.rotacao(relogiowise=True)
            elif is_key_pressed[pygame.K_LEFT]:
                self.naveEspacial.rotacao(relogiowise=False)

            # Aceleracao
            if is_key_pressed[pygame.K_UP]:
                self.naveEspacial.aceleracao()

        if is_key_pressed[pygame.K_r] and not self.naveEspacial:
            self.__init__()


    def _process_game_logic(self):
        for game_object in self._get_game_objects():
            game_object.movimento(self.screen)

        if self.naveEspacial:
            for asteroide in self.asteroides:
                if asteroide.collides_with(self.naveEspacial):
                    # self.naveEspacial = None
                    # self.mensagem = "You lost! Press R to respawn."
                    # break
                    pass

        for bala in self.balas[:]:
            for asteroide in self.asteroides[:]:
                if asteroide.collides_with(bala):
                    self.asteroides.remove(asteroide)
                    self.balas.remove(bala)
                    asteroide.split()
                    break

        for bala in self.balas[:]:
            if not self.screen.get_rect().collidepoint(bala.posicao):
                self.balas.remove(bala)

        if not self.asteroides and self.naveEspacial:
            self.mensagem = "You won!"

        print(self.naveEspacial.direction)


    def _get_game_objects(self):
        game_objects = [*self.asteroides, *self.balas]

        if self.naveEspacial:
            game_objects.append(self.naveEspacial)

        return game_objects


    def _draw(self):
        self.screen.blit(self.background, (0, 0))

        for game_object in self._get_game_objects():
            game_object.draw(self.screen)

        if self.mensagem:
            imprimir_texto(self.screen, self.mensagem, self.font)
        
        pygame.display.flip()
        self.relogio.tick(60)

