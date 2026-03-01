# 作业 4 参考答案
# 复用思想：后面的函数调用前面已实现的函数


# ==================== 辅助函数 ====================

# log 函数用于调试输出
# 上课会讲这个原理，现在直接拿来用即可
def log(*args, **kwargs):
    print(*args, **kwargs)


# ensure 函数用于测试
# condition 是 bool, 如果为 false, 则输出 message
def ensure(condition, message):
    if not condition:
        log('*** 测试失败:', message)


# ==================== 基础字符串 ====================

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


# ==================== 作业 1: 查找字符位置 ====================

# 作业 1
# 注意多看提示和提问
def find(s1, s2):
    """
    s1 s2 都是 string
    但 s2 的长度是 1

    返回 s2 在 s1 中的下标, 从 0 开始, 如果不存在则返回 -1
    """
    # 遍历字符串 s1
    for i in range(len(s1)):
        # 如果当前字符等于 s2，返回下标 i
        if s1[i] == s2:
            return i
    # 如果循环结束都没有找到，返回 -1
    return -1


# 测试函数
def test_find():
    # 成功的测试用例
    ensure(find('hello', 'e') == 1, 'find 成功测试 1 失败')
    ensure(find('hello', 'l') == 2, 'find 成功测试 2 失败')
    ensure(find('world', 'o') == 1, 'find 成功测试 3 失败')
    ensure(find('abc', 'a') == 0, 'find 成功测试 4 失败')
    ensure(find('abc', 'c') == 2, 'find 成功测试 5 失败')

    # 失败的测试用例
    ensure(find('hello', 'x') == -1, 'find 失败测试 1 失败')
    ensure(find('world', 'z') == -1, 'find 失败测试 2 失败')
    ensure(find('abc', 'd') == -1, 'find 失败测试 3 失败')


# ==================== 作业 2: 小写转大写 ====================

# 作业 2
# 定义一个函数
# 参数是一个字符串 s
# 返回大写后的字符串
# 注意, 假设 s 字符串全是小写字母
def uppercase(s):
    # 初始化一个空字符串用来保存结果
    result = ''
    # 遍历字符串 s
    for i in range(len(s)):
        # 使用 find 函数找到 s[i] 在 lower 中的下标
        index = find(lower, s[i])
        # 把对应的大写字母拼接到 result 中
        result += upper[index]
    # 返回结果
    return result


# 测试函数
def test_uppercase():
    # 成功的测试用例
    ensure(uppercase('abc') == 'ABC', 'uppercase 成功测试 1 失败')
    ensure(uppercase('hello') == 'HELLO', 'uppercase 成功测试 2 失败')
    ensure(uppercase('world') == 'WORLD', 'uppercase 成功测试 3 失败')
    ensure(uppercase('xyz') == 'XYZ', 'uppercase 成功测试 4 失败')

    # 失败的测试用例（验证转换结果不等于原字符串）
    ensure(uppercase('abc') != 'abc', 'uppercase 失败测试 1 失败')
    ensure(uppercase('hello') != 'Hello', 'uppercase 失败测试 2 失败')


# ==================== 作业 3: 处理包含小写字母的字符串转小写 ====================

# 作业 3
# 实现 lowercase1
# 它能正确处理带 小写字母 的字符串
def lowercase1(s):
    # 初始化一个空字符串用来保存结果
    result = ''
    # 遍历字符串 s
    for i in range(len(s)):
        # 如果当前字符是大写字母
        if s[i] in upper:
            # 使用 find 函数找到 s[i] 在 upper 中的下标
            index = find(upper, s[i])
            # 把对应的小写字母拼接到 result 中
            result += lower[index]
        else:
            # 如果不是大写字母，直接拼接
            result += s[i]
    # 返回结果
    return result


# 测试函数
def test_lowercase1():
    # 成功的测试用例
    ensure(lowercase1('Hello') == 'hello', 'lowercase1 成功测试 1 失败')
    ensure(lowercase1('HELLO') == 'hello', 'lowercase1 成功测试 2 失败')
    ensure(lowercase1('Hello World') == 'hello world', 'lowercase1 成功测试 3 失败')
    ensure(lowercase1('ABC123') == 'abc123', 'lowercase1 成功测试 4 失败')

    # 失败的测试用例（验证转换结果不等于原字符串）
    ensure(lowercase1('Hello') != 'Hello', 'lowercase1 失败测试 1 失败')
    ensure(lowercase1('HELLO') != 'HELLO', 'lowercase1 失败测试 2 失败')


