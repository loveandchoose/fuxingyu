import pandas as pd

# 读取CSV文件并创建DataFrame
df = pd.read_csv('drinks.csv')

# 任务1：找出平均啤酒消耗最多的大陆
continent_beer_mean = df.groupby('continent')['beer_servings'].mean()
max_continent = continent_beer_mean.idxmax()
max_beer_mean = continent_beer_mean.max()
print(f"1. 平均啤酒消耗最多的大陆: {max_continent} ({max_beer_mean:.2f}份)\n")

# 任务2：打印每个大陆红酒消耗的描述性统计值
wine_stats = df.groupby('continent')['wine_servings'].describe()
print("2. 每个大陆红酒消耗的描述性统计:")
print(wine_stats.to_string())
print("\n")

# 任务3：打印每个大陆每种酒类别的消耗平均值
drink_types = ['beer_servings', 'spirit_servings', 'wine_servings']
avg_consumption = df.groupby('continent')[drink_types].mean()
print("3. 每个大陆每种酒类别的平均消耗:")
print(avg_consumption.to_string(float_format="%.1f"))
print("\n")

# 任务4：打印每个大陆每种酒类别的消耗中位数
median_consumption = df.groupby('continent')[drink_types].median()
print("4. 每个大陆每种酒类别的消耗中位数:")
print(median_consumption.to_string(float_format="%.1f"))