"""
本文件演示下面 5 个知识点

tuple(元组)
set(集合)
列表推导(list comprehension)
字典推导(dict comprehension)
集合推导(set comprehension)

"""



def log(*args, **kwargs):
    print(*args, **kwargs)


# =====
# tuple
# =====
#
# tuple 和 list 几乎是一样的数据结构
# 区别在于 tuple 一旦赋值就不能往里面插入新元素也不能删除元素
# 你可以把 tuple 看做不能修改的 list

# tuple 和 list 的表示方法的区别在于, 一个用括号 () 一个用中括号 []
# t 是一个 tuple, 你对它进行修改操作是会报错的
t = (1, 2, 3)




# =====
# set
# =====
#
# set 是一个类似于 list 的数据结构, 只简单介绍, 不作过多要求
# 区别在于 set 中添加的元素是不会重复的
# 具体我们在下面的例子中查看

# 初始化一个 set 赋值给 s, s 中现在有 4 个值
s = {1, 2, 3, 3}

log(s)
# 输出如下, 你会发现只有一个 3, 因为 set 中的元素是不会重复的, 所以它丢掉了重复的多与数据
# {1, 2, 3}


# set 有 add remove 两个方法分别用于添加元素和删除元素
# 可以用 in 语法判断一个元素是否在 set 中
s.add('gua')
log('add', s)

s.remove(1)
log('remove, s')

log('in', 1 in s, 2 in s)






# =====
# 列表推导
# =====
#
# 这是在 python 中被广泛使用的一个语法, 其他主流语言中没有这个语法, 很独特
# 在之前的 process 函数中, 我们处理一个 list 并且添加进一个新的 list
#

array = [1, 2, 3, 4, 5]
# 把 array 里面每个元素都加上 100 并生成一个新的 list 的步骤如下
# 先创建一个新的 list
l = []
# 遍历老 list
for n in array:
    # 处理元素后添加进新的 list
    l.append(n + 100)


# 使用列表推导, 可以简化代码, 请注意看这个写法, 多抄抄多看看就记住了
# 方式如下
numbers = [n + 100 for n in array]

log('+100 list', l)
log('+100 numbers', numbers)

# 输出如下
# +100 list [101, 102, 103, 104, 105]
# +100 numbers [101, 102, 103, 104, 105]






# 列表推导可以使用 if 过滤数据
# 现在只要偶数不要奇数
#
# 老办法如下
l = []
# 遍历老 list
for n in array:
    # 处理元素后添加进新的 list
    if n % 2 == 0:
        l.append(n + 100)


# 使用列表推导, 可以简化代码
# 方式如下
numbers = [n + 100 for n in array if n % 2 == 0]

log('+100 filter list', l)
log('+100 filter numbers', numbers)

# 输出如下
# +100 filter list [102, 104]
# +100 filter numbers [102, 104]





# =====
# 字典推导(dict comprehension)
# 集合推导(set comprehension)
# =====
#
# 这两种用法性质和 列表推导 相似, 区别很小
# 也有 if 过滤的语法, 但这里不作演示了

# 字典推导
# 请观察输出来总结这个语法
d = {str(i) + '的平方' : i * i for i in range(3)}
log('字典推导', d)


# 集合推导
# 区别在于中括号 [] 换成了大括号 {}
s = {i for i in range(3)}
log('集合推导', s)