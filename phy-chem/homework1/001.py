import matplotlib.pyplot as plt
import numpy as np

# 定义合金原子数量
num_Au = 15
num_Ag = 15

# 计算所有可能的微观状态
microstates = []
for i in range(num_Au + 1):
    for j in range(num_Au + 1):
        if i + j == num_Au:
            microstates.append((i, j))

# 计算每个微观状态的权重（组合数）
weights = [np.math.comb(num_Au, i) * np.math.comb(num_Ag, j) for i, j in microstates]

# 计算每个微观状态出现的概率
total_weight = sum(weights)
probabilities = [weight / total_weight for weight in weights]

# 提取左半边Au原子的数量和对应的百分比
left_Au_atoms = [state[0] for state in microstates]
left_Au_percentage = [left_Au / num_Au * 100 for left_Au in left_Au_atoms]

# 绘制直方图并标注数据点的y轴值和权重
plt.bar(left_Au_percentage, probabilities, align='center', alpha=0.75)
plt.xlabel('Percentage of Left Au Atoms')
plt.ylabel('Probability')
plt.title('Probability Distribution of Macro States')
plt.xticks(left_Au_percentage)

# 标注数据点的y轴值和权重
for x, y, weight in zip(left_Au_percentage, probabilities, weights):
    plt.text(x, y, f'{y:.3f}\n{weight}', ha='center', va='bottom')

plt.grid(True)
plt.show()
