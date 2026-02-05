# Python Turtle 绘图练习

这是一个使用 Python `turtle` 库学习图形绘图的练习项目。

## 项目文件

| 文件 | 描述 |
|------|------|
| `import turtle.py` | 使用函数封装画正方形的代码 |
| `py` | 基础画正方形示例 |
| `预习 1请用vscode打开.py` | 使用 `from turtle import *` 的画正方形示例 |

## 运行方式

确保已安装 Python，然后在命令行运行：

```bash
python "import turtle.py"
```

或运行其他文件：

```bash
python py
python "预习 1请用vscode打开.py"
```

## 代码示例

```python
import turtle

t = turtle.Turtle()

def square(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

    for _ in range(4):
        t.forward(100)
        t.right(90)

square(0, 0)
turtle.done()
```

## 学习内容

- `turtle` 库的基本使用
- 画笔控制 (`penup`, `pendown`)
- 移动和转向 (`forward`, `right`)
- 函数封装与复用
