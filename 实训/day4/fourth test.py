import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
df = pd.read_csv('train.csv')

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体显示中文
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 处理缺失值（Age列）
df['Age'] = df['Age'].fillna(df['Age'].median())  # 用中位数填充缺失值

# 将年龄分组（每10岁一组）
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
labels = ['0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80-90']
df['AgeGroup'] = pd.cut(df['Age'], bins=bins, labels=labels)

# 计算每个Pclass和AgeGroup的生还率
survival_rate = df.groupby(['Pclass', 'AgeGroup'])['Survived'].mean().unstack() * 100

# 绘制分组柱状图
plt.figure(figsize=(12, 6))
survival_rate.plot(kind='bar', width=0.8, alpha=0.8, colormap='viridis')

# 设置图表标题和标签
plt.title('不同乘客等级和年龄组的生还率 (%)', fontsize=14)
plt.xlabel('乘客等级 (Pclass)', fontsize=12)
plt.ylabel('生还率 (%)', fontsize=12)
plt.xticks(rotation=0)
plt.ylim(0, 100)  # 设置y轴范围
plt.legend(title='年龄组', bbox_to_anchor=(1.05, 1), loc='upper left')  # 图例放在右侧

# 显示图表
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()