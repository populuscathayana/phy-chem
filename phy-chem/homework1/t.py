import numpy as np
import matplotlib.pyplot as plt

# 定义常数
B = 1.93  # cm^-1
k = 0.69503476  # cm^-1 / K
Temperatures = [3, 10, 20, 30, 40, 50, 60, 80, 120, 200, 300, 500, 700]  # K
J_values = np.arange(0, 15)

# 定义能量和简并度函数
E_J = lambda J: B * J * (J + 1)
g_J = lambda J: 2 * J + 1

# 初始化图像
plt.figure(figsize=(10, 6))

# 对于每个温度，计算并绘制P(J)
for T in Temperatures:
    # 计算配分函数
    Q_T = np.sum(g_J(J_values) * np.exp(-E_J(J_values) / (k * T)))

    # 计算每个J值的概率
    P_J = g_J(J_values) * np.exp(-E_J(J_values) / (k * T)) / Q_T

    # 绘制P(J) vs J
    plt.plot(J_values, P_J, label=f'T={T} K')

# 设定图像标题和标签
plt.title('Rotational Energy Level Distributions for CO')
plt.xlabel('Rotational Quantum Number (J)')
plt.ylabel('Probability')
plt.legend()

# 显示图像
plt.show()

