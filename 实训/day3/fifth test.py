import pandas as pd

# 1. 读取并合并数据
df_2015 = pd.read_csv('2015年国内主要城市年度数据.csv', encoding='utf-8')
df_2016 = pd.read_csv('2016年国内主要城市年度数据.csv', encoding='utf-8')
df_2017 = pd.read_csv('2017年国内主要城市年度数据.csv', encoding='utf-8')

# 纵向连接三个DataFrame
combined_df = pd.concat([df_2015, df_2016, df_2017], ignore_index=True)

# 2. 按照年份聚合
yearly_stats = combined_df.groupby('年份').agg({
    '国内生产总值': 'sum',
    '第一产业增加值': 'sum',
    '第二产业增加值': 'sum',
    '第三产业增加值': 'sum',
    '社会商品零售总额': 'sum',
    '货物进出口总额': 'sum',
    '年末总人口': 'sum',
    '房地产开发投资额': 'sum'
})

# 3. 计算每年的国内生产总值
gdp_by_year = combined_df.groupby('年份')['国内生产总值'].sum()

# 4. 处理缺省值，填充为0
combined_df_filled = combined_df.fillna(0)

# 打印结果
print("1. 合并后的数据前5行:")
print(combined_df.head().to_string())
print("\n2. 按年份聚合的统计数据:")
print(yearly_stats.to_string(float_format="%.2f"))
print("\n3. 每年的国内生产总值:")
print(gdp_by_year.to_string(float_format="%.2f"))
print("\n4. 处理缺省值后的数据示例(显示有缺省值的列):")
print(combined_df_filled[combined_df.isna().any(axis=1)].head().to_string())