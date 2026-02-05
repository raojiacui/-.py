from cocos import scene
from cocos.director import director
from cocos.layer import Layer
from cocos.text import Label
# 导入需要用到的东西


# 定义一个 class 继承自 Layer(cocos2d 提供的库)
# 这个 类 是我们要显示的画面
class HelloWorld(Layer):
    def __init__(self):
        super(HelloWorld, self).__init__()
        # 创建一个 标签（Label），内容为 “世界！”
        label = Label("世界!")
        # 使用 self.add 函数把 label 添加进画面
        # 默认坐标是 (0, 0) 在窗口左下角
        self.add(label)


def __main():
    # 初始化 director（导演），顶层导入的
    director.init()
    #
    # 用刚才定义的 HelloWorld 类创建一个 scene（场景）
    main_layer = HelloWorld()
    # local variable 'scene' referenced before assignment
    # scene = scene.Scene(main_layer)
    s = scene.Scene(main_layer)
    #
    # 使用 run 函数来运行我们的程序
    director.run(s)


__main()

