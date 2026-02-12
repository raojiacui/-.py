# 作业 3 参考答案
# 复用思想：后面的函数调用前面已实现的函数

from pixfog import *


# ==================== 辅助函数 ====================

# log 函数用于调试输出
# 上课会讲这个原理，现在直接拿来用即可
def log(*args, **kwargs):
    print(*args, **kwargs)


# ==================== 基础函数 ====================

# 例子 1
# 求数组的和
# 参数 array 是一个只包含数字的数组
# 返回数组中所有元素的和
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


# ==================== 作业 2: 绝对值函数 ====================

# 作业 2
# 返回一个数的绝对值
# 参数 n 是一个数字
# 返回 n 的绝对值
def abs(n):
    # 如果 n 小于 0，就把 n 的值赋值成 -n
    if n < 0:
        n = -n
    # 返回 n 的值（很重要，一定要 return n）
    return n


# ==================== 作业 3: 平均数函数 ====================

# 作业 3
# 参数是一个只包含数字的 array
# 求 array 中所有数字的平均数
def average(array):
    # 使用例子 1 中的 sum 函数来计算数组中所有元素的总和
    total = sum(array)
    # 使用 len 函数计算出数组中元素的个数
    length = len(array)
    # 使用数组中元素的总和除以数组中元素的个数，得到平均数
    result = total / length
    # 返回平均数
    return result


# ==================== 作业 4: 最小值函数 ====================

# 作业 4
# 参数是一个只包含数字的 array
# 求 array 中最小的数字
def min(array):
    # 将数组中第一个元素的值赋值给 s 作为初始值
    s = array[0]
    # 遍历数组，用变量 n 保存元素的值
    for i in range(len(array)):
        n = array[i]
        # 比较 n 与 s 的值，如果 n < s，就把 n 的值赋值给 s
        if n < s:
            s = n
    # 循环结束后，变量 s 里面存的是数组中最小的数字
    # 返回变量 s（很重要，一定要 return s）
    return s


# ==================== 作业 5: 序列求和 1 ====================

# 作业 5
# 参数是一个数字 n
# 返回以下序列的结果: 1 - 2 + 3 - 4 + 5 ... n
def sum1(n):
    # 先设置一个变量 s 用来存序列的和，初始值为 0
    s = 0
    # 循环 n 次，从 1 开始，到 n + 1 结束，即包括 n 但是不包括 n + 1
    for i in range(1, n + 1):
        # 判断每次循环的值
        # 如果是奇数，累加这个数到 s 上
        if i % 2 == 1:
            s = s + i
        # 如果是偶数，累减这个数到 s 上
        else:
            s = s - i
    # 循环结束后，变量 s 里面存的是序列的和
    # 返回变量 s（很重要，一定要 return s）
    return s


# ==================== 作业 6: 序列求和 2 ====================

# 作业 6
# 参数是一个数字 n
# 返回以下序列的结果: 1 + 2 - 3 + 4 - ... n
def sum2(n):
    # 先设置一个变量 s 用来存序列的和，初始值为 1
    # 这样就可以从 2 开始计算循环了
    s = 1
    # 循环 n - 1 次，从 2 开始，到 n 结束（包括 n）
    for i in range(2, n + 1):
        # 判断每次循环的值
        # 从 2 开始之后，当一个数字是奇数时（3 5 7...），就是减去这个数
        if i % 2 == 1:
            s = s - i
        # 当一个数字是偶数时（2 4 6 8...），就是加上这个数
        else:
            s = s + i
    # 循环结束后，变量 s 里面存的是序列的和
    # 返回变量 s（很重要，一定要 return s）
    return s


# ==================== 作业 7: 阶乘函数 ====================

# 作业 7
# 实现阶乘函数
# 接受一个参数 n
# 返回 n 的阶乘, 1 * 2 * 3 * ... * n
def fac(n):
    # 先设置一个变量 s 用来存阶乘，初始值为 1
    s = 1
    # 用循环把 1 到 n 的数字相乘保存到 s 中
    for i in range(1, n + 1):
        s = s * i
    # 循环结束后，变量 s 里面存的是从 1 到 n 的阶乘
    # 返回变量 s（很重要，一定要 return s）
    return s


# ==================== 作业 8: 基本运算函数 ====================

# 作业 8
# 实现 apply 函数
# 参数如下:
#   op 是 string 类型, 值是 '+' '-' '*' '/' 其中之一
#   a b 分别是 2 个数字
# 根据 op 对 a b 运算并返回结果(加减乘除)
def apply(op, a, b):
    # 如果 op 是 +，返回 a + b 的结果
    if op == '+':
        return a + b
    # 如果 op 是 -，返回 a - b 的结果
    if op == '-':
        return a - b
    # 如果 op 是 *，返回 a * b 的结果
    if op == '*':
        return a * b
    # 如果 op 是 /，返回 a / b 的结果（不考虑 b 为 0 的情况）
    if op == '/':
        return a / b


# ==================== 作业 9: 列表运算函数 ====================

# 作业 9
# 实现 apply_list 函数
# 参数如下:
#   op 是 '+' '-' '*' '/' 其中之一
#   oprands 是一个只包含数字的 list(数组)
# 根据 op 对 oprands 中的元素进行运算并返回结果
# 例如, 下面的调用返回 -4: apply_list('-', [3, 4, 2, 1])
# 结果是 -4, 用第一个数字减去所有的数字
def apply_list(op, oprands):
    # 先取出 oprands 的第一个元素赋值给 s
    s = oprands[0]
    # 从第二个元素开始遍历数组
    for i in range(1, len(oprands)):
        # 取出当前元素
        b = oprands[i]
        # 调用作业 8 的 apply 函数，并且把得到的结果赋值给 s
        s = apply(op, s, b)
    # 循环结束之后，s 的值就是调用 apply_list 之后的结果
    # 返回 s
    return s


