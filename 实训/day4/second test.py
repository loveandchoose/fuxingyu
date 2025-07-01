import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为黑体
plt.rcParams['axes.unicode_minus'] = False    # 解决负号 '-' 显示为方块的问题
# 读取数据
df_2015 = pd.read_csv(r'D:\Games\pythonProject3\实训\day3\2015年国内主要城市年度数据.csv', encoding='utf-8')
df_2016 = pd.read_csv(r'D:\Games\pythonProject3\实训\day3\2016年国内主要城市年度数据.csv', encoding='utf-8')
df_2017 = pd.read_csv(r'D:\Games\pythonProject3\实训\day3\2017年国内主要城市年度数据.csv', encoding='utf-8')

# 提取所需数据
gdp_2015 = df_2015[['地区', '国内生产总值']].rename(columns={'国内生产总值': '2015年'})
gdp_2016 = df_2016[['地区', '国内生产总值']].rename(columns={'国内生产总值': '2016年'})
gdp_2017 = df_2017[['地区', '国内生产总值']].rename(columns={'国内生产总值': '2017年'})

# 合并数据
gdp_all = gdp_2015.merge(gdp_2016, on='地区').merge(gdp_2017, on='地区')

# 设置绘图参数
plt.figure(figsize=(15, 8))
x = np.arange(len(gdp_all['地区']))
width = 0.25

# 绘制直方图
plt.bar(x - width, gdp_all['2015年'] / 1e4, width, label='2015年')
plt.bar(x, gdp_all['2016年'] / 1e4, width, label='2016年')
plt.bar(x + width, gdp_all['2017年'] / 1e4, width, label='2017年')

# 设置图表标题和标签
plt.title('2015-2017年各城市国内生产总值（单位：万亿元）', fontsize=14)
plt.xlabel('城市', fontsize=12)
plt.ylabel('国内生产总值（万亿元）', fontsize=12)
plt.xticks(x, gdp_all['地区'], rotation=90)
plt.legend()

# 调整布局
plt.tight_layout()
plt.show()
# 提取2015年数据并排序
gdp_2015_sorted = df_2015[['地区', '国内生产总值']].sort_values('国内生产总值', ascending=False)

# 设置绘图参数
plt.figure(figsize=(12, 12))

# 绘制饼状图
plt.pie(gdp_2015_sorted['国内生产总值'],
        labels=gdp_2015_sorted['地区'],
        autopct='%1.1f%%',
        startangle=90,
        textprops={'fontsize': 8})

# 设置图表标题
plt.title('2015年各城市国内生产总值占比', fontsize=14)

# 调整布局
plt.tight_layout()
plt.show()
