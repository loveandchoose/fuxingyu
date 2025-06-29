# 定义Car类
class Car:
    def __init__(self, brand, speed=0):
        """初始化汽车品牌和速度"""
        self.brand = brand
        self.speed = speed

    def accelerate(self, m):
        """加速m次，每次速度增加10"""
        for _ in range(m):
            self.speed += 10
        return self.speed

    def brake(self, n):
        """刹车n次，每次速度减少10（不低于0）"""
        for _ in range(n):
            self.speed = max(0, self.speed - 10)  # 确保速度不低于0
        return self.speed

    def __str__(self):
        """打印当前状态"""
        return f"{self.brand}当前速度：{self.speed}"

#创建Car实例并测试
# 创建实例
my_car = Car("Toyota", 30)

# 测试加速和刹车
print(my_car)  # 初始状态
my_car.accelerate(3)
print(my_car)  # 加速3次后
my_car.brake(2)
print(my_car)  # 刹车2次后

#定义ElectricCar子类
class ElectricCar(Car):
    def __init__(self, brand, speed=0, battery=50):
        """初始化电动车属性"""
        super().__init__(brand, speed)  # 调用父类初始化
        self.battery = battery

    def charge(self):
        """充电（电量增加20，不超过100）"""
        self.battery = min(100, self.battery + 20)
        return self.battery

    def __str__(self):
        """扩展状态显示"""
        return f"{super().__str__()}，剩余电量：{self.battery}%"

#使用ElectricCar子类
# 创建电动车实例
tesla = ElectricCar("Tesla", 20, 60)

# 测试继承的方法和新增方法
print("\n" + str(tesla))  # 初始状态
tesla.accelerate(2)
tesla.charge()
print(tesla)  # 加速2次+充电后
tesla.brake(1)
tesla.charge()
print(tesla)  # 刹车1次+再次充电后