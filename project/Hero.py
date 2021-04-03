from settings import *


class Hero(pg.sprite.Sprite):
    animation = {
        "idle": [],
        "attack": [],
        "hit": [],
        "run": []
    }

    def __init__(self, position: vec):
        super().__init__()
        self.current_sprite = 0
        self.facing_right = True
        self.can_jump = False
        self.is_attacking = False
        self.pos = position
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.gravity = 10
        self.hp = 3
        self.image = pg.image.load("assets/hero_idle/sprite_0.png")
        self.image = pg.transform.scale(self.image, [BIT * SCALE, BIT * SCALE])
        self.rect = self.image.get_rect()
        self.__prepare_assets()

    def update(self):
        self.acc = vec(0, 2.5)
        SCREEN.blit(self.image, self.pos)
        self.move()

        self.acc += self.vel * HERO_FRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.x > BG_SIZE[0]:
            self.pos.x = -self.rect.width
        if self.pos.x < -self.rect.width:
            self.pos.x = BG_SIZE[0]

        self.rect.topleft = self.pos

    def move(self):
        key = pg.key.get_pressed()
        self.animate("idle")
        self.is_attacking = False
        if key[pg.K_d]:
            self.__move_right()
        if key[pg.K_a]:
            self.__move_left()
        if key[pg.K_k]:
            self.__attack()
            self.is_attacking = True

    def __move_right(self):
        self.acc.x = HERO_ACC
        self.facing_right = True
        self.animate("run")

    def __move_left(self):
        self.acc.x = -HERO_ACC
        self.facing_right = False
        self.animate("run")

    def __attack(self):
        self.animate("attack")

    def jump(self):
        if self.can_jump:
            self.vel.y = -40
        self.can_jump = False

    def is_colliding_with(self, sprite):
        return self.rect.colliderect(sprite.rect)

    def __prepare_assets(self):
        for key, value in self.animation.items():
            sprite_count = 6 if key == "run" else 4
            for i in range(0, sprite_count):
                image = pg.image.load(f"assets/hero_{key}/sprite_{i}.png")
                image = pg.transform.scale(image, [BIT * SCALE, BIT * SCALE])
                value.append(image)

    def animate(self, name):
        self.current_sprite += 0.25
        if self.current_sprite >= len(self.animation[name]):
            self.current_sprite = 0

        if self.facing_right:
            self.image = self.animation[name][int(self.current_sprite)]
        else:
            self.image = pg.transform.flip(self.animation[name][int(self.current_sprite)], True, False)