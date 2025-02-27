import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 假设已经加载了数据集到DataFrame df
df = pd.read_csv('health_data.csv')

# 健康趋势分析：分析不同年龄段的BMI分布
plt.figure(figsize=(10, 6))
sns.boxplot(x='Age', y='BMI', data=df)
plt.title('BMI Distribution by Age')
plt.xlabel('Age')
plt.ylabel('BMI')
plt.show()
