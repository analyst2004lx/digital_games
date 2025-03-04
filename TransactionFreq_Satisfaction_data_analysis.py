import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 读取保存的数据集
file_path = 'TransactionFreq_Satisfaction_data.csv'
data = pd.read_csv(file_path)

# 数据整理：检查并确保没有缺失值
data.dropna(inplace=True)

# 关联分析：观察高频交易客户的满意度分布
# 假定“高频交易”为高于平均交易频率的客户
average_freq = data['TransactionFreq'].mean()
high_freq_data = data[data['TransactionFreq'] > average_freq]

# 绘制满意度分布图
plt.figure(figsize=(8, 6))
sns.countplot(x='Satisfaction', data=high_freq_data)
plt.title('Satisfaction Levels among High Frequency Customers')
plt.xlabel('Satisfaction Level')
plt.ylabel('Count')
plt.show()
