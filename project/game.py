import sys

from Hero import Hero
from Mushroom import Mushroom
from Tile import Tile
from settings import *


class Game:
    start = pg.time.get_ticks()
    is_playing = True
    tiles = []
    hero = Hero(vec([BIT * SCALE * 24, BIT * SCALE * 3]))
    score = 0
    mushrooms = []

    def restart_game(self):
        self.is_playing = True
        self.hero = Hero(vec([BIT * SCALE * 24, BIT * SCALE * 3]))
        self.score = 0

    def handle_events(self):
        for event in pg.event.get():
            esc_btn_pressed = pg.key.get_pressed()[pg.K_ESCAPE]
            red_btn_pressed = event.type == pg.QUIT
            if red_btn_pressed or esc_btn_pressed:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_w:
                    self.hero.jump()

    @staticmethod
    def draw_background():
        for i in range(0, 3):
            bg = pg.image.load(f"assets/background/bg_{i}.png")
            bg = pg.transform.scale(bg, BG_SIZE)
            SCREEN.blit(bg, [0, 0])
            SCREEN.blit(bg, [BG_SIZE[0], 0])

    def draw_tiles(self):
        hp = []

        for i in range(0, 3):
            heart = 22 if self.hero.hp > i else 23
            hp.append(heart)

        schema = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 24, hp[0], hp[1], hp[2], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 5, 6, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 5, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 4, 5, 5, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 5, 5, 6, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        ]

        for row in range(0, MAP[1]):
            for column in range(0, MAP[0] * 2):
                value = schema[row][column]
                if value == 0:
                    continue
                sprite_family = "hud" if 20 < value < 30 else "tiles"
                self.show_sprite(value, [row, column], sprite_family)

    def show_sprite(self, sprite_id, position, sprite_family):
        image = pg.image.load(f"assets/{sprite_family}/sprite_{sprite_id}.png")
        image = pg.transform.scale(image, [BIT * SCALE, BIT * SCALE])
        tile_position = [position[1] * BIT * SCALE, position[0] * BIT * SCALE]
        self.tiles.append(Tile(image, tile_position, SCREEN))

    def draw_text(self):
        font = pg.font.Font("assets/VT323.ttf", 30)
        text_surface = font.render(f'Score: {self.score}', False, (255, 255, 255))
        SCREEN.blit(text_surface, (35, 64))

    @staticmethod
    def update_view():
        pg.display.update()
        pg.time.Clock().tick(60)

    def run_game(self):

        while self.is_playing:

            # spawn mushrooms
            now = pg.time.get_ticks()
            if now - self.start > 3000 and len(self.mushrooms) < 3:
                self.start = now
                mushroom = Mushroom(vec(BIT * SCALE * random.randint(8, 32), (-BIT * SCALE)))
                self.mushrooms.append(mushroom)

            self.handle_events()
            self.draw_background()
            self.draw_tiles()
            self.hero.update()
            self.draw_text()

            for tile in self.tiles:
                if self.hero.is_colliding_with(tile):
                    self.hero.pos.y = tile.rect.top - self.hero.rect.height
                    self.hero.vel.y = 0
                    self.hero.can_jump = True
                for mushroom in self.mushrooms:
                    if mushroom.is_colliding_with(tile):
                        mushroom.pos.y = tile.rect.top - mushroom.rect.height + 1
                        mushroom.vel.y = 0
                        mushroom.can_jump = True

            for mushroom in self.mushrooms:
                mushroom.update()
                if mushroom.is_colliding_with(self.hero):
                    if self.hero.is_attacking:
                        mushroom.animate("hit")
                        self.mushrooms.remove(mushroom)
                        self.score += 1
                    else:
                        self.hero.pos = [BIT * SCALE * 24, BIT * SCALE * 3]
                        self.hero.hp -= 1

            if self.hero.hp == 0:
                self.is_playing = False
                self.restart_game()

            self.update_view()
