import matplotlib.pyplot as plt
import numpy as np

def calculate_normalized_weights(num_atoms, percentages):
    weights = []
    num_atoms_half = num_atoms // 2
    
    for percent in percentages:
        num_left_Au = round(num_atoms * percent / 100)
        
        numerator = num_atoms_half
        denominator = num_atoms_half + 1
        
        # 逐步计算分数
        for i in range(num_atoms_half - 1, num_atoms_half - num_left_Au - 1, -1):
            numerator *= i
            denominator *= (num_atoms - i)
        
        weight = numerator // denominator  # 进行整数除法
        weights.append(weight)
    
    # 找到最接近 50% 的索引
    closest_to_50_index = min(range(len(percentages)), key=lambda index: abs(percentages[index] - 50))
    
    # 计算归一化因子
    if weights[closest_to_50_index] != 0:
        normalization_factor = weights[closest_to_50_index]
    else:
        normalization_factor = 1  # 如果归一化因子为零，则默认为 1
    
    # 对权重进行归一化
    normalized_weights = [weight / normalization_factor for weight in weights]
    
    return normalized_weights

# 对于10^3原子的情况
num_atoms_1 = 10**3
percentages_1 = [45, 47, 49, 49.5, 50.5, 51, 53, 55]
normalized_weights_1 = calculate_normalized_weights(num_atoms_1, percentages_1)

# 对于10^7原子的情况
num_atoms_2 = 10**7
percentages_2 = [49, 49.9, 49.99, 49.999, 50.001, 50.01, 50.1, 51]
normalized_weights_2 = calculate_normalized_weights(num_atoms_2, percentages_2)

# 绘制分布图
plt.figure(figsize=(12, 6))

# 对于10^3原子的情况
plt.subplot(1, 2, 1)
plt.bar(percentages_1, normalized_weights_1, align='center', alpha=0.75)
plt.xlabel('Percentage of Left Au Atoms')
plt.ylabel('Normalized Weight')
plt.title(f'Distribution of Left Au Atoms (Total Atoms: {num_atoms_1})')
plt.grid(True)


# 对于10^7原子的情况
plt.subplot(1, 2, 2)
plt.bar(percentages_2, normalized_weights_2, align='center', alpha=0.75)
plt.xlabel('Percentage of Left Au Atoms')
plt.ylabel('Normalized Weight')
plt.title(f'Distribution of Left Au Atoms (Total Atoms: {num_atoms_2})')
plt.grid(True)

plt.tight_layout()
plt.show()
