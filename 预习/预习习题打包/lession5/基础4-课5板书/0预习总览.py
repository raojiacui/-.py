def log(*args, **kwargs):
    print(*args, **kwargs)


# for i in [1, 3, 4]:
#     log('i, ', i)
#     log('a, ', a)


# # 多行凯撒加密，每行移位不一样
# code = '''
# WKH TXLFN EURZQ IRA MXPSV RYHU WKH ODCB GRJ
# JXU GKYSA RHEMD VEN ZKCFI ELUH JXU BQPO TEW
# BPM YCQKS JZWEV NWF RCUXA WDMZ BPM TIHG LWO
# '''
#
# 1, 分成一行一行的
# 2, 一共 26 中情况，针对每一行列出所有情况下的结果
# 3, 断开一行中的词，与词库进行比对
# 4, 选出最优解


"""
decode
encode(26 - n)



oo


*args **kwargs  关键字参数

列表推导式

生成器表达式

tuple tuple set 集合表达式

异常捕获

内建函数 abs(), len()

各个语言, 各个编程方向




项目
用python处理数据 csv
写游戏
写爬虫

写 GUI 程序, 音乐播放器
https://github.com/HuberTRoy/MusicBox

词典软件, GUI 扩展, 音频合成读取







for i in a 语法
import

"""
for i in [1, 3, 4]:
    log('i, ', i)

for i in 'asbb':
    log('i, ', i)

lower = 'abcd'
upper = 'ABCD'


def lowercase(s):
    result = ''
    for c in s:
        # 对每一个字符，找到它在 upper 中的下标
        i = upper.find(c)
        result += lower[i]
    return result


s = 'AB'
log(lowercase(s))

# import
# import math
# math.sin()


# 方法一
import words

words.words

# 方法二
from words import words

words

# 方法三
from words import *

words

# 异常捕获
# print(int('2.5'))


try:
    int('2.5')
except ValueError as e:
    print('error, ', e)

# 不应该写这个东西，应该把错误都改过来