# ==================== 作业 4: 处理包含大写字母的字符串转大写 ====================

# 作业 4
# 实现 uppercase1
# 它能正确处理带 大写字母 的字符串
def uppercase1(s):
    # 初始化一个空字符串用来保存结果
    result = ''
    # 遍历字符串 s
    for i in range(len(s)):
        # 如果当前字符是小写字母
        if s[i] in lower:
            # 使用 find 函数找到 s[i] 在 lower 中的下标
            index = find(lower, s[i])
            # 把对应的大写字母拼接到 result 中
            result += upper[index]
        else:
            # 如果不是小写字母，直接拼接
            result += s[i]
    # 返回结果
    return result


# 测试函数
def test_uppercase1():
    # 成功的测试用例
    ensure(uppercase1('Hello') == 'HELLO', 'uppercase1 成功测试 1 失败')
    ensure(uppercase1('hello') == 'HELLO', 'uppercase1 成功测试 2 失败')
    ensure(uppercase1('Hello World') == 'HELLO WORLD', 'uppercase1 成功测试 3 失败')
    ensure(uppercase1('abc123') == 'ABC123', 'uppercase1 成功测试 4 失败')

    # 失败的测试用例（验证转换结果不等于原字符串）
    ensure(uppercase1('Hello') != 'Hello', 'uppercase1 失败测试 1 失败')
    ensure(uppercase1('hello') != 'hello', 'uppercase1 失败测试 2 失败')


# ==================== 作业 5: 凯撒加密（右移1位） ====================

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
    # 初始化一个空字符串用来保存结果
    result = ''
    # 遍历字符串 s
    for i in range(len(s)):
        # 使用 find 函数找到 s[i] 在 lower 中的下标
        index = find(lower, s[i])
        # 右移 1 位，需要处理边界情况
        if index == 25:
            # 如果是 'z'，则变成 'a'
            result += lower[0]
        else:
            # 否则，取下一位字符
            result += lower[index + 1]
    # 返回结果
    return result


# 测试函数
def test_encode1():
    # 成功的测试用例
    ensure(encode1('abc') == 'bcd', 'encode1 成功测试 1 失败')
    ensure(encode1('xyz') == 'yza', 'encode1 成功测试 2 失败')
    ensure(encode1('afz') == 'bga', 'encode1 成功测试 3 失败')
    ensure(encode1('hello') == 'ifmmp', 'encode1 成功测试 4 失败')

    # 失败的测试用例（验证加密后不等于原文）
    ensure(encode1('abc') != 'abc', 'encode1 失败测试 1 失败')
    ensure(encode1('xyz') != 'xyz', 'encode1 失败测试 2 失败')


# ==================== 作业 6: 凯撒解密（左移1位） ====================

# 作业 6
# 实现 decode1 函数, 把作业 5 加密的密码解密为明文并返回
# 注意:
# s 是一个只包含小写字母的字符串
def decode1(s):
    # 初始化一个空字符串用来保存结果
    result = ''
    # 遍历字符串 s
    for i in range(len(s)):
        # 使用 find 函数找到 s[i] 在 lower 中的下标
        index = find(lower, s[i])
        # 左移 1 位，需要处理边界情况
        if index == 0:
            # 如果是 'a'，则变成 'z'
            result += lower[25]
        else:
            # 否则，取前一位字符
            result += lower[index - 1]
    # 返回结果
    return result


# 测试函数
def test_decode1():
    # 成功的测试用例
    ensure(decode1('bcd') == 'abc', 'decode1 成功测试 1 失败')
    ensure(decode1('yza') == 'xyz', 'decode1 成功测试 2 失败')
    ensure(decode1('bga') == 'afz', 'decode1 成功测试 3 失败')
    ensure(decode1('ifmmp') == 'hello', 'decode1 成功测试 4 失败')

    # 失败的测试用例（验证解密后不等于密文）
    ensure(decode1('bcd') != 'bcd', 'decode1 失败测试 1 失败')
    ensure(decode1('yza') != 'yza', 'decode1 失败测试 2 失败')

    # 验证加密解密互逆
    ensure(decode1(encode1('hello')) == 'hello', 'decode1 互逆测试失败')


