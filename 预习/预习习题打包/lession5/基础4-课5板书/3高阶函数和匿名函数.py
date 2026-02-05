def log(*args, **kwargs):
    print(*args, **kwargs)


# =====
# 高阶函数
# =====
#
# 高阶函数这个名字很唬人, 实际上概念很简单——函数可以作为参数传递
#
# 有什么用呢？灵活性高，舒适度佳
# 请看例子
#
# int 函数是 Python 内置函数, 是用来把数据转换成 int 类型的一个函数
log('int ', int(6.3))


def process(array, processor):
    '''
    array 是一个列表
    processor 是一个函数, 注意, 这是一个函数, 所以可以调用

    把 array 中的每个元素都用 processor 函数处理并返回一个新的 list
    '''
    result = []
    for a in array:
        # processor 必须能调用成功, 否则这里就跪了
        element = processor(a)
        result.append(element)
    return result


# 创建一个 list, 包含 3 个 float
array = [1.1, -2.2, 3.3]

# int str abs 分别是内置函数, 前两个是转换类型的, abs 是用来求绝对值的
int_list = process(array, int)
str_list = process(array, str)
abs_list = process(array, abs)
log('int_list', int_list)
log('str_list', str_list)
log('abs_list', abs_list)


# 输出结果如下
# 我们可以看到, process 函数通过 参数传进来的函数 对数据进行了处理
# int_list [1, -2, 3]
# str_list ['1.1', '-2.2', '3.3']
# abs_list [1.1, 2.2, 3.3]


# =====
# 匿名函数 lambda
# =====
#
# 有时候要传递高阶函数的时候, 函数很短, 可能就一行
# 如果去定义一个新函数有人觉得划不来, 就想了一个偷懒的办法
# 那就是匿名函数
# 匿名函数在 Python 中叫 lambda(一个数学符号)
# 匿名函数的意思是没有函数名, 一般定义了就用
# 需要注意的是, Python 设计这样的只能有一行的匿名函数就是为了让人尽量少用它


# 例子
# 定义一个 square 函数求平方
def square(n):
    return n * n


# 用上面的 process 函数处理试试
array = [1, 2, 3]
square_list = process(array, square)
log('square_list', square_list)

add1 = lambda n: n + 1
'''
上面这行相当于
def add1(n):
    return n + 1
'''

add_list1 = process(array, add1)
add_list2 = process(array, lambda n: n + 1)
log('add_list1', add_list1)
log('add_list2', add_list2)

# 输出结果如下
# square_list [1, 4, 9]
# add_list [2, 3, 4]


# lambda 定义多参数函数如下
lambda a, b: a + b

# 可以看到 lambda 可以定义一个函数
# 但是 lambda 功能有限, 只能定义单行并且返回数据的函数
# 了解一下即可
