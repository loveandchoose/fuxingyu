import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
df = pd.read_csv('train.csv')

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 处理缺失值（Age列用中位数填充）
df['Age'] = df['Age'].fillna(df['Age'].median())

# 定义年龄分组（每10岁一组）
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80]
labels = ['0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80']
df['AgeGroup'] = pd.cut(df['Age'], bins=bins, labels=labels)

# 计算各年龄组的总人数和生还率
age_stats = df.groupby('AgeGroup').agg(
    Total=('Survived', 'count'),
    Survived_Rate=('Survived', 'mean')
)
age_stats['Survived_Rate'] *= 100  # 转换为百分比

# 创建画布和双坐标轴
fig, ax1 = plt.subplots(figsize=(12, 6))

# 直方图：各年龄组人数（左轴）
ax1.bar(
    age_stats.index,
    age_stats['Total'],
    color='skyblue',
    alpha=0.7,
    label='乘客人数'
)
ax1.set_xlabel('年龄组', fontsize=12)
ax1.set_ylabel('乘客人数', fontsize=12)
ax1.tick_params(axis='y')
ax1.grid(axis='y', linestyle='--', alpha=0.5)

# 折线图：生还率（右轴）
ax2 = ax1.twinx()
ax2.plot(
    age_stats.index,
    age_stats['Survived_Rate'],
    color='red',
    marker='o',
    linewidth=2,
    label='生还率'
)
ax2.set_ylabel('生还率 (%)', fontsize=12)
ax2.set_ylim(0, 100)  # 固定y轴范围
ax2.tick_params(axis='y')

# 添加标题和图例
plt.title('年龄对生还率的影响（人数分布 vs 生还率）', fontsize=14, pad=20)
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')

# 在折线上标注生还率
for x, y in zip(age_stats.index, age_stats['Survived_Rate']):
    ax2.text(x, y + 2, f'{y:.1f}%', ha='center', color='red')

plt.tight_layout()
plt.show()