def log(*args, **kwargs):
    print(*args, **kwargs)


#
# =====
# 类 与 面向对象
# =====
#
# 语言自带的数据类型有限, 要表示复杂的数据, 必须有复杂的数据类型
# 我们可以用字典表示复杂类型, 但 Python 提供一种机制被称之为 面向对象(Object Oriented)
#
# Python 面向对象编程中的 类, 就是语言提供的自定义数据类型的机制
# 它可以比字典更方便地表示复杂类型, 并能实现更多功能
# 例子如下
#

# class 是用来声明 类 的特殊语法
# Student 是类名, 一般首字母大写(驼峰命名法(搜))
# 括号中的 object 是继承的父类, object 是 Python 自带的最基础的类
# 类 中双下划线的 函数 和 变量 叫 魔法函数/魔法变量(稍后会讲)
# 先看如何使用再看定义方法, 这是一个创建类的标准方法
class Student(object):
    # 定义一个函数, 类的函数叫 方法 (单纯只是名字不同)
    # __init__ 是一个特殊的名字
    # 第一个参数叫 self, 你可以随意取名, 但强烈建议使用 self (大家都是这么叫它)
    def __init__(self):
        log('初始化的时候会调用这个函数')
        # 用 self.变量名 来创造一个只有类的实例才能访问的变量, 这句话之后会解释
        self.name = 'gua'
        self.height = 169


# 对 类 调用得到一个「类的实例」
# 赋值给变量 s1
# 这时候 s1 引用的是一个 Student 类型(也就是对象 Student 的实例)
# 也称之为 对象
s1 = Student()

# 可以通过 . 语法访问对象的属性(也就是 __init__ 函数中
# 用 self.变量名 创造的变量)
# 类的变量叫做 属性(单纯只是名字不同)
log('class, s1', s1.name, s1.height)
# 输出如下
# class, s1 gua 169


# ==
# 可以改变 s1 的属性值
s1.name = 'xiaogua'
s1.height = 1.69
log('class, s1 属性', s1.name, s1.height)
# 输出如下
# class, s1 属性 xiaogua 1.69


# ==
# 可以创建多个互相独立的实例
# 下面的例子可以看到, s2 和 s3 是互相独立的
s2 = Student()
s3 = Student()
s2.name = 'gua II'
s3.name = '三代瓜'
log(s2.name, s3.name)


# ==
# 可以给类增加一些方法(函数)
class StudentInfo(object):
    def __init__(self):
        self.name = 'gua'
        self.height = 169

    def show(self):
        log('student info', self.name, self.height)

    def update(self, name, height):
        self.name = name
        self.height = height


# 初始化
info = StudentInfo()
# info.name = 'info name'
# info.height = 100


# 调用 info 的 show 方法
# 注意, show 的第一个参数 self 是不用传递的
# Python 自动帮你传递第一个参数
# 下面这句实际上相当于 StudentInfo.show(info)
# 这是一个 Python 提供的方便书写的语法(这种我们称之为 语法糖)
info.show()

# 调用 info 的 update 方法
# 也是不用传递 self 的
info.update('xiao', 169.98)

info.show()


# ==
# 封装, 上面 show 和 update 就是封装的例子
# 意思是说把一些操作做好, 对外部来说只需要简单调用即可
#


# =
# 继承
# 继承是说, 父类的东西你可以直接拿来用
class Phone(object):
    def __init__(self):
        self.price = 0

    def off(self):
        log('关机, 手机')

    def on(self):
        log('开机, 手机')


# 注意, AnZhuo 类继承自 Phone 类, 写法如下
class AnZhuo(Phone):
    def on(self):
        log('安卓, 开机')


# 初始化并调用
p = Phone()
p.on()
p.off()

a = AnZhuo()
# 因为 AnZhuo 实现了自己的 on 所以这里调用的是自己的
a.on()

# 下面的这句 a.off() 能调用成功, 虽然 AnZhuo 类没有实现 off() 方法
# 但是 Python 会自动在父类中查找 off() 方法
# off 是继承自父类的方法, 所以被调用了
a.off()


#
# def add(a, b):
#     return a + b
#
#
# log(add(1, 2))
# log(add('sss', 'www'))

# =
# 类主要的优势就是 字典的替代品 和 可封装方法
# 其他上课要讲的杂项


# ===
# 魔法方法和魔法属性
# ===
class Circle(object):
    def __init__(self, radius):
        self.r = radius

    # 双下划线包围的方法叫做魔法方法
    # __add__ 是一个魔法方法
    # 一些特殊的操作符实际上是调用了这些魔法方法而已(看例子)
    def __add__(self, number):
        return self.r + number

    def show(self):
        log('circle.show, ', self.r)

    def __str__(self):
        return '自定义的方法，r:{}'.format(self.r)


c = Circle(10)
c.show()
log('circle + ', c + 20)
# c + 20 实际上变成了以下这句, 这是 Python 约定的
# c.__add__(20)

log('在这里', c)

# 输出如下
# circle.show,  10
# circle +  30


# Python 中 数字也是对象
# 所以下面的表达式中
# 1 + 2
# 相当于
# (1).__add__(2)
log(1 + 2)
log('数字也是对象', (1).__add__(2))

log(1)
log((1).__str__(), [1, 2, 3].__str__())

# 双下划线包围的属性叫做魔法属性
log('魔法属性', c.__class__.__name__)
#
# 魔法方法有很多, 这里不一一列举了, 给出资料即可
# 也就是说, Python 中的操作符实际上是一些特殊的函数
# 想知道具体的话, 可以参考下面的链接(想看的话随便看看即可, 来日方长, 现在不用看)
# http://pyzh.readthedocs.io/en/latest/python-magic-methods-guide.html#id1
