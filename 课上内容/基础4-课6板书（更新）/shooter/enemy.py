from cocos.sprite import Sprite


class Enemy(object):
    def __init__(self):
        super(Enemy, self).__init__()
        self.sprite = Sprite('images/enemy.png')
        self.speed = 5
        self.sprite.position = (320, 640)
        self.dead = False

    def move(self):
        x, y = self.sprite.position
        y -= self.speed
        if y < 0:
            y = 500
        self.sprite.position = (x, y)

    def die(self):
        self.dead = True
