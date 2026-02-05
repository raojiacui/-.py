from cocos import scene
from cocos.layer import Layer
from cocos.director import director
from cocos.sprite import Sprite


class SpriteLayer(Layer):
    def __init__(self):
        super(SpriteLayer, self).__init__()
        # 使用 Sprite 获得一张图片
        self.actor = Sprite('images/tank.jpg')
        # 可以设置图片的位置
        self.actor.position = (320, 240)
        # 添加进场景
        self.add(self.actor)


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
