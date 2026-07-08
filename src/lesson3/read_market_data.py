from pathlib import Path

import pandas as pd


# 用脚本位置反推出项目根目录，避免写死电脑上的绝对路径。
PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_FILE = PROJECT_ROOT / "data" / "market_data_2018_2025.csv"
REQUIRED_COLUMNS = ["date", "USO_Close", "GLD_Close", "SPY_Close", "QQQ_Close"]


def main():
    """读取本地市场数据，并打印基础检查信息。"""
    if not DATA_FILE.exists():
        print(f"没有找到市场数据文件：{DATA_FILE}")
        print("请确认 data/market_data_2018_2025.csv 已经放在项目 data 文件夹中。")
        return

    try:
        # parse_dates 会把 date 列从字符串转换成 pandas 的日期类型。
        df = pd.read_csv(DATA_FILE, parse_dates=["date"])
    except ValueError as exc:
        print("读取 CSV 时没有找到 date 列，无法使用 parse_dates=['date']。")
        print(f"错误信息：{exc}")
        return

    missing_columns = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing_columns:
        print("市场数据列名不匹配。")
        print(f"当前实际列名：{list(df.columns)}")
        print(f"期望列名：{REQUIRED_COLUMNS}")
        print(f"缺失列名：{missing_columns}")
        return

    print("数据预览：")
    print(df.head())
    print("\n列名：")
    print(list(df.columns))
    print("\n数据形状：")
    print(df.shape)

    # 把日期设置为索引，后面画时间序列图会更方便。
    df = df.set_index("date")
    print("\n设置 date 为索引后的前几行：")
    print(df.head())


if __name__ == "__main__":
    main()
