from cocos import scene
from cocos.director import director

from layer import *


def __main():
    # 初始化 director（导演）
    director.init()
    #
    # 用刚才定义的 SpriteLayer 类创建一个 scene（场景）
    main_layer = GameLayer()
    s = scene.Scene(main_layer)
    #
    # 使用 run 函数来运行我们的程序
    director.run(s)


__main()
