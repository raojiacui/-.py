from cocos.text import Label
from cocos import scene
from cocos.layer import Layer
from cocos.director import director
from cocos.sprite import Sprite
from pyglet.window.key import symbol_string


class KeyLayer(Layer):
    # 要响应事件，必须在类的定义中加上这一句
    is_event_handler = True

    def __init__(self):
        super(KeyLayer, self).__init__()
        self.label = Label("按键: ", font_size=42)
        self.label.position = (100, 240)
        self.add(self.label)

    def update_text(self, key):
        # 用这个函数得到按键代码的字符串描述
        key_name = symbol_string(key)
        print('按键代码', key, key_name, self.label.element)
        # 为 label 设置新的显示文本
        self.label.element.text = key_name

    # 这个函数是自动被调用的，当有按键被按下的时候
    # key 是被按下的按键代码
    # modifiers 是同时被按下的 ctrl alt 之类的按键
    def on_key_press(self, key, modifiers):
        self.update_text(key)

    # 这个函数是自动被调用的，当有按键被松开的时候
    def on_key_release(self, key, modifiers):
        self.update_text(key)


def __main():
    # 初始化 director（导演）
    director.init()
    # 用刚才定义的 KeyLayer 类创建一个 scene（场景）
    main_layer = KeyLayer()
    s = scene.Scene(main_layer)
    # 使用 run 函数来运行我们的程序
    director.run(s)


__main()
