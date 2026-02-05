from cocos.sprite import Sprite

import random


class Star(object):
    def __init__(self):
        super(Star, self).__init__()
        self.sprite = Sprite('images/star.png')
        self.speed = 0
        self.reset_status()

    def reset_status(self):
        self.speed = random.randint(0, 5)
        x = random.randint(0, 640)
        y = random.randint(480, 600)
        self.sprite.position = (x, y)

    def move(self):
        x, y = self.sprite.position
        y -= self.speed
        self.sprite.position = (x, y)
        if y < 0:
            self.reset_status()
