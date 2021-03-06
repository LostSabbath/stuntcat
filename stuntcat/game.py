import time

import pygame

from stuntcat.scenes import LoadingScene
from stuntcat.scenes import CatUniScene


class Game:
    FLAGS = 0
    WIDTH = 960
    HEIGHT = 540
    FPS = 30

    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT), self.FLAGS)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("a + d keys: lean left/right. Arrow left/right move left/right. Catch fish. Avoid shark lazers elephant stomps.")

        self.running = True
        self.scenes = [
            # LoadingScene(self),
            CatUniScene(self)
        ]

    def tick(self, dt):
        """
        Propagate a tick to the highest active scene.
        If a scene responds with a truthy value, the tick will
        continue to be propagated.
        """
        for i in self.scenes[::-1]:
            if i.active:
                if not i.tick(dt):
                    break

        self.clock.tick(self.FPS)

    def render(self):
        """ Propagate a render to the highest active scene.

        If ascene.propagate_render is True, the render will
            continue to be propagated.
        """
        # for i in self.scenes[::-1]:
        #     if i.active:
        #         if not i.render():
        #             break
        # pygame.display.flip()

        all_rects = []
        for ascene in self.scenes[::-1]:
            if ascene.active:
                rects = ascene.render()
                if rects is not None:
                    all_rects.extend(rects)
                if not getattr(ascene, 'propagate_render', False):
                    break
        print(all_rects)
        pygame.display.update(all_rects)

    def events(self):
        """
        Standard event loop. Will propagate events to scenes
        following the same rules as tick and render.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            for i in self.scenes[::-1]:
                if i.active:
                    if not i.event(event):
                        break

    def mainloop(self):
        """
        Handle the game mainloop until self.running is set to
        a falsey value. Usually form pygame.QUIT.
        """

        dt = 0
        while self.running:
            fs = time.time()
            self.tick(dt)
            self.render()
            self.events()
            dt = (time.time() - fs) * 1000

        pygame.quit()
