# 作业 1 参考答案
# 复用思想：后面的函数调用前面已实现的函数

from pixfog import *

# ==================== 基础函数 ====================

# 1. 画一个正方形
# 参数 x, y 是正方形左上角坐标
# 参数 l 是正方形边长
def square(x, y, l):
    jump(x, y)
    i = 0
    while i < 4:
        forward(l)
        right(90)
        i = i + 1


# 2. 画一个矩形
# 参数 x, y 是左上角坐标
# 参数 w, h 是长宽
def rect(x, y, w, h):
    jump(x, y)
    i = 0
    while i < 2:
        forward(w)
        right(90)
        forward(h)
        right(90)
        i = i + 1


# ==================== 一排正方形 ====================

# 3. 画一排正方形，一共 5 个
# 从 (0,0) 开始，边长为 30，正方形之间间隔为 0
# 写法一：直接调用 square()，简洁版
def square5():
    square(0, 0, 30)
    square(30, 0, 30)
    square(60, 0, 30)
    square(90, 0, 30)
    square(120, 0, 30)


# 3-写法二：用循环实现（理解用）
def square5_loop():
    i = 0
    while i < 5:
        next_x = i * 30
        next_y = 0
        square(next_x, next_y, 30)
        i = i + 1


# 4. 画一排正方形，一共 5 个
# 从 (0,0) 开始，边长为 30，正方形之间间隔为 10 像素
# 写法一：直接调用 square()
def square5_10():
    square(0, 0, 30)
    square(40, 0, 30)
    square(80, 0, 30)
    square(120, 0, 30)
    square(160, 0, 30)


# 4-写法二：用循环实现（理解用）
def square5_10_loop():
    i = 0
    while i < 5:
        next_x = i * 40
        next_y = 0
        square(next_x, next_y, 30)
        i = i + 1


# 5. 画一排正方形（通用版本）
# 参数 x, y 是第一个正方形左上角坐标
# 参数 n 是正方形的个数
# 参数 space 是两个正方形之间的间距
# 参数 len 是正方形的边长
def square_line(x, y, n, space, len):
    i = 0
    while i < n:
        next_x = x + i * (len + space)
        next_y = y
        square(next_x, next_y, len)
        i = i + 1


# ==================== 正方形方阵 ====================

# 6. 画一个正方形方阵
# 参数 x, y 是第一个正方形左上角坐标
# 参数 space 是两个正方形之间的间距
# 参数 len 是正方形的边长
# 参数 n 是横向正方形的个数
# 参数 m 是纵向正方形的个数
# 复用 square_line() 实现
def square_square(x, y, space, len, n, m):
    row = 0
    while row < m:
        next_y = y + row * (len + space)
        square_line(x, next_y, n, space, len)
        row = row + 1


# ==================== 一排矩形 ====================

# 7. 画一排矩形（通用版本）
# 参数 x, y 是第一个矩形左上角坐标
# 参数 w, h 是矩形长宽
# 参数 n 是矩形的个数
# 参数 space 是两个矩形之间的间距
def rect_line(x, y, w, h, n, space):
    i = 0
    while i < n:
        next_x = x + i * (w + space)
        next_y = y
        rect(next_x, next_y, w, h)
        i = i + 1


# ==================== 矩形方阵 ====================

# 8. 画一个矩形方阵
# 参数 x, y 是第一个矩形左上角坐标
# 参数 space 是两个矩形之间的间距（横向和纵向）
# 参数 w, h 是矩形的长宽
# 参数 n 是横向矩形的个数
# 参数 m 是纵向矩形的个数
# 复用 rect_line() 实现
def rect_square(x, y, space, w, h, n, m):
    row = 0
    while row < m:
        next_y = y + row * (h + space)
        rect_line(x, next_y, w, h, n, space)
        row = row + 1


# ==================== 正多边形 ====================

# 9. 画一个正多边形
# 参数 x, y 是起点（多边形顶部边的左顶点）
# 参数 n 是多边形的边数
# 参数 l 是边长
def polygon(x, y, n, l):
    jump(x, y)
    degree = 360 / n
    i = 0
    while i < n:
        forward(l)
        right(degree)
        i = i + 1


# ==================== 测试代码 ====================

# 取消注释来测试各个函数

# 测试第1题 - 正方形
# square(0, 0, 100)
# pause()

# 测试第2题 - 矩形
# rect(0, 0, 200, 100)
# pause()

# 测试第3题 - 一排5个正方形（间隔0）
# square5()
# pause()

# 测试第4题 - 一排5个正方形（间隔10）
# square5_10()
# pause()

# 测试第5题 - 一排n个正方形
# square_line(0, 0, 5, 10, 30)
# pause()

# 测试第6题 - 正方形方阵
# square_square(0, 0, 10, 30, 4, 4)
# pause()

# 测试第7题 - 一排矩形
# rect_line(0, 0, 100, 50, 3, 20)
# pause()

# 测试第8题 - 矩形方阵
# rect_square(0, 0, 10, 100, 50, 3, 3)
# pause()

# 测试第9题 - 正多边形
# polygon(0, 0, 6, 100)  # 正六边形
# pause()
