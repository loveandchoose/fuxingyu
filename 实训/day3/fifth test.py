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


# 5. 计算每个城市GDP年均增长率并找出最高和最低的五个城市
def calculate_growth_rate(df):
    cities = df['地区'].unique()
    growth_rates = []

    for city in cities:
        city_data = df[df['地区'] == city].sort_values('年份')
        if len(city_data) >= 2:  # 至少有两年数据
            gdp_2015 = city_data[city_data['年份'] == 2015]['国内生产总值'].values
            gdp_2017 = city_data[city_data['年份'] == 2017]['国内生产总值'].values
            if len(gdp_2015) > 0 and len(gdp_2017) > 0:
                cagr = ((gdp_2017[0] / gdp_2015[0]) ** (1 / 2) - 1) * 100
                growth_rates.append({'城市': city, '年均增长率(%)': cagr})

    growth_df = pd.DataFrame(growth_rates)
    top5 = growth_df.nlargest(5, '年均增长率(%)')
    bottom5 = growth_df.nsmallest(5, '年均增长率(%)')
    return growth_df, top5, bottom5


growth_df, top5_cities, bottom5_cities = calculate_growth_rate(combined_df_filled)


# 6. 对医院、卫生院数进行归一化处理并按年份比较
def normalize_hospital_data(df):
    # Min-Max标准化
    df['医院、卫生院数_归一化'] = df.groupby('年份')['医院、卫生院数'].transform(
        lambda x: (x - x.min()) / (x.max() - x.min()))
    return df


combined_df_normalized = normalize_hospital_data(combined_df_filled)


# 7. 提取四个一线城市的数据并保存为新的CSV
def extract_top_cities_data(df):
    top_cities = ['北京', '上海', '广州', '深圳']
    filtered = df[df['地区'].isin(top_cities)][['地区', '年份', '国内生产总值', '社会商品零售总额']]
    filtered.to_csv('一线城市GDP和消费数据.csv', index=False, encoding='utf-8-sig')
    return filtered


top_cities_data = extract_top_cities_data(combined_df_filled)

# 打印所有结果
print("1. 合并后的数据前5行:")
print(combined_df.head().to_string())
print("\n2. 按年份聚合的统计数据:")
print(yearly_stats.to_string(float_format="%.2f"))
print("\n3. 每年的国内生产总值:")
print(gdp_by_year.to_string(float_format="%.2f"))
print("\n4. 处理缺省值后的数据示例(显示有缺省值的列):")
print(combined_df_filled[combined_df.isna().any(axis=1)].head().to_string())
print("\n5. GDP年均增长率最高的5个城市:")
print(top5_cities.to_string(index=False))
print("\n5. GDP年均增长率最低的5个城市:")
print(bottom5_cities.to_string(index=False))
print("\n6. 归一化后的医院数据示例:")
print(combined_df_normalized[['地区', '年份', '医院、卫生院数', '医院、卫生院数_归一化']].head(10).to_string(
    float_format="%.4f"))
print("\n7. 四个一线城市数据已保存到: 一线城市GDP和消费数据.csv")
print(top_cities_data.to_string(float_format="%.2f"))