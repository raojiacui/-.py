from cocos import scene
from cocos.layer import Layer
from cocos.director import director
from cocos.sprite import Sprite
from pyglet.window.key import symbol_string


class GameLayer(Layer):
    is_event_handler = True

    def __init__(self):
        super(GameLayer, self).__init__()
        self.sprite = Sprite("images/fighter.png")
        self.sprite.position = (320, 240)
        self.add(self.sprite)

        self.speed = 10
        self.key_pressed_left = False
        self.key_pressed_right = False
        self.key_pressed_up = False
        self.key_pressed_down = False

        self.schedule(self.update)

    def update(self, dt):
        x, y = self.sprite.position
        if self.key_pressed_left:
            x -= self.speed
        if self.key_pressed_right:
            x += self.speed
        if self.key_pressed_up:
            y += self.speed
        if self.key_pressed_down:
            y -= self.speed
        self.sprite.set_position(x, y)

    def on_mouse_press(self, x, y, buttons, modifiers):
        print('mouse press', x, y, buttons)
        print('size', self.sprite.width, self.sprite.height)

    def on_key_press(self, key, modifiers):
        self.key_pressed_left = symbol_string(key) == "LEFT"
        self.key_pressed_right = symbol_string(key) == "RIGHT"
        self.key_pressed_up = symbol_string(key) == "UP"
        self.key_pressed_down = symbol_string(key) == "DOWN"

    def on_key_release(self, key, modifiers):
        if symbol_string(key) == "LEFT":
            self.key_pressed_left = False
        if symbol_string(key) == "RIGHT":
            self.key_pressed_right = False
        if symbol_string(key) == "UP":
            self.key_pressed_up = False
        if symbol_string(key) == "DOWN":
            self.key_pressed_down = False


def __main():
    director.init()
    director.run(scene.Scene(GameLayer()))


__main()
