```

# 本次作业主要是 str
# str 题目用到的知识仍然是
# 0, 用下标引用字符串
# 2, 循环
# 3, 选择 (也就是 if)
# 1, 字符串切片
#
# 请以之前上课中 str 相关的内容作为参考
# 请自行编写测试
#
# *** 注意, 多看提示, 并且有问题要及时在群里发问, 不要做无谓的卡壳


# 定义我们的 log 函数
# 其实更简单的办法是下面这句, 相当于把 print 赋值给 log
log = print


# ======
# 资料
# ======
#
# str 函数可以把数字转成字符串
# 例如 str(1) 就能得到 '1'
#


# 作业 1
#
def zfill(n, width):
    """
    n 是 int 类型
    width 是 int 类型

    把 n 的位数变成 width 这么长，并在右对齐，不足部分用 0 补足并返回
    具体请看测试, 注意, 返回的是 str 类型

    返回 str 类型

    提示:
    计算 n 的长度, 随后生成一串指定长度的 0, 使两者组合后长度为 width

    分步提示:
    1. 将 n 转化为字符串并计算长度
    2. 在 zfill 函数前, 构建一个辅助函数 n_char, 生成一个长度为 n 的 0 字符串
    3. 算出需要填充的 0 的个数并使用 n_char 生成
    4. 拼接
    """
    ...


# 测试函数
def test_zfill():
    ensure(zfill(1, 4) == '0001', 'zfill 测试 1')
    ensure(zfill(23, 4) == '0023', 'zfill 测试 2')
    ensure(zfill(12345, 4) == '12345', 'zfill 测试 3')
    ensure(zfill(169, 5) == '00169', 'zfill 测试 4')


# 调用测试函数
test_zfill()





# 作业 2
#
# 注意, 这是一个新的知识点, 叫 默认参数
# fillchar 这个参数如果你不提供, 它的值默认就是 ' '
# 语法就是这样
def rjust(s, width, fillchar=' '):
    """
    s 是 str
    width 是 int
    fillchar 是 长度为 1 的字符串, 默认为空格 ' '

    如果 s 长度小于 width, 则在开头用 fillchar 填充并返回

    返回 string 类型

    提示:
    类似于作业 1, 但有几个区别
    一是不需要先用 str() 转换类型
    二是填充的字符不是 0 而是可以自行定义

    分步提示：
    1. 计算需要用 fillchar 生成的字符串长度
    2. 使用作业 1 中的辅助函数 n_char, 修改它以便符合本题的使用
    3. 调用修改后的 n_char 生成填充用的字符串
    4. 拼接并返回结果
    """



# 测试函数
def test_rjust():
    ensure(rjust('gua', 5) == '  gua', 'rjust 测试 1')
    ensure(rjust('guagua', 5) == 'guagua', 'rjust 测试 2')
    ensure(rjust('gua', 5, '*') == '**gua', 'rjust 测试 3')




# 作业 3
#
def ljust(s, width, fillchar=' '):
    """
    s 是 str
    width 是 int
    fillchar 是 长度为 1 的字符串, 默认为空格 ' '

    如果 s 长度小于 width, 则在末尾用 fillchar 填充并返回
    否则, 原样返回, 不做额外处理

    返回 str 类型

    提示:
    类似于作业 2, 区别是填充位置在左侧而不是右侧

    分步提示:
    1. 复制作业 2 中的代码, 记得把函数名改成 ljust
    2. 把作业 2 最后一步的字符串拼接的两个元素调换位置
    """


# 测试函数
def test_ljust():
    ensure(ljust('gua', 5) == 'gua  ', 'ljust 测试 1')
    ensure(ljust('guagua', 5) == 'guagua', 'ljust 测试 2')
    ensure(ljust('gua', 5, '*') == 'gua**', 'ljust 测试 3')
    
    



# 作业 4
#
def center(s, width, fillchar=' '):
    """
    s 是 str
    width 是 int
    fillchar 是 长度为 1 的字符串, 默认为空格 ' '

    如果 s 长度小于 width, 则在两边用 fillchar 填充并返回
    如果 s 长度和 width 互为奇偶, 则无法平均分配两边的 fillchar
        这种情况下, 让左边的 fillchar 数量小于右边

    返回 str 类型

    提示:
    需要计算 s 左右两侧字符串的长度后, 分别生成左右填充字符串, 并最终把三者按顺序拼接

    分步提示:
    1. 计算左右填充字符串的总长度
    2. 计算左右填充字符串的长度，注意要是整数
    3. 生成左右两个填充字符串
    4. 拼接字符串, 并返回结果
    """


# 测试函数
def test_center():
    ensure(center('gua', 5) == ' gua ', 'center 测试 1')
    ensure(center('gua', 5, '*') == '*gua*', 'center 测试 2')
    ensure(center('gw', 5) == ' gw  ', 'center 测试 3')
    ensure(center('gua', 6) == ' gua  ', 'center 测试 4')



# 作业 5
#
def is_space(s):
    """
    s 是 str
    检查 s 中是否只包含空格

    返回 bool, 如果 s 中包含的只有空格则返回 True, 否则返回 False

    提示:
    遍历 s 中的所有字符, 其中如果包含非空格字符, 返回 False, 否则返回 True

    分步提示:
    1. 如果是一个空字符串返回 False
    2. 遍历 s 中的每个字符
    3. 如果字符不是空格, 返回 False
    4. 在循环结束后, 返回 True
    """



# 测试函数
def test_is_space():
    ensure(is_space(' '), 'center 测试 1')
    ensure(is_space('   '), 'center 测试 2')
    ensure(not is_space(''), 'center 测试 3')
    ensure(not is_space('gua'), 'center 测试 4')
    ensure(not is_space('  gua'), 'center 测试 5')



# 作业 6
#
def is_digit(s):
    """
    s 是字符串
    检查 s 中是否只包含数字
    返回: bool

    提示:
    类似于作业 5, 判断的条件从空格变为了数字

    分步提示:
    1. 复制 is_space 函数中的代码
    2. 将判断字符是否为空格的部分改为判断是否为数字
        通过判断字符是否在字符串 '0123456789' 中, 来判断其是否为数字
    """


# 测试函数
def test_is_digit():
    ensure(is_digit('123'), 'is_digit 测试 1')
    ensure(is_digit('0'), 'is_digit 测试 2')
    ensure(not is_digit('  '), 'is_digit 测试 3')
    ensure(not is_digit('1.1'), 'is_digit 测试 4')
    ensure(not is_digit('gua'), 'is_digit 测试 5')
    ensure(not is_digit(''), 'is_digit 测试 6')




# 作业 7
#
def strip_left(s):
    """
    s 是 str
    返回一个「删除了字符串开始的所有空格」的字符串

    返回 str

    提示:
    从左侧遍历字符串, 记录第一个非空格字符的位置, 并由此切割字符串

    分步提示:
    1. 使用作业 5 的 is_space 函数来判断 s 是否只包含空格，
       如果 s 只包含空格，返回空字符串
    2. 遍历字符串找到不是空格的字符的下标
    3. 切片并返回
    """


# 测试函数
def test_strip_left():
    ensure(strip_left('  gua') == 'gua', 'strip_left 测试 1')
    ensure(strip_left(' gua  ') == 'gua  ', 'strip_left 测试 2')
    ensure(strip_left('') == '', 'strip_left 测试 3')
    ensure(strip_left('    ') == '', 'strip_left 测试 4')



# 作业 8
#
def strip_right(s):
    """
    s 是 str
    返回一个「删除了字符串末尾的所有空格」的字符串

    返回 str

    提示:
    类似于作业 7
    区别在于这次需要从右至左遍历字符串

    分步提示:
    1. 创建一个循环, 从右到左遍历字符串
        从右到左遍历的参考代码:
        for i in range(len(s)):
            index = len(s) - i - 1
    2. 遍历字符串找到不是空格的字符的下标
    3. 切片并返回
    """


# 测试函数
def test_strip_right():
    ensure(strip_right('gua') == 'gua', 'strip_right 测试 1')
    ensure(strip_right(' gua  ') == ' gua', 'strip_right 测试 2')
    ensure(strip_right('') == '', 'strip_right 测试 3')
    ensure(strip_right('    ') == '', 'strip_right 测试 4')



# 作业 9
#
def strip(s):
    """
    s 是 str
    返回一个「删除了字符串首尾的所有空格」的字符串

    返回 str

    提示:
    依次调用作业 7 和作业 8 中的函数即可

    分布提示:
    1. 调用 strip_left
    2. 对上一步的结果继续调用 strip_right
    3. 返回结果
    """


# 测试函数
def test_strip():
    ensure(strip('  gua') == 'gua', 'strip 测试 1')
    ensure(strip(' gua  ') == 'gua', 'strip 测试 2')
    ensure(strip('') == '', 'strip 测试 3')
    ensure(strip('    ') == '', 'strip 测试 4')





# 作业 10
#
def replace(s, old_str, new_str):
    """
    3 个参数 s old_str new_str 都是字符串
    返回一个「将 s 中的 old_str 字符串替换为 new_str 字符串」的字符串
    假设 old 存在并且只出现一次

    返回 str

    提示:
    找到指定旧字符串的起始下标, 将其前后字符串与新字符串进行拼接

    分步提示:
    1. 找到 old_str 的下标
    2. 把 s 切成 2 个不包含 old_str 的字符串
    3. 拼接并返回结果
    """


# 测试函数自行添加



作业 11

'''
这个作业是选做的, 如果你不想做或者不会做, 直接在答案处写上下面这句话的拼音
我选择不做这道题


本题将对一段凯撒加密后的密文进行解密。
该段密文有多行内容，每一行在加密时都采用了不同（或相同）的位移数 shift 。
但每行加密时的位移数未知。
请求出该段密文的明文。


本次作业提供字库 words.py，存储了常用的英文单词。 words.py 中是一个名为 words 的集合。
判断某元素是否存在于集合中，用 if a in set 的语法。


字符串有一个split()方法，用来在指定分隔符处对字符串进行切片。用法如下：
'  a b  '.split()
结果为：['a', 'b']

注意换行符的转义符是  '\n'，也就是说我们用 '\n' 表示换行符
'''


# 引入我们需要的词库，词库中存储着英文常用单词，这个文件在群文件，请自行下载
from words import words


def best_answer(possible_answers):
    # 在 26 种可能解中，寻找最优解。


def decode_line(line):
    # 针对一行密文解密，通过调用 best_answer 函数，返回最优解


def decode_random(code):
    # 将一段密文分解为一行行不知道 shift 的句子
    # 每行句子调用 decode_line


def __main():
    code = '''WKH TXLFN EURZQ IRA MXPSV RYHU WKH ODCB GRJ
    JXU GKYSA RHEMD VEN ZKCFI ELUH JXU BQPO TEW
    BPM YCQKS JZWEV NWF RCUXA WDMZ BPM TIHG LWO'''
    # 请调用所需的函数，并打印出最终的明文


__main()


分步提示：
1，我们只要能解密一行就能解密任意行，所以先实现一个解密一行不知道 shift 的句子的函数

2，把一行句子转成包含单词的 list

3，一共有 26 种 shift，对于每一个可能的 shift 查看有几个解密后的单词在 words 中

4，单词命中最高的那一个 shift 就是正确的 shift


```