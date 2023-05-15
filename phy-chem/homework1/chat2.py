import matplotlib.pyplot as plt

S = 10000000

def product_of_numbers(*args, d):
    result = 1
    for num in args:
        result *= (S/4 - num) / (S/4 + int((S*abs(1-2*d))/4) - num)
    return result

p = [0,0.1,0.2,0.3,0.4,0.45,0.47,0.48,0.49,0.499,0.4999,0.49995,0.49999,0.5,0.50001,0.50005,0.5001,0.501,0.51,0.52,0.53,0.55,0.6,0.7,0.8,0.9,1]

result = {}
for i in p:
    numbers = [num for num in range(1, int((S*abs(1-2*i)/4))+1)]
    result[i] = product_of_numbers(*numbers, d=i)

# 绘制折线图
plt.figure(figsize=(10, 6))
plt.plot(list(result.keys()), list(result.values()), marker='o', linestyle='-', markersize=4)
plt.xlabel('Percentage of Left Au Atoms')
plt.ylabel('Product')
plt.title('Product vs Percentage of Left Au Atoms')
plt.grid(True)
plt.show()