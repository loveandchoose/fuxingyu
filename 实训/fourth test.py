# 任务1
s1 = "Python is a powerful programming language"
s2 = " Let's learn together"

print("=== 任务1 ===")
print("(1) 最后一个单词:", s1.split()[-1])
print("(2) 重复输出3次:\n" + (s1 + s2 + "\n") * 3, end="")
print("(3) 以p/P开头的单词:", [w for w in s1.split() if w[0].lower() == 'p'])

# 任务2
s3 = " Hello, World! This is a test string. "
print("\n=== 任务2 ===")
trimmed = s3.strip()
print("(1) 去除前后空格:", trimmed)
print("(2) 转换为大写:", trimmed.upper())
print("(3) 'test'的起始下标:", trimmed.find("test"))
print("(4) 替换后的字符串:", trimmed.replace("test", "practice"))
print("(5) 分割并连接:", "-".join(trimmed.split()))