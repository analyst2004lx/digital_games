import pandas as pd
import matplotlib.pyplot as plt

# 读取数据集
file_path = 'sales_trend_data.csv'
df = pd.read_csv(file_path)

# 确保日期列是日期格式，并设置为索引
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# 分别对每个类别按月聚合销售数据
monthly_sales = df.groupby('Category').resample('M').sum()

# 绘制每个类别的月销售趋势图以展示季节性变化
plt.figure(figsize=(14, 7))
for category, group_data in monthly_sales.groupby('Category'):
    group_data['Sales'].plot(label=category)

plt.title('Monthly Sales Trend by Category')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.legend(title='Category')
plt.grid(True)
plt.show()
