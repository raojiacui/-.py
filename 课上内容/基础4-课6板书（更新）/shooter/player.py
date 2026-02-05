from cocos.sprite import Sprite
from bullet import Bullet


class Player(object):
    def __init__(self):
        super(Player, self).__init__()
        self.speed = 5
        # 使用 Sprite 获得一张图片
        self.sprite = Sprite('images/fighter.png')
        # 可以设置图片的位置
        self.sprite.position = (320, 240)

    def fire(self):
        print('fire!')
        x, y = self.sprite.position
        b = Bullet(x, y)
        layer = self.sprite.parent
        layer.add(b.sprite)
        layer.bullets.append(b)
