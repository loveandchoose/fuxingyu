# 1. 输出1-100的素数
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print("1-100之间的素数：")
for num in range(1, 101):
    if is_prime(num):
        print(num, end=" ")

# 2. 斐波那契数列前20项
def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib[:n]

print("\n\n斐波那契数列前20项：")
print(fibonacci(20))

# 3. 计算特定条件的和
total = 0
num = 1
while num <= 10000:
    if (num % 3 == 0 or num % 5 == 0) and num % 15 != 0:
        total += num
    num += 1

print("\n1-10000之间满足条件的数的和：", total)