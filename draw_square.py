# 使用 pixfog 库绘制图形
# 需要从 pixfog 模块导入具体的函数

from pixfog import forward, right, pause

print("导入成功！开始绘制正方形...")

# 绘制一个正方形 (边长100，转角90度)
forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)

# 绘制完成后暂停，等待用户关闭窗口
pause()
