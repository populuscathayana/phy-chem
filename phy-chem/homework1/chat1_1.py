import matplotlib.pyplot as plt

S = 6.022*(10**23)

def product_of_numbers(*args, d):
    result = 1
    for num in args:
        result *= (S/4 - num) / (S/4 + int((S*abs(1-2*d))/4) - num)
    return result

p = [0.5-10**6/(2*6.022*(10**23))]

result = {}
for i in p:
    numbers = [num  for num in range(1, int((S*abs(1-2*i)/4))+1)]
    result[i] = product_of_numbers(*numbers, d=i)
    print(result[i])

# 绘制折线图
plt.figure(figsize=(10, 6))
plt.plot(list(result.keys()), list(result.values()), marker='o', linestyle='-', markersize=4)
plt.xlabel('Percentage of Left Au Atoms')
plt.ylabel('Product')
plt.title('Product vs Percentage of Left Au Atoms')
plt.grid(True)
plt.show()
