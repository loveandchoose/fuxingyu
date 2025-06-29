# 1. 判断变量数据类型
x = 10
y = "10"
z = True
print(f"x的类型是: {type(x)}")  # <class 'int'>
print(f"y的类型是: {type(y)}")  # <class 'str'>
print(f"z的类型是: {type(z)}")  # <class 'bool'>

# 2. 计算圆的面积
radius = float(input("请输入圆的半径: "))
pi = 3.14
area = pi * radius ** 2
print(f"半径为 {radius} 的圆的面积是: {area}")

# 3. 类型转换观察
num_str = "3.14"
num_float = float(num_str)  # 转换为浮点数
num_int = int(num_float)    # 浮点数转换为整数(会截断小数部分)
print(f"字符串 '{num_str}' 转换为浮点数: {num_float}")  # 3.14
print(f"浮点数 {num_float} 转换为整数: {num_int}")      # 3 (小数部分丢失)