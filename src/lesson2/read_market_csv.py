# ==============================
# TACO 第2次课：读取本地市场数据 CSV
# 文件名：read_market_csv.py
# ==============================

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# 当前文件路径：
# D:\TACO\TACO_Project\src\lesson2\read_market_csv.py
#
# parents[0] = lesson2
# parents[1] = src
# parents[2] = TACO_Project
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# data 文件夹
DATA_DIR = PROJECT_ROOT / "data"

# 标准市场数据文件路径
MARKET_FILE = DATA_DIR / "market_data_2018_2025.csv"

# 市场数据必须包含这些列
REQUIRED_COLUMNS = [
    "date",
    "USO_Close",
    "GLD_Close",
    "SPY_Close",
    "QQQ_Close"
]


def find_market_file():
    """
    寻找市场数据文件。
    优先找 data/market_data_2018_2025.csv。
    如果找不到，就在项目目录中搜索其他 CSV，
    找到包含市场数据列的文件。
    """

    # 1. 优先使用标准路径
    if MARKET_FILE.exists():
        return MARKET_FILE

    print("没有在 data 文件夹中找到 market_data_2018_2025.csv。")
    print("开始在项目中自动搜索可能的市场数据 CSV 文件...")

    # 2. 在整个项目中搜索 CSV 文件
    csv_files = list(PROJECT_ROOT.rglob("*.csv"))

    for csv_file in csv_files:
        try:
            # 只读取前 5 行，用来检查列名
            temp_df = pd.read_csv(csv_file, nrows=5)

            # 判断这个 CSV 是否包含市场数据列
            if all(col in temp_df.columns for col in REQUIRED_COLUMNS):
                print("找到市场数据文件：", csv_file)
                return csv_file

        except Exception:
            # 如果某个 CSV 读不了，就跳过
            continue

    # 3. 如果都找不到，返回 None
    return None


# 找到市场数据文件
file_path = find_market_file()

if file_path is None:
    print("\n没有找到可用的市场数据文件。")
    print("请确认你有一个 CSV 文件，列名包含：")
    print(REQUIRED_COLUMNS)
    print("\n建议放到：")
    print(MARKET_FILE)

else:
    # 读取 CSV
    df = pd.read_csv(file_path)

    print("\n成功读取市场数据！")
    print("文件路径：", file_path)
    print("=" * 60)

    # 查看前 5 行
    print("数据预览：")
    print(df.head())

    # 查看列名
    print("\n数据列名：")
    print(df.columns)

    # 检查列是否完整
    missing_columns = []

    for col in REQUIRED_COLUMNS:
        if col not in df.columns:
            missing_columns.append(col)

    if len(missing_columns) > 0:
        print("\n缺少以下列，无法继续分析：")
        print(missing_columns)

    else:
        # 把 date 列转换成日期格式
        df["date"] = pd.to_datetime(df["date"])

        # 计算 USO 每日涨跌幅
        # pct_change() 表示计算相邻两天之间的百分比变化
        df["USO_Change"] = df["USO_Close"].pct_change() * 100

        print("\nUSO 最近 10 天数据：")
        print(df[["date", "USO_Close", "USO_Change"]].tail(10))

        # 保存 USO 涨跌幅结果到 data 文件夹
        DATA_DIR.mkdir(exist_ok=True)

        output_path = DATA_DIR / "uso_daily_change.csv"

        df[["date", "USO_Close", "USO_Change"]].to_csv(
            output_path,
            index=False,
            encoding="utf-8-sig"
        )

        print("\nUSO 涨跌幅结果已保存到：")
        print(output_path)

        # 画 USO 收盘价折线图
        plt.figure(figsize=(10, 5))

        plt.plot(df["date"], df["USO_Close"])

        plt.title("USO Close Price")
        plt.xlabel("Date")
        plt.ylabel("USO Close Price")

        plt.xticks(rotation=30)
        plt.tight_layout()
        plt.show()