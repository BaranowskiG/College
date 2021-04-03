from settings import *


class Mushroom(pg.sprite.Sprite):

    animation = {
        "run": [],
        "hit": []
    }

    def __init__(self, position: vec):
        super().__init__()
        self.current_sprite = 0
        self.facing_right = bool(random.getrandbits(1))
        self.pos = position
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.gravity = 5
        self.image = pg.image.load("assets/mushroom_run/sprite_0.png")
        self.rect = self.image.get_rect()
        self.__prepare_assets()

    def update(self):
        direction = 0.8 if self.facing_right else -0.8
        self.acc = vec(direction, 2.5)
        SCREEN.blit(self.image, self.pos)
        self.animate("run")
        self.rect = pg.Rect(self.pos.x, self.pos.y, BIT * SCALE, BIT * SCALE)

        self.acc += self.vel * HERO_FRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.x > BG_SIZE[0]:
            self.pos.x = -self.rect.width
        if self.pos.x < -self.rect.width:
            self.pos.x = BG_SIZE[0]

    def __prepare_assets(self):
        for key, value in self.animation.items():
            sprite_count = 8 if key == "run" else 3
            for i in range(0, sprite_count):
                image = pg.image.load(f"assets/mushroom_{key}/sprite_{i}.png")
                image = pg.transform.scale(image, [BIT * SCALE, BIT * SCALE])
                value.append(image)

    def is_colliding_with(self, sprite):
        return self.rect.colliderect(sprite.rect)

    def animate(self, name):
        self.current_sprite += 0.8
        if self.current_sprite >= len(self.animation[name]):
            self.current_sprite = 0

        if self.facing_right:
            self.image = self.animation[name][int(self.current_sprite)]
        else:
            self.image = pg.transform.flip(self.animation[name][int(self.current_sprite)], True, False)
