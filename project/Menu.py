from settings import *
import sys
from game import Game


class Menu:

    @staticmethod
    def setup_app():
        icon = pg.image.load("assets/hud/sprite_24.png")
        pg.init()
        pg.display.set_caption("Game")
        pg.display.set_icon(icon)

    @staticmethod
    def draw_background():
        for i in range(0, 3):
            bg = pg.image.load(f"assets/background/bg_{i}.png")
            bg = pg.transform.scale(bg, BG_SIZE)
            SCREEN.blit(bg, [0, 0])
            SCREEN.blit(bg, [BG_SIZE[0], 0])

    @staticmethod
    def handle_events():
        for event in pg.event.get():
            esc_btn_pressed = pg.key.get_pressed()[pg.K_ESCAPE]
            red_btn_pressed = event.type == pg.QUIT
            if red_btn_pressed or esc_btn_pressed:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_p:
                    gameplay = Game()
                    gameplay.run_game()

    @staticmethod
    def draw_text():
        font = pg.font.Font("assets/VT323.ttf", 30)
        text_surface = font.render('A, D, W - move    K - attack    press P to start', False, (255, 255, 255))
        SCREEN.blit(text_surface, (250, SCREEN.get_height() - 50))

    def play(self):
        while True:
            self.setup_app()
            self.handle_events()
            self.draw_background()
            self.draw_text()
            pg.display.update()


if __name__ == '__main__':
    Menu().play()
