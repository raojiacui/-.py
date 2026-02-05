from gua import *


# 第 3 课的上课内容

# 作业 2 讲解
# debug（调试/除错）的标准应对流程（最重要的内容）
# array 和 string

# 预习内容是
# 内置数据结构 array（数组）
# for 循环(和 while 循环功能一样, 但某些场景下更方便)
# 字符串和常用字符串操作


# 这里用一种特殊的方式创造了一个 log 函数
# 下面就可以用 log 替代 print 了, 用 log 的原因在于统一/方便/灵活(具体以后你会学到)
# 以后会学这个的原理, 现在直接拿来用即可
# 注意, 我们以后用这个 log 替代 print


def log(*args, **kwargs):
    print(*args, **kwargs)


# debug
# 常见的 2 种错误
# 1. 语法错误，程序没有运行
# 2. 逻辑错误，程序运行，但是结果不是想要的


# 调试的 2 个难点
# 1. 程序运行的分支你不知道，要让它显形
# 2. 程序的运行状态（变量的值）你不知道，要看到它


# print('gua')
# print('hahah', gua)


# def japan():
#     # ...
#     forward(100)

# debug 流程演示
# log('japan start')
#
#
# def japan(l):
#     # ...
#     log('japan l', l)
#     forward(1)
#
#
# log('japan end')
#
#
# japan(100)
# japan(13)
#
# log('japan run')
#
#
# pause()


# log 的两个作用：
# 1. 把程序运行的路径显示出来
# 2. 把变量显示出来


# ;   希腊问号（GREEK QUESTION MARK）
# ;   分号


# ord 可以获取代表字符的数字
log('希腊问号', ord(';'))
log('分号', ord(';'))

# 通过 log 找错误的方式，一共两点：
# 1. 看是否被调用了
# 2. 看这个值是不是想要的值


# array 可以干嘛？
# array 可以存储很多元素，每个元素的值、类型都可以不同
# 具体看下面的例子
#
# array（数组）常用操作
# 创建数组
# 使用 [] 符号，每个元素用逗号分隔
a = [1, 3, 4, 5]
# # 现在 a 是一个 array，拥有 4 个元素
#
#
# 可以用内置的 len 函数得到 array 的长度
log('求 array 长度', len(a))
# 使用 len(a) 可以求出数组的长度（数组中元素的个数）
# 值可以用变量接住
length = len(a)
log(length)

# 访问元素
# 对于数组中的每个元素，可以通过下标（就是元素在数组中的序号，从 0 开始）访问
# 下标访问语法是 [] 中括号
log('用下标访问 array 中的元素')
log(a[0])
log(a[1])
log(a[2])
log(a[3])
# 因为一共只有 4 个元素，所以访问不存在的下标会出错
# log(a[4])

# 手动访问元素当然是低效的
# 可以用循环来访问元素，这个过程叫 遍历
# 注意，这里我们引入了一个新的语法，for 循环
# 具体上课会解释
log('循环访问 array 所有元素')
length = len(a)
for i in range(length):
    log(a[i])
# i 分别是 0 1 2 3


# 上面的循环等价于下面的 while
i = 0
length = len(a)
while i < length:
    log('while', a[i])
    i = i + 1

# 向已经存在的 array 中添加新元素
# 可以用数组的 append 函数往列表末尾插入一个元素
# 并且，这个新元素可以是任意类型，这里是一个字符串
# 请注意, 这是一个全新的概念, 数组类型的变量可以用 .函数 的方式来进行操作
a.append('新元素')
log(a)
# [1, 3, 4, 5, '新元素']
a.append(0)
log(a)
# [1, 3, 4, 5, '新元素', 0]
# 多添加几个元素
a.append(12)
a.append(23)
a.append(34)
log(a)

# 题目，给定一个只包含数字的 array
# 题目，得到列表中最小的元素
# 题目，得到列表中所有数字的和
# 题目，得到列表中所有数字的平均数
# 题目，len(array) 可以得到 array 长度（也就是元素个数），上文有写


# 这是一段获取数组中最小元素的代码
a = [3, 9, 2, 0, 8]
min_number = a[0]

for i in range(len(a)):
    n = a[i]
    if n < min_number:
        min_number = n

log('min_number', min_number)

# sum = 0
# for i in range(len(a)):
#     n = a[i]
#     sum = sum + n


# 字符串
# 字符串的操作
# 字符串可以判断相等、判断是否包含、相加、取子字符串
# 例子
# 判断相等或者包含
log('good' == 'good')
log('good' == 'bar')
log('good' != 'bad')
log('possible' in 'impossible')

# 拼接得到一个新字符串
log('very' + 'good')
log('very ' + 'good')

name = 'gua'
greeting = 'hello,' + name
log(greeting)

# 得到一个你想要的字符串有多种方式
# 但是现在有现代的方式, 字符串的 format 函数
# 注意，书上如果和我不一样，以我为准(如果你看过书或者自学过其他教程你会知道百分号格式化字符串, 那是过时的用法了)
# 用法如下
name = 'gua'
name2 = 'gua2'
a = '#{}，{}#, 你好'.format(name, name2)
log(a)
# 简单说来，就是 {} 会被变量替换形成新字符串
# 可以有多个参数, 按顺序替换字符串中的 {}


# 字符串相当于一个 array，可以用下标访问
# 看例子，看结果
# s 的长度是 7，但是下标是从 0 开始的，所以最大下标是 6
s = 'iamgood'
log(s[0])
log(s[1])
log(s[2])
# ...
log(s[6])
#
# 当然也就可以和 array 一样用循环遍历了
# 自己试试


# 字符串不能使用下标来赋值
# 只能拼接起来生成一个新的字符串
name = 'gua'

# name[0] 是 'g'
# 假如你进行如下操作 name[0] = 'A'
# 会产生一个错误, 因为字符串不能这样操作


# 字符串可以切片，当然 array 也可以这样切片
# 语法如下
# s[开始下标:结束下标]
s[0:3]  # 'iam'
s[1:3]  # 'am'

# 省略开始下标参数意思是从 0 开始取
s[:3]  # 'iam'

# 省略结束下标参数意思是取到底
s[2:]  # 'mgood'

s1 = 'iamgood'[3:]
log(s1)

# 变量作用域
# def center_rect():
#     x = 1
#     ...
#
#
# def rect():
#     x = 100
#     y = 100
#     ...
