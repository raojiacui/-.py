def log(*args, **kwargs):
    print(*args, **kwargs)


# 例子 1
# 求数组的和
def sum(array):
    # 先设置一个变量用来存数组的和
    s = 0
    for i in range(len(array)):
        # 用变量 n 保存元素的值
        n = array[i]
        # 累加到变量 s
        s = s + n
    # 循环结束, 现在 s 里面存的是数组中所有元素的和了
    return s



# 作业 2
# 返回一个数的绝对值
# 函数定义是
def abs(n):
    if n <0:
        n = -n
    return n


# 作业 3
# 参数是一个只包含数字的 array
# 求 array 中所有数字的平均数
# 函数定义是
#average(array)
def average(array):
    log('求 array 长度', len(array))
    length = len(array)
    # log(length)
    average = sum(array) / len(array)
    return average


# 作业 4
# 参数是一个只包含数字的 array
# 求 array 中最小的数字
# 函数定义是
def min(array):
    s=array[0]
    for i in range(len(array)):
        n = array[i]
        if n < s:
            s = n
    return s
    

# 作业 5
# 参数是一个数字 n
# 返回以下序列的结果
# 1 - 2 + 3 - 4 + 5 ... n
# sum1(n)
def sum1(n):
    s=0
    for i in range(1, n + 1):
        if i % 2 == 0:
            s = s - i
        else:
            s = s + i
    return s


# 作业 6
# 参数是一个数字 n
# 返回以下序列的结果
# 1 + 2 - 3 + 4 - ... n
# sum2(n)
def sum2(n):
    s = 1
    for i in range(2,n + 1):
        if i % 2 == 0:
            s = s + i
        else:
            s = s - i
    return s


# 作业 7
# 实现 fac 函数
# 接受一个参数 n
# 返回 n 的阶乘, 1 * 2 * 3 * ... * n
# fac(n)
def fac(n):
    s = 1
    for i in range(1, n + 1):
        s = s * i
    return s


# 作业 8
# 实现 apply 函数
# 参数如下
# op 是 string 类型, 值是 '+' '-' '*' '/' 其中之一
# a b 分别是 2 个数字
# 根据 op 对 a b 运算并返回结果(加减乘除)

# 这里提供部分代码作为你的参考
def apply(op, a, b):
    if op == '-':
        return a - b
    if op == '*':
        return a * b
    if op == '/':
        return a / b
    if op == '+':
        return a + b


# 作业 9
# 实现 apply_list 函数
# op 是 '+' '-' '*' '/' 其中之一
# oprands 是一个只包含数字的 list(数组)
# 根据 op 对 oprands 中的元素进行运算并返回结果
# 例如, 下面的调用返回 -4
# n = apply_list('-', [3, 4, 2, 1])
# log(n)
# 结果是 -4, 用第一个数字减去所有的数字
def apply_list(op, oprands):
    s = oprands[0]
    for i in range(1, len(oprands)):
        b = oprands[i]
        s = apply(op, s, b)
    return s


# 作业 10
# 实现 apply_compare 函数
# 参数如下
# expression 是一个 array(数组), 包含了 3 个元素
# 第一个元素是 op, 值是 '>' '<' '==' 其中之一
# 剩下两个元素分别是 2 个数字
# 根据 op 对数字运算并返回结果(结果是 True 或者 False)
def apply_compare(expression):
    op = expression[0]
    a = expression[1]
    b = expression[2]
    if op == '>':
        return a > b
    if op == '<':
        return a < b
    if op == '==':
        return a == b


# 作业 11
# 实现 apply_ops 函数
# 参数如下
# expression 是一个 array
# expression 中第一个元素是上面几题的 op, 剩下的元素是和 op 对应的值
# 根据 expression 运算并返回结果
# 假设 expression 为 ['+', 1, 3, 5, 7]
# 1 + 3 + 5 + 7 = 16
# 那么返回的结果为 16
def apply_ops(expression):
    op = expression[0]
    if op == '>' or op == '<' or op =='==':
        a = expression[1]
        b = expression[2]
        return apply_compare(op, a, b)
    else:
        oprands = expression[1:]
        return apply_list(op, oprands)


# 作业 12
# 根据本周天气，绘制柱状图
# temps 保存了中国本周的每日平均气温, 从周一到周日一共 7 个数字
# 柱壮图里每个图宽 30，间距为 0
# 温度数字每摄氏度的高度由参数 unit_len 决定，默认是 8
from pixfog import* 
def rect_1b(x, y, w, h):
    jump(x, y)
    i=0
    while i < 4:
        if i % 2 == 0:
            forward(w)
        else:
            forward(h)
        right(90)
        i = i + 1


def forecast(temps, unit_len = 8):
    i=0
    while i < len(temps):
        temp = temps[i]
        x = i * 30
        y = 0
        w = 30
        h = temp * unit_len
        rect_1b(x,0,30,h)
        i = i + 1

    
# ==================== 测试代码 ====================

# 取消注释来测试各个函数


# log(abs(-3))
# log(abs(3))


log(average([1, 3, 5]))


#log(min([20, 5, 10]))


#log(sum1(5))


#log(sum1(5))


#log(fac(5))


# log(apply('-', 6, 2))
# log(apply('*', 6, 2))
# log(apply('/', 6, 2))


#log(apply_list('-', [3, 4, 2, 1]))


#log(apply_compare(['>', 4, 3]))


#log(apply_ops(['+', 1, 3, 5, 7]))


# temps = [22, 19, 22, 25, 27, 30, 28]
# forecast(temps, unit_len=8)
# pause()