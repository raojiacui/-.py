def log(*args, **kwargs):
    print(*args, **kwargs)


# =====
# *args (多参数)
# =====
#
# 在函数有多个参数的时候, 或者接受无限参数的时候, Python 提供便捷的处理方法, 就是 *args 多参数
def add_all(a, b, c, d, e, f, g):
    '''
    函数接受 7 个 int 参数并且返回 它们的合
    '''
    return a + b + c + d + e + f + g


# 调用方式如下
log('add all', add_all(1, 2, 3, 4, 5, 6, 7))

# 参数过多, 调用起来很麻烦
# 简便的方式是通过一个 list 装参数然后传给函数
# Python 提供的机制如下
# 给一个 list 加上 * 当参数传递的时候
# 这个 list 会被解开分别传递给函数
arg_list = [1, 2, 3, 4, 5, 6, 7]
log('add all arg_list', add_all(*arg_list))


# 在这个例子中, add_all 接受 7 个参数, 参数 *arg_list 就是把 arg_list 拆成独立的参数病分别传给 add_all


# 输出如下
# add all 28
# add all arg_list 28


# *arg 还可以用作定义函数时的参数表示
# 方便函数的处理
# 请注意, *args 中的 args 可以是任意变量名, 我们只是因为习惯所以使用 args 这个名字
def add_numbers(*args):
    '''
    注意, args 是一个 list
    '''
    s = 0
    # 因为 args 是一个 list 所以我们可以遍历它
    for n in args:
        s += n
    return s


# 然后这样调用, 无论你传多少参数都会被视为是一个数组
log('add numbers', add_numbers(1, 2, 3, 4, 5))

# 或者继续刚才那样调用也是可以的
numbers = [1, 2, 3, 4, 5, 6]
log('add numbers list', add_numbers(*numbers))


# =====
# **kwargs  关键字参数
# =====
#
# 在 Python 中, 即使一个参数没有默认值, 也可以在调用时用参数名指定参数(见下方例子)
def gua(name, sex, height=169.0):
    print(name, sex, height)


gua('gua', 'male')
gua('gua', 'male', 1.69)
gua(height=1.69, name='gua', sex='male')

# 输出如下
# gua male 169.0
# gua male 1.69
# gua male 1.69


# 上面讲过使用 * 表示多参数
# 这里要讲的是 ** 关键字参数
# 和 *args 类似, 可以自行脑补测试一下
# 一般叫 **kwargs, 是 key word arguments 的缩写
# 对于上面的例子, 用 关键字参数 的方法如下
info = {
    'name': 'Gua',
    'sex': 'Male',
    'height': 169.9,
    # 'note': 123,
}
gua(**info)

# 输出如下
# Gua Male 169.9
#
info = {
    'name': 'Gua',
    'sex': 'Male',
    'height': 169.9,
    'note': 123,
}


def gua1(**kwargs):
    log('gua1 打印出来的结果，', kwargs)


gua1(**info)
gua1(name=1, age=2, weight=3)


# 同理, **kwargs 还可以用作定义函数时的参数表示
# 方便函数的处理
# 请注意, **kwargs 中的 kwargs 可以使任意变量名, 我们只是因为习惯所以使用 kwargs 这个名字
def print_info(**kwargs):
    '''
    注意, kwargs 是一个 dict
    '''
    log(kwargs)


# 然后这样调用, 无论你传多少关键字参数都会被视为是一个字典
log('** kwargs', print_info(name='GUA', height=169))

# 或者继续刚才那样调用也是可以的
log('** kwargs', print_info(**info))

# 注意, 下面的用法是错的, 因为 **kwargs 必须接受关键字参数
# log('错误', print_info('gua'))


# =====
# 把 *args, **kwargs 结合起来, 就可以在参数列表中混合普通参数和关键字参数
# print 函数就是一个这样的例子
