# 1. 列表推导式输出偶数
numbers = [x for x in range(1, 101)]
even_numbers = [x for x in numbers if x % 2 == 0]
print("1-100的所有偶数：")
print(even_numbers)

# 2. 删除列表重复元素
def remove_duplicates(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

original_list = [3, 2, 1, 2, 4, 3, 5, 1]
print("\n原始列表：", original_list)
print("去重后列表：", remove_duplicates(original_list))

# 3. 合并列表为字典
keys = ["a", "b", "c"]
values = [1, 2, 3]
print("\n合并后的字典：", dict(zip(keys, values)))

# 4. 元组解包
student = ("张三", 20, 89.5)
name, age, score = student
print("\n学生信息：")
print(f"姓名：{name}\n年龄：{age}\n成绩：{score}")