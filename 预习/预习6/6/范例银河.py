from cocos import scene
from cocos.layer import Layer
from cocos.director import director
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


class SpriteLayer(Layer):
    def __init__(self):
        super(SpriteLayer, self).__init__()
        # 使用 Sprite 获得一张图片
        self.actor = Sprite('images/fighter.png')
        # 可以设置图片的位置
        self.actor.position = (320, 240)
        # 添加进场景
        self.add(self.actor)
        self.schedule(self.update)
        self.stars = [Star() for i in range(30)]
        for s in self.stars:
            self.add(s.sprite)

    def update(self, dt):
        self.move_stars()

    def move_stars(self):
        for s in self.stars:
            s.move()


def __main():
    # 初始化 director（导演）
    director.init()
    #
    # 用刚才定义的 SpriteLayer 类创建一个 scene（场景）
    main_layer = SpriteLayer()
    s = scene.Scene(main_layer)
    # 
    # 使用 run 函数来运行我们的程序
    director.run(s)


__main()
