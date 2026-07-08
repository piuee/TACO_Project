# ==============================
# TACO 第三次课 示例 1
# 读取本地市场数据 CSV
# ==============================

# pandas 用来处理表格数据
import pandas as pd

# matplotlib 用来画图
import matplotlib.pyplot as plt

# 读取本地 CSV 文件
# parse_dates=["date"] 表示把 date 列转换成日期格式
df = pd.read_csv("market_data_2018_2025.csv", parse_dates=["date"])

# 查看前 5 行数据
print("数据预览：")
print(df.head())

# 查看列名
print("\n数据列名：")
print(df.columns)

# 把 date 列设置为索引
# 这样后面按照日期筛选、画图会更方便
df = df.set_index("date")

# 再次查看数据
print("\n设置日期索引后的数据：")
print(df.head())