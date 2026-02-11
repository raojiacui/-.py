#例子1
# def is_even(n):
#     if n%2==0:
#         return True
#     else:
#         return False
    

# print(is_even(1))
# print(is_even(2))
# print(is_even(3))
# print(is_even(4))

#例子2
# def max(a,b):
#     if a>b:
#         return True
#     else:
#         return False
    
# print(max(3,4))
# print(max(100,99))
from pixfog import*
import math
def left(a):
     turtle.left(a)
def sin(degree):
    radians = degree * math.pi / 180
    return math.sin(radians)
def cos(degree):
    radians = degree * math.pi / 180
    return math.cos(radians)





# 作业 1
# 实现一个圆形函数
# x y 是圆形的圆心
# r 是半径
#circle(x, y, r)
def circle(x, y,r):
     jump(x,y)
     j = (2 * math.pi * r) / 36
     left(95)
     forward(r)
     right(95)
     degree = 360 / 36
     i = 0
     while i < 36:
         forward(j)
         right(10)
         i = i + 1
# circle(0,0,90)
# pause()

# 作业 2
# 实现一个矩形函数
# x y 是矩形中心的坐标
# w h 是宽高
# center_rect(x, y, w, h)
# def center_rect(x,y,w,h):
#      x1=x+w/2
#      y1=y+h/2
#      rect(x1,y1,w,h)
def rect(x,y,w,h):
     jump(x,y)
     i = 0
     while i < 2:
         forward(w)
         right(90)
         forward(h)
         right(90)
         i = i + 1
# center_rect(-300,0,300,200)
# pause()

# 作业 3
# 实现一个正五角星(国旗大星星那种)函数
# x y 是五角星顶部横边的左边点坐标
# length 是一条线的长度
# 这是一个正五角星
#vgwujcxy(x, y, length)
def vgwujcxy(x,y,len):
      i=0
      while i<5:
           forward(len)
           right(144)
           i=i+1
#vgwujcxy(0,0,100)
# pause()

# 作业 4
# 实现一个函数画日本国旗
# 调用 2 个函数画日本国旗
# 一个画背景的白色矩形
# 一个画中间的红色圆
# japan()
作业1,2一起运行
def japan():
 japan()  
pause()

# 作业 5
# 实现一个五角星函数
# x y 是五角星的中心点坐标
# r 是五角星外接圆的半径
# wujcxy(x, y, r)
#调用作业 3 的函数 vgwujcxy(x1, y1, length)
#和作业3一起运行
def wujcxy(x,y,r):
     left(162)
     forward(r)
     right(162)
     x1 = x - cos(18) * r
     y1 = y + sin(18) * r
     len = cos(18) * r * 2
     vgwujcxy(x1,y1,len)
wujcxy(0,0,100)
pause()

# 作业 6
# 实现一个函数画中国国旗(以下国旗题目都是如此 不重复了)
# 调用 2 个函数画中国国旗
# 一个画红色背景
# 另一个画五角星（函数里调用 5 次，不要求角度朝向，不要求尺寸, 只要 5 个五角星即可）
# 当然你也可以使用第 5 题 wujcxy 这个函数画出比较完美的国旗 (不过这不是学习的重点)
# China()
#作业2，3一起运行的
def China():
     j=0
     while j<5:
          jump(j*100,0)
          vgwujcxy(j*100,0,50)
          j=j+1
China()
rect(0,0,300,200)
pause()


# 作业 7
# 实现一个函数画法国国旗
# France()
#和作业2一起运行的
def France():
    w=300
    h=200
    w1=w/3
    x1=-w/2
    x2=-w/2+w1
    x3=-w/2+w1*2
    y1=h/2
    rect(x1,y1,w1,h)
    rect(x2,y1,w1,h)
    rect(x3,y1,w1,h)
France()
pause() 

# 作业 8
# 画德国国旗
# Germany()
#和作业2一起运行的
def Germany():
    w=400
    h=300
    h1=h/3
    y1=h/2
    y2=h/2-h1
    y3=h/2-h1*2
    x1=-w/2
    rect(x1,y1,w,h1)
    rect(x1,y2,w,h1)
    rect(x1,y3,w,h1)
Germany()
pause()
        
# 作业 9
# 画冈比亚国旗
# gambia()
#和作业2一起运行的
def gambia():
    w=400
    h=300
    h1=h/3
    h2=h/24
    h3=h/4
    y1=h/3
    y2=-h/3
    y3=h/48*7
    y4=-h/48*7
    center_rect(0,y1,w,h1)
    center_rect(0,y3,w,h2)
    center_rect(0,0,w,h3)
    center_rect(0,y4,w,h2)
    center_rect(0,y2,w,h1)
gambia()
pause()

