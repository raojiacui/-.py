log = print
lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# 作业 1
# 注意多看提示和提问
def find(s1, s2):
    for i in range(0, len(s1)):
        if s1[i] == s2:
            return i
    return -1


# 作业 2
# 定义一个函数
# 参数是一个字符串 s
# 返回大写后的字符串
# 注意, 假设 s 字符串全是小写字母
# 注意, 自行实现测试函数, 之后的题目都要求自行实现测试函数
def uppercase(s):
    result = ''
    for i in range(0, len(s)):
        index = find(lower, s[i])
        result += upper[index]
    return result


# 作业 3
# 实现 lowercase1
# 它能正确处理带 小写字母 的字符串
def lowercase1(s):
    result = ''
    for i in range(0, len(s)):
        if s[i] in upper:
            index = find(upper, s[i])
            result += lower[index]
        else:  
            result += s[i]
    return result


# 作业 4
# 实现 uppercase1
# 它能正确处理带 大写字母 的字符串:
def uppercase(s):
    result = ''
    for i in range(0, len(s)):
        if s[i] in lower:
            index = find(lower, s[i])
            result += upper[index]
        else:
            result += s[i]
    return result


# 作业 5
# 实现一个叫 凯撒加密 的加密算法, 描述如下
# 对于一个字符串, 整体移位, 就是加密
# 以右移 1 位为例
# 原始信息 'afz' 会被加密为 'bga'
# 实现 encode1 函数, 把明文加密成密码并返回
# 右移 1 位
# 注意:
# s 是一个只包含小写字母的字符串
def encode1(s):
    result = ''
    for i in range(0, len(s)):
        index = find(lower, s[i])
        if index == 25:
            result += lower[0]
        else:
            result += lower[index + 1]
    return result


# 作业 6
# 实现 decode1 函数, 把作业 5 加密的密码解密为明文并返回
# 注意:
# s 是一个只包含小写字母的字符串
def decode1(s):
    result = ''
    for i in range(0, len(s)):
        index = find(lower, s[i])
        if index == 0:
            result += lower[25]
        else:
            result += lower[index - 1]
    return result


# 作业 7
# 实现 encode2
# 多了一个参数 shift 表示移的位数
# 注意:
# s 是一个只包含小写字母的字符串
def encode2(s, shift):
    result = ''
    for i in range(0, len(s)):
        index = find(lower, s[i]) 
        if index + shift == 25:
            result += lower[0]
        else:
            result += lower[index + shift]
    return result


# 作业 8
# 实现 decode2
# 多了一个参数 shift 表示移的位数
# 注意:
# s 是一个只包含小写字母的字符串
def decode2(s, shift):
    result = ''
    for i in range(0, len(s)):
        index = find(lower, s[i])
        if index - shift <= 0:
            new_index = (index - shift) % 26
            result += lower[new_index]
        else:
            result += lower[index - shift]
    return result


# 作业 9
# 实现 encode3
# 多了一个参数 shift 表示移的位数
# 如果 s 中包含了不是字母的字符, 比如空格或者其他符号, 则对这个字符不做处理保留原样
# 注意:
# s 是一个只包含小写字母和不是字母的字符的字符串
def encode3(s, shift):
    result = ''
    for i in range(0, len(s)):
        if s[i] in lower:
            index = find(lower, s[i])
            new_index = (index + shift) % 26
            result += lower[new_index]
        else:
            result += s[i]
    return result


# 作业 10
# 实现 decode3
# 多了一个参数 shift 表示移的位数
# 如果 s 中包含了不是字母的字符, 比如空格或者其他符号, 则对这个字符不做处理保留原样
def decode3(s, shift):
    result = ''
    for i in range(0, len(s)):
        if s[i] in lower:
            index = find(lower, s[i])
            new_index = (index - shift) % 26
            result += lower[new_index]
        else:
            result += s[i]
    return result


#作业11
code = 'VRPHWLPHV L ZDQW WR FKDW ZLWK BRX,EXW L KDYH QR UHDVRQ WR FKDW ZLWK BRX'
def decode4(s):
    lower_s = lowercase1(s)
    for shift in range(1, 26):
       result = decode3(lower_s, shift)
#        log(f"shift={shift}: {result}")  
# decode4(code)

    
#作业12
def find2(s1, s2):
    for i in range(len(s1) - len(s2) + 1):
        if s1[i:i + len(s2)] == s2:
            return i
    return -1


#作业13
def find_between(s, left, right):
    left_pos = find2(s, left)
    if left_pos == -1:
        return -1
    content_start = left_pos + len(left)
    right_pos = find2(s, right)
    if right_pos == -1:
        return -1
    return s[content_start:right_pos]


import urllib.request
def openurl():
    # 这里把 url 写死为豆瓣 top250 页面
    url = 'https://movie.douban.com/top250'
    # 下载页面, 得到的是一个 bytes 类型的变量 s
    s = urllib.request.urlopen(url).read()
    # 用 utf-8 编码把 s 转为字符串并返回
    content = s.decode('utf-8')
    return content











# ==================== 测试代码 ====================

# 取消注释来测试各个函数


#log(find("Hello", "e")


#log(f"uppercase('abc') = {uppercase('abc')},期望: ABC")


#log(f"lowercase1('Hello') = {lowercase1('Hello')},期望: hello")


#log(f"uppercase('acd') = {uppercase('acd')},期望: ACD")


#log(encode1('acd'))


#log(decode1('bde'))


#log(encode2('abc', 1))


#log(decode2('bcd', 1))


#log(encode3('a-b-c', 1))


#log(decode3('a-b-c', 1))


# log(f"shift={shift}: {result}")  
# decode4(code)


#log(find2("Hello", "e"))


# s1 = 'meet #<gua># halfway'
# s2 = 'meet #<gua># #<high>#way'
# left = '#<'
# right = '>#'

# content1 = find_between(s1, left, right)
# content2 = find_between(s2, left, right)

# print('结果1 ', content1)
# print('结果2 ', content2)


#log(openurl)


