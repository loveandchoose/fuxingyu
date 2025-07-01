import numpy as np
import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 微软雅黑
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 数据准备
countries = ['挪威', '德国', '中国', '美国', '瑞典']
gold_medal = np.array([16, 12, 9, 8, 8])
silver_medal = np.array([8, 10, 4, 10, 5])
bronze_medal = np.array([13, 5, 2, 7, 5])

# 创建图表
plt.figure(figsize=(10, 6))
x = np.arange(len(countries))

# 绘制柱状图
plt.bar(x - 0.2, gold_medal, width=0.2, color='gold', label='金牌')
plt.bar(x, silver_medal, width=0.2, color='silver', label='银牌')
plt.bar(x + 0.2, bronze_medal, width=0.2, color='saddlebrown', label='铜牌')

# 设置X轴标签
plt.xticks(x, countries)
plt.xlabel('国家')
plt.ylabel('奖牌数量')
plt.title('各国奥运奖牌分布')

# 添加数据标签
for i in x:
    plt.text(x[i] - 0.2, gold_medal[i], gold_medal[i],
             va='bottom', ha='center', fontsize=8)
    plt.text(x[i], silver_medal[i], silver_medal[i],
             va='bottom', ha='center', fontsize=8)
    plt.text(x[i] + 0.2, bronze_medal[i], bronze_medal[i],
             va='bottom', ha='center', fontsize=8)

# 添加图例
plt.legend()

# 显示图表
plt.tight_layout()
plt.show()