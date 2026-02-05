from cocos.sprite import Sprite


class Bullet(object):
    def __init__(self, x, y):
        super(Bullet, self).__init__()
        self.sprite = Sprite('images/bullet.png')
        self.speed = 10
        self.sprite.position = (x, y)

    def move(self):
        x, y = self.sprite.position
        y += self.speed
        self.sprite.position = (x, y)
