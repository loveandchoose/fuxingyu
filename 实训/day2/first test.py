#判断回文数
def is_palindrome(num):
    """判断一个数是否为回文数"""
    # 将数字转换为字符串
    num_str = str(num)
    return num_str == num_str[::-1]

# 测试
print(is_palindrome(121))  # True
print(is_palindrome(123))  # False


#计算任意数量参数的平均值
def calculate_average(*args):
    """计算任意数量参数的平均值"""
    return sum(args) / len(args) if args else 0

print(calculate_average(1, 2, 3, 4))  # 2.5
print(calculate_average(10, 20))     # 15.0

#返回最长字符串
def find_longest_string(*strings):
    """返回任意多个字符串中最长的那个"""
    return max(strings, key=len, default=None)

# 测试
print(find_longest_string("apple", "banana", "cherry"))  # "banana"
print(find_longest_string("a", "ab", "abc"))            # "abc"


#创建矩形计算模块
def area(length, width):
    """计算矩形面积"""
    return length * width

def perimeter(length, width):
    """计算矩形周长"""
    return 2 * (length + width)

from bag import area, perimeter

# 使用模块中的函数
print("面积:", area(5, 3))      # 15
print("周长:", perimeter(5, 3))  # 16