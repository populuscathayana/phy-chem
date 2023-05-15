import matplotlib.pyplot as plt
import numpy as np

# 数据集1
percentages_1 = [0.45, 0.47, 0.49, 0.495, 0.5, 0.505, 0.51, 0.53, 0.55]
product_1 = [0.0813320334147723, 0.40561678859448674, 0.9046501591282005, 0.9840956175298805, 1, 0.9840956175298805, 0.9046501591282005, 0.40561678859448674, 0.0813320334147723]

# 绘制数据集1的柱状图
plt.figure(figsize=(8, 4))
plt.bar(range(len(percentages_1)), product_1, width=0.6, align='center', alpha=0.75)  # 调整柱状图的宽度
plt.xlabel('Percentage of Left Au Atoms')
plt.ylabel('Product')
plt.title('Product vs Percentage of Left Au Atoms')
plt.grid(True)

# 设置 x 轴刻度标签
plt.xticks(range(len(percentages_1)), ['45%', '47%', '49%', '49.5%', '50%', '50.5%', '51%', '53%', '55%'])

plt.show()

# 数据集2
percentages_2 = [0.49, 0.499, 0.4999, 0.49999, 0.5, 0.50001, 0.5001, 0.501, 0.51]
product_2 = [1.2e-322, 4.5399536297454e-05, 0.9051990446898273, 0.9990004996335086, 1, 0.9990400608445181, 0.9051990446898273, 4.5399536297454e-05, 1.2e-322]
# 绘制数据集2的柱状图
plt.figure(figsize=(8, 4))
plt.bar(range(len(percentages_2)), product_2, width=0.6, align='center', alpha=0.75)  # 调整柱状图的宽度
plt.xlabel('Percentage of Left Au Atoms')
plt.ylabel('Product')
plt.title('Product vs Percentage of Left Au Atoms')
plt.grid(True)

# 设置 x 轴刻度标签
plt.xticks(range(len(percentages_2)), ['49%', '49.9%', '49.99%', '49.999%', '50%', '50.001%', '50.01%', '50.1%', '51%'])

plt.show()