# ==================== 作业 7: 凯撒加密（指定位数） ====================

# 作业 7
# 实现 encode2
# 多了一个参数 shift 表示移的位数
# 注意:
# s 是一个只包含小写字母的字符串
def encode2(s, shift):
    # 初始化一个空字符串用来保存结果
    result = ''
    # 遍历字符串 s
    for i in range(len(s)):
        # 使用 find 函数找到 s[i] 在 lower 中的下标
        index = find(lower, s[i])
        # 右移 shift 位，使用模运算处理边界情况
        new_index = (index + shift) % 26
        # 拼接结果
        result += lower[new_index]
    # 返回结果
    return result


# 测试函数
def test_encode2():
    # 成功的测试用例
    ensure(encode2('abc', 1) == 'bcd', 'encode2 成功测试 1 失败')
    ensure(encode2('abc', 2) == 'cde', 'encode2 成功测试 2 失败')
    ensure(encode2('xyz', 3) == 'abc', 'encode2 成功测试 3 失败')
    ensure(encode2('hello', 5) == 'mjqqt', 'encode2 成功测试 4 失败')

    # 失败的测试用例（验证加密后不等于原文）
    ensure(encode2('abc', 1) != 'abc', 'encode2 失败测试 1 失败')
    ensure(encode2('xyz', 3) != 'xyz', 'encode2 失败测试 2 失败')

    # 边界测试
    ensure(encode2('a', 26) == 'a', 'encode2 边界测试 1 失败')
    ensure(encode2('a', 27) == 'b', 'encode2 边界测试 2 失败')


# ==================== 作业 8: 凯撒解密（指定位数） ====================

# 作业 8
# 实现 decode2
# 多了一个参数 shift 表示移的位数
# 注意:
# s 是一个只包含小写字母的字符串
def decode2(s, shift):
    # 初始化一个空字符串用来保存结果
    result = ''
    # 遍历字符串 s
    for i in range(len(s)):
        # 使用 find 函数找到 s[i] 在 lower 中的下标
        index = find(lower, s[i])
        # 左移 shift 位，使用模运算处理边界情况
        new_index = (index - shift) % 26
        # 拼接结果
        result += lower[new_index]
    # 返回结果
    return result


# 测试函数
def test_decode2():
    # 成功的测试用例
    ensure(decode2('bcd', 1) == 'abc', 'decode2 成功测试 1 失败')
    ensure(decode2('cde', 2) == 'abc', 'decode2 成功测试 2 失败')
    ensure(decode2('abc', 3) == 'xyz', 'decode2 成功测试 3 失败')
    ensure(decode2('mjqqt', 5) == 'hello', 'decode2 成功测试 4 失败')

    # 失败的测试用例（验证解密后不等于密文）
    ensure(decode2('bcd', 1) != 'bcd', 'decode2 失败测试 1 失败')
    ensure(decode2('abc', 3) != 'abc', 'decode2 失败测试 2 失败')

    # 边界测试
    ensure(decode2('a', 26) == 'a', 'decode2 边界测试 1 失败')
    ensure(decode2('b', 27) == 'a', 'decode2 边界测试 2 失败')

    # 验证加密解密互逆
    ensure(decode2(encode2('hello', 7), 7) == 'hello', 'decode2 互逆测试失败')


# ==================== 作业 9: 凯撒加密（处理非字母字符） ====================

# 作业 9
# 实现 encode3
# 多了一个参数 shift 表示移的位数
# 如果 s 中包含了不是字母的字符, 比如空格或者其他符号, 则对这个字符不做处理保留原样
# 注意:
# s 是一个只包含小写字母和不是字母的字符的字符串
def encode3(s, shift):
    # 初始化一个空字符串用来保存结果
    result = ''
    # 遍历字符串 s
    for i in range(len(s)):
        # 如果当前字符是小写字母
        if s[i] in lower:
            # 使用 find 函数找到 s[i] 在 lower 中的下标
            index = find(lower, s[i])
            # 右移 shift 位，使用模运算处理边界情况
            new_index = (index + shift) % 26
            # 拼接结果
            result += lower[new_index]
        else:
            # 如果不是小写字母，直接拼接
            result += s[i]
    # 返回结果
    return result