# ==================== 作业 10: 比较运算函数 ====================

# 作业 10
# 实现 apply_compare 函数
# 参数如下:
#   expression 是一个 array(数组), 包含了 3 个元素
#   第一个元素是 op, 值是 '>' '<' '==' 其中之一
#   剩下两个元素分别是 2 个数字
# 根据 op 对数字运算并返回结果(结果是 True 或者 False)
def apply_compare(expression):
    # 取出 expression 的元素，分别赋值给 op、a、b
    op = expression[0]
    a = expression[1]
    b = expression[2]
    # 如果 op 是 '>'，返回 a > b 的值
    if op == '>':
        return a > b
    # 如果 op 是 '<'，返回 a < b 的值
    if op == '<':
        return a < b
    # 如果 op 是 '=='，返回 a == b 的值
    if op == '==':
        return a == b


# ==================== 作业 11: 综合运算函数 ====================

# 作业 11
# 实现 apply_ops 函数
# 参数如下:
#   expression 是一个 array
#   expression 中第一个元素是上面几题的 op, 剩下的元素是和 op 对应的值
# 根据 expression 运算并返回结果
# 假设 expression 为 ['+', 1, 3, 5, 7]
# 1 + 3 + 5 + 7 = 16
# 那么返回的结果为 16
def apply_ops(expression):
    # 先取出 expression 的第一个元素，赋值给 op
    op = expression[0]
    # 如果 op 是 >、<、== 中的一种
    # 这种情况下 expression 只有三个元素
    if op == '>' or op == '<' or op == '==':
        # 取出剩下的两个元素
        a = expression[1]
        b = expression[2]
        # 调用作业 10 的 apply_compare 函数，得到结果之后返回这个结果
        return apply_compare([op, a, b])
    # 如果 op 是 +、-、*、/ 中的一种
    else:
        # 使用数组切片把剩下的数组元素放在 oprands 中
        oprands = expression[1:]
        # 调用作业 9 的 apply_list 函数，得到结果之后返回这个结果
        return apply_list(op, oprands)


# ==================== 作业 12: 柱状图函数 ====================

# 作业 12
# 根据本周天气，绘制柱状图
# temps 保存了中国本周的每日平均气温, 从周一到周日一共 7 个数字
# 柱状图里每个图宽 30，间距为 0
# 温度数字每摄氏度的高度由参数 unit_len 决定，默认是 8

# 辅助函数：画一个以左下角为基准的矩形
# 参数 x, y 是矩形左下角的坐标
# 参数 w, h 是矩形的宽度和高度
def rect_lb(x, y, w, h):
    jump(x, y)
    i = 0
    while i < 2:
        forward(w)
        right(90)
        forward(h)
        right(90)
        i = i + 1


# 主函数：绘制温度柱状图
# 参数 temps 是温度数组
# 参数 unit_len 是每摄氏度对应的高度，默认为 8
def forecast(temps, unit_len=8):
    # 遍历 temps 数组
    for i in range(len(temps)):
        # 获取当前温度
        temp = temps[i]
        # 计算 x 坐标：每个柱子宽 30
        x = i * 30
        # 计算 y 坐标：从 0 开始
        y = 0
        # 计算柱子高度
        h = temp * unit_len
        # 画矩形
        rect_lb(x, y, 30, h)


# ==================== 主程序入口 ====================


def main():
    """
    作业3主函数 - 选择要测试的功能
    取消注释想要测试的内容即可
    """

    # 测试例子 1 - 数组求和
    # log('数组求和:', sum([1, 2, 3, 4, 5]))

    # 测试作业 2 - 绝对值
    # log('绝对值 -3:', abs(-3))
    # log('绝对值 3:', abs(3))

    # 测试作业 3 - 平均数
    # log('平均数:', average([1, 3, 5]))

    # 测试作业 4 - 最小值
    # log('最小值:', min([20, 5, 10]))

    # 测试作业 5 - 序列求和 1
    # log('sum1(5):', sum1(5))  # 1 - 2 + 3 - 4 + 5 = 3

    # 测试作业 6 - 序列求和 2
    # log('sum2(5):', sum2(5))  # 1 + 2 - 3 + 4 - 5 = -1

    # 测试作业 7 - 阶乘
    # log('fac(5):', fac(5))  # 1 * 2 * 3 * 4 * 5 = 120

    # 测试作业 8 - 基本运算
    # log('apply +:', apply('+', 6, 2))
    # log('apply -:', apply('-', 6, 2))
    # log('apply *:', apply('*', 6, 2))
    # log('apply /:', apply('/', 6, 2))

    # 测试作业 9 - 列表运算
    # log('apply_list -4:', apply_list('-', [3, 4, 2, 1]))

    # 测试作业 10 - 比较运算
    # log('apply_compare >:', apply_compare(['>', 4, 3]))
    # log('apply_compare <:', apply_compare(['<', 4, 3]))
    # log('apply_compare ==:', apply_compare(['==', 3, 3]))

    # 测试作业 11 - 综合运算
    # log('apply_ops +:', apply_ops(['+', 1, 3, 5, 7]))
    # log('apply_ops >:', apply_ops(['>', 4, 3]))

    # 测试作业 12 - 柱状图
    # temps = [22, 19, 22, 25, 27, 30, 28]
    # forecast(temps, unit_len=8)
    # pause()


if __name__ == "__main__":
    main()
