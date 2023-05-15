import matplotlib.pyplot as plt

S = 1000

def product_of_numbers(*args, d):
    result = 1
    for num in args:
        result *= (S/4 - num) / (S/4 + int((S*abs(1-2*d))/4) - num)
    return result

p = [0 + 0.00001 * i for i in range(100000)]

result = {}
for i in p:
    numbers = [num  for num in range(1, int((S*abs(1-2*i)/4))+1)]
    result[i] = product_of_numbers(*numbers, d=i)

# 绘制折线图
plt.figure(figsize=(10, 6))
plt.plot(list(result.keys()), list(result.values()), marker='o', linestyle='-', markersize=4)
plt.xlabel('Percentage of Left Au Atoms')
plt.ylabel('Product')
plt.title('Product vs Percentage of Left Au Atoms')
plt.grid(True)
plt.show()