# 测试函数
def test_encode3():
    # 成功的测试用例
    ensure(encode3('a-b-c', 1) == 'b-c-d', 'encode3 成功测试 1 失败')
    ensure(encode3('hello world', 1) == 'ifmmp xpsme', 'encode3 成功测试 2 失败')
    ensure(encode3('abc xyz!', 3) == 'def abc!', 'encode3 成功测试 3 失败')
    ensure(encode3('test-123', 2) == 'vguv-123', 'encode3 成功测试 4 失败')

    # 失败的测试用例（验证非字母字符保持不变）
    ensure(encode3('a b', 1) != 'abc', 'encode3 失败测试 1 失败')
    ensure(encode3('a-b', 1) != 'bcd', 'encode3 失败测试 2 失败')

    # 验证特殊字符保持不变
    result = encode3('a!b@c#', 1)
    ensure(result == 'b!c@d#', 'encode3 特殊字符测试失败')


# ==================== 作业 10: 凯撒解密（处理非字母字符） ====================

# 作业 10
# 实现 decode3
# 多了一个参数 shift 表示移的位数
# 如果 s 中包含了不是字母的字符, 比如空格或者其他符号, 则对这个字符不做处理保留原样
def decode3(s, shift):
    # 初始化一个空字符串用来保存结果
    result = ''
    # 遍历字符串 s
    for i in range(len(s)):
        # 如果当前字符是小写字母
        if s[i] in lower:
            # 使用 find 函数找到 s[i] 在 lower 中的下标
            index = find(lower, s[i])
            # 左移 shift 位，使用模运算处理边界情况
            new_index = (index - shift) % 26
            # 拼接结果
            result += lower[new_index]
        else:
            # 如果不是小写字母，直接拼接
            result += s[i]
    # 返回结果
    return result


# 测试函数
def test_decode3():
    # 成功的测试用例
    ensure(decode3('b-c-d', 1) == 'a-b-c', 'decode3 成功测试 1 失败')
    ensure(decode3('ifmmp xpsme', 1) == 'hello world', 'decode3 成功测试 2 失败')
    ensure(decode3('def abc!', 3) == 'abc xyz!', 'decode3 成功测试 3 失败')
    ensure(decode3('vguv-123', 2) == 'test-123', 'decode3 成功测试 4 失败')

    # 失败的测试用例（验证非字母字符保持不变）
    ensure(decode3('b c', 1) != 'abc', 'decode3 失败测试 1 失败')
    ensure(decode3('b-c', 1) != 'abc', 'decode3 失败测试 2 失败')

    # 验证特殊字符保持不变
    result = decode3('b!c@d#', 1)
    ensure(result == 'a!b@c#', 'decode3 特殊字符测试失败')

    # 验证加密解密互逆
    ensure(decode3(encode3('hello world!', 5), 5) == 'hello world!', 'decode3 互逆测试失败')


# ==================== 作业 11: 破译知乎密码 ====================

# 作业 11
# 知乎有一个求助题, 破译密码的
# 链接在此
# https://www.zhihu.com/question/28324597
# 这一看就是凯撒加密...
# 我把密码放在下面, 请解出原文
code = 'VRPHWLPHV L ZDQW WR FKDW ZLWK BRX,EXW L KDYH QR UHDVRQ WR FKDW ZLWK BRX'


def decode4(s):
    # 先把字符串转成小写（大写字母转成小写，空格和标点不要转）
    lower_s = lowercase1(s)
    # 尝试所有的 shift 值（1 到 25）
    for shift in range(1, 26):
        # 解密
        result = decode3(lower_s, shift)
        # 输出结果供观察
        log(f'shift={shift}: {result}')


# ==================== 作业 12: 查找字符串位置 ====================

