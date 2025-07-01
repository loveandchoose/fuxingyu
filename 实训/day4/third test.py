import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
df = pd.read_csv('train.csv')

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体显示中文
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 计算每个乘客等级的生存率
survival_rate = df.groupby('Pclass')['Survived'].mean() * 100

# 绘制直方图
plt.figure(figsize=(10, 6))
survival_rate.plot(kind='bar', color=['gold', 'silver', 'brown'], alpha=0.7)

# 设置图表标题和标签
plt.title('不同乘客等级的生存率', fontsize=14)
plt.xlabel('乘客等级', fontsize=12)
plt.ylabel('生存率 (%)', fontsize=12)
plt.xticks(rotation=0)  # 保持x轴标签水平
plt.ylim(0, 100)  # 设置y轴范围

# 在柱子上添加百分比标签
for index, value in enumerate(survival_rate):
    plt.text(index, value + 2, f'{value:.1f}%', ha='center', fontsize=12)

# 显示图表
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()