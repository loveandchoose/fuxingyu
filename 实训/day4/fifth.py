import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 读取数据
df = pd.read_csv('train.csv')


# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 数据预处理
# 处理Age缺失值（用中位数填充）
df['Age'] = df['Age'].fillna(df['Age'].median())

# 定义年龄分组
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80]
labels = ['0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80']
df['AgeGroup'] = pd.cut(df['Age'], bins=bins, labels=labels)

# 计算各分组的生还率
result = df.groupby(['Sex', 'AgeGroup'])['Survived'].agg(
    Total='count',
    Survived='sum'
).reset_index()
result['Survival_Rate'] = result['Survived'] / result['Total'] * 100

# 可视化
plt.figure(figsize=(14, 7))
sns.barplot(
    x='AgeGroup',
    y='Survival_Rate',
    hue='Sex',
    data=result,
    palette={'female': 'pink', 'male': 'lightblue'}
)

# 添加标签
for index, row in result.iterrows():
    plt.text(
        index % len(labels),
        row['Survival_Rate'] + 2,
        f"{row['Survival_Rate']:.1f}%",
        ha='center',
        color='black'
    )

# 图表装饰
plt.title('不同性别和年龄组的生还率对比', fontsize=16, pad=20)
plt.xlabel('年龄组', fontsize=12)
plt.ylabel('生还率 (%)', fontsize=12)
plt.ylim(0, 110)
plt.legend(title='性别', loc='upper right')

plt.tight_layout()
plt.show()

# 输出统计表格
print("\n=== 详细统计数据 ===")
print(result.to_string(index=False))