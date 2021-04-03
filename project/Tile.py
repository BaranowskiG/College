import pygame as pg


class Tile(pg.sprite.Sprite):

    def __init__(self, image, position, screen):
        super().__init__()
        self.image = image
        self.rect = pg.Rect(position[0], position[1], image.get_width(), image.get_height())
        self.position = position
        screen.blit(self.image, self.position)
