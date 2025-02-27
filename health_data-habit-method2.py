import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 假设已经加载了数据集到DataFrame df
df = pd.read_csv('health_data.csv')

# 生活习惯与健康状况的关联：分析运动习惯和饮食习惯与BMI的关系
# 假设运动习惯和饮食习惯已经是二进制编码，0代表不良习惯，1代表良好习惯

# 可视化分析
plt.figure(figsize=(12, 6))
sns.barplot(x='ExerciseHabit', y='BMI', hue='DietHabit', data=df, ci=None)
plt.title('BMI by Exercise and Diet Habits')
plt.xlabel('Exercise Habit (0: Poor, 1: Good)')
plt.ylabel('BMI')
plt.legend(title='Diet Habit (0: Poor, 1: Good)')
plt.show()