# 作业 10
# 画 瑞士国旗
# switzerland()
#和作业2一起运行的
def switZerland():
     w=75
     h=25
     x1=x-w/2 在作业2中定义的
     y1=y+h/2       1
     x2=x+w/2       1
     y2=y-h/2 在作业2中定义的
     center_rect(0,0,w,h)
     center_rect(0,0,h,w)
     center_rect(0,0,300,300)
switZerland()
pause()
     
# 作业 11
# 画朝鲜国旗
# northkorea()
def northkorea():
     w=400
     h=300
     x1=-w/2
     x2=-w/8
     r=h/5
     y1=h/2
     y2=17/50*h
     y3=3/10*h
     y4=-3/10*h
     y5=-17/50*h
     h1=4/25*h
     h2=1/25*h
     h3=3/5*h
     rect(x1,y1,w,h1)
     rect(x1,y2,w,h2)
     rect(x1,y3,w,h3)
     rect(x1,y4,w,h2)
     rect(x1,y5,w,h1)
     circle(x2,0,r)
     wujcxy(x2,0,25)
northkorea()
pause()


# ============= 格式化错误梳理 =============
# 根据板书2的代码格式化规则检查

# 规则3: 运算符的左右各加一个空格
# 第 63 行: x1=x+w/2  →  应该 x1 = x + w / 2
# 第 64 行: y1=y+h/2  →  应该 y1 = y + h / 2
# 第 86 行: i=0  →  应该 i = 0
# 第 87 行: i<5  →  应该 i < 5
# 第 89 行: i=i+1  →  应该 i = i + 1
# 第 114 行: r=h/5  →  应该 r = h / 5
# 第 132 行: j=0  →  应该 j = 0
# 第 133 行: j<5  →  应该 j < 5
# 第 135 行: j=j+1  →  应该 j = j + 1
# 第 167 行: h1=h/3  →  应该 h1 = h / 3
# 第 168 行: y1=h/2  →  应该 y1 = h / 2
# 第 169 行: y2=h/2-h1  →  应该 y2 = h / 2 - h1
# 第 170 行: y3=h/2-h1*2  →  应该 y3 = h / 2 - h1 * 2
# 第 171 行: x1=-w/2  →  应该 x1 = -w / 2
# 第 183-190 行: 多处赋值语句缺少空格

# 规则4: 逗号前无空格，后面 1 个空格
# 第 23 行: import*  →  应该 import *
# 第 43 行: def circle(x, y,r):  →  应该 def circle(x, y, r):
# 第 44 行: jump(x,y)  →  应该 jump(x, y)
# 第 63 行: def center_rect(x,y,w,h):  →  应该 def center_rect(x, y, w, h)
# 第 67 行: def rect(x,y,w,h):  →  应该 def rect(x, y, w, h)
# 第 68 行: jump(x,y)  →  应该 jump(x, y)
# 第 85 行: def vgwujcxy(x,y,len):  →  应该 def vgwujcxy(x, y, length):
# 第 112 行: def wujcxy(x,y,r):  →  应该 def wujcxy(x, y, r):
# 第 119 行: vgwujcxy(x1,y1,len)  →  应该 vgwujcxy(x1, y1, length)
# 第 134 行: jump(j*100,0)  →  应该 jump(j * 100, 0)
# 第 135 行: vgwujcxy(j*100,0,50)  →  应该 vgwujcxy(j * 100, 0, 50)
# 第 138 行: rect(0,0,300,200)  →  应该 rect(0, 0, 300, 200)
# 第 152-156 行: 函数调用中逗号后缺少空格

# 规则2: 函数之间空两行
# 第 26 行: left() 和 sin() 之间只空了1行（应该空2行）
# 第 29-30 行: sin() 和 cos() 之间只空了1行（应该空2行）
# 第 56 行: circle() 和 rect() 之间应该空2行
# 第 76 行: rect() 和 vgwujcxy() 之间应该空2行
# 第 92 行: vgwujcxy() 和 japan() 之间应该空2行
# 第 121 行: wujcxy() 调用和 China() 之间应该空2行
# 第 139-142 行: China() 和 France() 之间应该空2行
# 第 158-160 行: France() 和 Germany() 之间应该空2行
# 第 176-178 行: Germany() 和 gambia() 之间应该空2行
# 第 198-200 行: gambia() 和 switZerland() 之间应该空2行
# 第 215-217 行: switZerland() 和 northkorea() 之间应该空2行

# 规则1: 每行只写一条语句
# 第 207-210 行: 注释混在代码中，导致语法错误
#   "x1=x-w/2 在作业2中定义的"  →  应该 # x1=x-w/2 在作业2中定义的
#   "y1=y+h/2       1"  →  应该 # y1=y+h/2

# 规则7: 函数、列表左括号前无空格，所有右括号前无空格
# 第 23 行: import*  →  应该 import * (右括号前无空格)


