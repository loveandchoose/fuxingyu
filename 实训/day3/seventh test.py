import numpy as np
import matplotlib.pyplot as plt
# 日期
year = np.arange(2000,2021).astype(np.str_)
month = np.random.randint(1,13,size = 20).astype(np.str_)
day = np.random.randint(1,31,size = 20).astype(np.str_)
date = np.array([])
for i in range(20):
    a = np.array([year[i],month[i],day[i]])
    b = ['/'.join(a)]  # 组合年月日
    date = np.append(date,b)

# 随机出销量
sales = np.random.randint(500,2000,size=len(date))

# 绘制图形
plt.xticks(range(0,len(date),2),['日期:%s'%i for i in date][::2],rotation=45, color='red')
plt.plot(date,sales)
plt.show()