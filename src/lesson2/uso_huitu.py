# ==============================
# TACO 第三次课 示例 2
# 绘制 USO 收盘价折线图
# ==============================

import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
df = pd.read_csv("market_data_2018_2025.csv", parse_dates=["date"])

# 设置日期索引
df = df.set_index("date")

# 创建图表
plt.figure(figsize=(10, 5))

# 绘制 USO 收盘价
plt.plot(df.index, df["USO_Close"])

# 设置图表标题
plt.title("USO Close Price")

# 设置横轴和纵轴名称
plt.xlabel("Date")
plt.ylabel("USO Close Price")

# 旋转日期文字，防止挤在一起
plt.xticks(rotation=30)

# 自动调整布局
plt.tight_layout()

# 显示图表
plt.show()