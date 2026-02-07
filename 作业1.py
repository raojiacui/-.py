# from pixfog import*
# def square(x,y):
#     jump(x,y)
#     i=0
#     while i < 4:
#         forward(100)
#         right(90)
#         i=i+1
# square(0,0)
# pause()

# 1
# 实现函数, 用于画一个正方形, 边长由参数提供
# 参数 x, y 是正方形左上角坐标
# 参数 l(注意，这里是字母 l，不是数字 1) 是正方行边长
# 函数声明如下
# square(x, y, l)
from pixfog import*
def square(x,y,i):
     jump(x,y)
     j=0
     while j <4:
         forward(i)
         right(90)
         j=j+1
square(0,0,100)
pause()

# 2
# 实现函数, 用于画一个矩形, 长宽由参数提供
# 参数 x, y 是左上角坐标
# 参数 w, h 是长宽
# 函数声明如下
# rect(x, y, w, h)
# from pixfog import*
# def rect(x,y,w,h):
#     jump(x,y)
#     i=0
#     while i<2:
#         forward(w)
#         right(90)
#         forward(h)
#         right(90)
#         i=i+1
# rect(0,0,200,100)
# pause()

# 3
# 画一排正方形, 一共 5 个
# 从 0 0 点开始(, 边长为 30, 正方形之间间隔为 0
# 函数声明如下
# square5()
from pixfog import*
def square5(x,y,i):
     jump(x,y)
     i=0
     while i<5:
         j=0
         while j<4:
          forward(30)
          right(90)
          j=j+1
     jump(x+30*i,y)
     i=i+1
square5(0,0,5)
pause()

# 4
# 画一排正方形, 一共 5 个
# 从 0 0 点开始, 边长为 30, 正方形之间间隔为 10 像素
# 函数声明如下
# square5_10()
# from pixfog import*
# def square5_10(x,y,n,space,len):
#     jump(x,y)
#     i=0
#     while i<5:
#         j=0
#         while j<4:
#             forward(30)
#             right(90)
#             j=j+1
#         jump(x+(len+space)*(i+1),y)    
#         i=i+1
# square5_10(0,0,5,10,30)
# pause()

# 5
# 实现函数, 画一排正方形, 有如下参数
# x, y 是第一个正方形左上角坐标
# n 是正方形的个数
# space 是两个正方形之间的间距
# len 是正方形的边长
# square_line(x, y, n, space, len)
# from pixfog import*
# def square_line(x,y,space,len):
#     jump(0,0)
#     i=0
#     while True:
#         j=0
#         while j<4:
#             forward(len)
#             right(90)
#             j=j+1
#         jump(x+(len+space)*(i+1),y)
#         i=i+1
# square_line(0,0,10,100)
# pause()

# 6
# 实现函数, 用上题的函数来画一个正方形方阵, 参数如下
# x, y 是第一个正方形左上角坐标
# space 是两个正方形之间的间距
# len 是正方形的边长
# n 是横向正方形的个数
# m 是纵向正方形的个数
# square_square(x, y, space, len, n, m)
# from pixfog import*
# def square_line(x,y,space,len):
#      n=0
#      while True:
#          m=0
#          while True:
#              jump(x+(len+space)*n,y+(len+space)*m)
#              j=0
#              while j<4:
#                  forward(30)
#                  right(90)
#                  j=j+1
#              m=m+1
#              n=n+1
         
# square_line(0,0,10,30)
# pause()

# 7
# 实现函数, 画一排矩形, 有如下参数
# x, y 是第一个矩形左上角坐标
# w, h 是矩形长宽
# n 是矩形的个数
# space 是两个矩形之间的间距
# rect_line(x, y, w, h, n, space)
# from pixfog import*
# def rect_line(x,y,w,h,space):
#     jump(0,0)
#     i=0
#     while True:
#         j=0
#         while j<4:
#             forward(w)
#             right(90)
#             forward(h)
#             right(90)
#             j=j+1
#         jump(x+(w+space)*(i+1),y)
#         i=i+1
# rect_line(0,0,100,50,10)
# pause()

# 8
# 实现函数, 画一个矩形方阵, 参数如下
# x, y 是第一个矩形左上角坐标
# space 是两个矩形之间的间距(横向和纵向)
# w, h 是矩形的长宽
# n 是横向矩形的个数
# m 是纵向矩形的个数
# rect_square(x, y, space, w, h, n, m)
# from pixfog import*
# def rect_line(x,y,w,h,space):
#      jump(0,0)
#      i=0
#      n=0
#      while True:
#          m=0
#          while True:
#              j=0
#              while j<4:
#               forward(w)
#               right(90)
#               forward(h)
#               right(90)
#               j=j+1
#              jump(x+(w+space)*(i+1),y+(h+space*(i+1)))
#              m=m+1
#              n=n+1
#              i=i+1
# rect_line(0,0,100,50,10)
# pause()

# 9
# 实现函数, 画一个正多边形, 参数如下
# x y 是起点, 设起点为多边形的顶部边的左顶点
# n 是多边形的边数
# l 是边长
# polygon(x, y, n, l)
# from pixfog import*
# def polygon(x,y,i):
#     jump(0,0)
#     nzjc = (n - 2) * 180 / n
#     degree = 180 - nzjc
#     i=0
#     n=0
#     while i<n:
#         forward(i)
#         right(degree)
#         i=i+1
#     n=n+1
# polygon(0,0,100)
# pause()



    




