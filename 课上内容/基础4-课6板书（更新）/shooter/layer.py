from cocos.layer import Layer
from pyglet.window.key import symbol_string

from star import Star
from player import Player
from enemy import Enemy

import random


class GameLayer(Layer):
    is_event_handler = True

    def __init__(self):
        super(GameLayer, self).__init__()
        self.player = Player()
        # 添加进场景
        self.add(self.player.sprite)
        self.schedule(self.update)
        self.stars = [Star() for i in range(30)]
        for s in self.stars:
            self.add(s.sprite)

        self.key_pressed_left = False
        self.key_pressed_right = False
        self.key_pressed_up = False
        self.key_pressed_down = False
        self.schedule(self.update)

        self.bullets = []
        self.enemies = []
        self.add_enemies()

    def update(self, dt):
        self.move_stars()
        self.move_bullets()
        self.move_enemies()
        self.remove_bullets()

        # 检查碰撞
        self.hit()
        # 按键控制
        x, y = self.player.sprite.position
        s = self.player.speed
        if self.key_pressed_left:
            x -= s
        if self.key_pressed_right:
            x += s
        if self.key_pressed_up:
            y += s
        if self.key_pressed_down:
            y -= s
        self.player.sprite.set_position(x, y)

    def on_key_press(self, key, modifiers):
        k = symbol_string(key)
        # 按下空格实现开火的功能
        if k == 'SPACE':
            self.player.fire()
            return

        self.key_pressed_left = (k == "LEFT")
        self.key_pressed_right = (k == "RIGHT")
        self.key_pressed_up = (k == "UP")
        self.key_pressed_down = (k == "DOWN")

    def on_key_release(self, key, modifiers):
        k = symbol_string(key)
        if k == "LEFT":
            self.key_pressed_left = False
        if k == "RIGHT":
            self.key_pressed_right = False
        if k == "UP":
            self.key_pressed_up = False
        if k == "DOWN":
            self.key_pressed_down = False

    def move_stars(self):
        for s in self.stars:
            s.move()

    def move_bullets(self):
        for b in self.bullets:
            b.move()

    def move_enemies(self):
        for e in self.enemies:
            e.move()

    def remove_bullets(self):
        bs = []
        for b in self.bullets:
            x, y = b.sprite.position
            if y > 800:
                b.sprite.kill()
            else:
                bs.append(b)
        self.bullets = bs

    def add_enemies(self):
        for i in range(3):
            x = i * 130 + 70
            y = 600
            e = Enemy()
            e.sprite.position = (x, y)
            self.enemies.append(e)
            self.add(e.sprite)

    def hit(self):
        for e in self.enemies:
            for b in self.bullets:
                x, y = b.sprite.position
                if e.sprite.contains(x, y):
                    # 子弹碰到敌人，把敌人杀死
                    e.die()
        # 把死了的敌人从画面中移走
        self.remove_dead_enemies()

    def remove_dead_enemies(self):
        es = []
        for e in self.enemies:
            if e.dead:
                e.sprite.kill()
            else:
                es.append(e)
        self.enemies = es