# 作业 12
def find2(s1, s2):
    """
    s1 s2 都是 str
    两个 str 的长度不限

    返回 s2 在 s1 中的下标, 从 0 开始, 如果不存在则返回 -1
    """
    # 遍历字符串 s1，注意边界条件
    for i in range(len(s1) - len(s2) + 1):
        # 用切片的方式取出与 s2 长度相等的字符串
        if s1[i:i + len(s2)] == s2:
            # 如果相等，返回下标 i
            return i
    # 如果循环结束都没有找到，返回 -1
    return -1


# 测试函数
def test_find2():
    # 成功的测试用例
    ensure(find2('hello world', 'world') == 6, 'find2 成功测试 1 失败')
    ensure(find2('hello world', 'hello') == 0, 'find2 成功测试 2 失败')
    ensure(find2('aaa', 'aa') == 0, 'find2 成功测试 3 失败')
    ensure(find2('abc def ghi', 'def') == 4, 'find2 成功测试 4 失败')

    # 失败的测试用例
    ensure(find2('hello world', 'xyz') == -1, 'find2 失败测试 1 失败')
    ensure(find2('abc', 'abcd') == -1, 'find2 失败测试 2 失败')
    ensure(find2('hello', 'world') == -1, 'find2 失败测试 3 失败')

    # 边界测试
    ensure(find2('abc', 'abc') == 0, 'find2 边界测试 1 失败')
    ensure(find2('abc', 'a') == 0, 'find2 边界测试 2 失败')
    ensure(find2('abc', 'c') == 2, 'find2 边界测试 3 失败')


# ==================== 作业 13: 提取两个标记之间的内容 ====================

# 作业 13
def find_between(s, left, right):
    """
    s, left, right 都是 str
    返回 left 和 right 之间包含的字符串
    """
    # 使用 find2 函数找到 left 的位置
    left_pos = find2(s, left)
    # 如果 left 不存在，返回 -1
    if left_pos == -1:
        return -1
    # 计算 left 之后的起始位置
    content_start = left_pos + len(left)
    # 从 left 之后开始查找 right 的位置
    right_pos = find2(s[content_start:], right)
    # 如果 right 不存在，返回 -1
    if right_pos == -1:
        return -1
    # 计算实际的 right 位置（相对于原始字符串）
    actual_right_pos = content_start + right_pos
    # 用切片提取内容
    return s[content_start:actual_right_pos]


# 测试函数
def test_find_between():
    s1 = 'meet #<gua># halfway'
    s2 = 'meet #<gua># #<high>#way'
    left = '#<'
    right = '>#'

    # 成功的测试用例
    ensure(find_between(s1, left, right) == 'gua', 'find_between 成功测试 1 失败')
    ensure(find_between(s2, left, right) == 'gua', 'find_between 成功测试 2 失败')
    ensure(find_between('<hello>world<test>', '<', '>') == 'hello', 'find_between 成功测试 3 失败')
    ensure(find_between('name: [value] end', '[', ']') == 'value', 'find_between 成功测试 4 失败')
    ensure(find_between('start**middle**end', '**', '**') == 'middle', 'find_between 成功测试 5 失败')

    # 失败的测试用例
    ensure(find_between('hello world', '#<', '>#') == -1, 'find_between 失败测试 1 失败')
    ensure(find_between('hello world', 'hello', 'xyz') == -1, 'find_between 失败测试 2 失败')
    ensure(find_between('no markers here', '<', '>') == -1, 'find_between 失败测试 3 失败')

    # 边界测试
    ensure(find_between('<a>', '<', '>') == 'a', 'find_between 边界测试 1 失败')
    ensure(find_between('<<>>', '<<', '>>') == '', 'find_between 边界测试 2 失败')


# ==================== 作业 14: 爬虫获取豆瓣电影评分 ====================

# 作业 14
# 这是一个简单的爬虫
import urllib.request


def openurl(url):
    """
    下载网页内容并返回字符串
    添加请求头模拟浏览器访问，避免反爬虫机制
    """
    # 创建请求头，模拟浏览器访问
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Referer': 'https://www.douban.com/',
    }

    # 创建 Request 对象
    request = urllib.request.Request(url, headers=headers)

    # 下载页面, 得到的是一个 bytes 类型的变量 s
    s = urllib.request.urlopen(request).read()

    # 用 utf-8 编码把 s 转为字符串并返回
    content = s.decode('utf-8')
    return content


