import matplotlib.pyplot as plt

temperatures = [22, 24, 19, 24, 17, 18, 23, 24, 25, 22, 20, 19, 23, 24, 25, 26, 27, 22, 21, 20, 23, 24, 25, 26, 27, 28, 29, 30, 22, 21]

average_temp = sum(temperatures) / len(temperatures)
print(f"平均最高气温: {average_temp:.2f}°C")

# 使用sorted函数和切片
hottest_days = sorted(temperatures, reverse=True)[:3]
coldest_days = sorted(temperatures)[:3]
print(f"最热的三天气温: {hottest_days}°C")
print(f"最冷的三天气温: {coldest_days}°C")


# 使用sorted函数和切片
hottest_days = sorted(temperatures, reverse=True)[:3]
coldest_days = sorted(temperatures)[:3]
print(f"最热的三天气温: {hottest_days}°C")
print(f"最冷的三天气温: {coldest_days}°C")



plt.plot(temperatures)
plt.title('Daily Maximum Temperatures Over a Year')
plt.xlabel('Day')
plt.ylabel('Temperature (°C)')
plt.show()
