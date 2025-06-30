import pandas as pd
import numpy as np

# 1. 创建包含指定数据的CSV文件
data = {
    'Student_ID': [101, 102, 103, 104, 105],
    'Name': ['Alice', 'Bob', None, 'David', 'Eva'],
    'Score': [85, 92, 78, np.nan, 88],
    'Grade': ['A', 'A', 'B', None, 'B+']
}

df = pd.DataFrame(data)
df.to_csv('students.csv', index=False)
print("1. students.csv 文件已创建\n")

# 2. 读取CSV文件并打印前3行
students_df = pd.read_csv('students.csv')
print("2. 原始数据前3行:")
print(students_df.head(3).to_string())
print()

# 3. 处理缺失值
# 计算Score列的平均分(忽略NaN)
score_mean = students_df['Score'].mean()

# 填充缺失值
students_df['Score'].fillna(score_mean, inplace=True)
students_df['Name'].fillna('Unknown', inplace=True)
students_df['Grade'].fillna('Unknown', inplace=True)  # 额外处理Grade列的缺失值

print("3. 处理后的数据:")
print(students_df.to_string())
print()

# 4. 保存处理后的DataFrame为新CSV文件
students_df.to_csv('students_cleaned.csv', index=False)
print("4. 已保存处理后的数据到 students_cleaned.csv")