def ratings():
    """
    返回一个 list, 包含 25 个电影的评分
    注意, 电影评分是 str 类型
    """
    # 豆瓣 top250 的 url
    url = 'https://movie.douban.com/top250'
    # 下载页面内容
    content = openurl(url)
    # 用于保存评分的列表
    rating_list = []
    # 评分的左右标记
    left = 'property="v:average">'
    right = '</span>'
    # 循环查找所有评分，只获取前25个
    while len(rating_list) < 25:
        # 查找评分
        rating = find_between(content, left, right)
        # 如果找不到，说明已经找完了
        if rating == -1:
            break
        # 把评分添加到列表中
        rating_list.append(rating)
        # 切片，去掉已经处理过的部分
        # 找到 right 的位置
        right_pos = find2(content, right)
        # 切片
        content = content[right_pos + len(right):]
    # 返回评分列表
    return rating_list


# ==================== 主程序入口 ====================


def main():
    """
    作业4主函数 - 运行所有测试
    """
    log('========== 开始测试作业4所有函数 ==========\n')

    # 测试作业 1 - 查找字符位置
    log('测试作业 1 - find 函数:')
    test_find()
    log('find 测试通过\n')

    # 测试作业 2 - 小写转大写
    log('测试作业 2 - uppercase 函数:')
    test_uppercase()
    log('uppercase 测试通过\n')

    # 测试作业 3 - 处理包含小写字母的字符串转小写
    log('测试作业 3 - lowercase1 函数:')
    test_lowercase1()
    log('lowercase1 测试通过\n')

    # 测试作业 4 - 处理包含大写字母的字符串转大写
    log('测试作业 4 - uppercase1 函数:')
    test_uppercase1()
    log('uppercase1 测试通过\n')

    # 测试作业 5 - 凯撒加密（右移1位）
    log('测试作业 5 - encode1 函数:')
    test_encode1()
    log('encode1 测试通过\n')

    # 测试作业 6 - 凯撒解密（左移1位）
    log('测试作业 6 - decode1 函数:')
    test_decode1()
    log('decode1 测试通过\n')

    # 测试作业 7 - 凯撒加密（指定位数）
    log('测试作业 7 - encode2 函数:')
    test_encode2()
    log('encode2 测试通过\n')

    # 测试作业 8 - 凯撒解密（指定位数）
    log('测试作业 8 - decode2 函数:')
    test_decode2()
    log('decode2 测试通过\n')

    # 测试作业 9 - 凯撒加密（处理非字母字符）
    log('测试作业 9 - encode3 函数:')
    test_encode3()
    log('encode3 测试通过\n')

    # 测试作业 10 - 凯撒解密（处理非字母字符）
    log('测试作业 10 - decode3 函数:')
    test_decode3()
    log('decode3 测试通过\n')

    # 测试作业 11 - 破译知乎密码
    log('测试作业 11 - decode4 函数:')
    log('破译知乎密码（显示所有可能的解密结果）:')
    decode4(code)
    log('decode4 测试完成\n')

    # 测试作业 12 - 查找字符串位置
    log('测试作业 12 - find2 函数:')
    test_find2()
    log('find2 测试通过\n')

    # 测试作业 13 - 提取两个标记之间的内容
    log('测试作业 13 - find_between 函数:')
    test_find_between()
    log('find_between 测试通过\n')

    # 测试作业 14 - 爬虫获取豆瓣电影评分
    # 注意：需要网络连接，可能会失败
    log('测试作业 14 - ratings 函数（爬虫）:')
    log('注意：此测试需要网络连接，可能会失败')
    try:
        rating_list = ratings()
        log('成功获取电影评分数量:', len(rating_list))
        log('前5个评分:', rating_list[:5])
        log('ratings 测试通过\n')
    except Exception as e:
        log('ratings 测试失败（可能是网络问题）:', str(e), '\n')

    log('========== 所有测试完成 ==========')


if __name__ == "__main__":
    main()
