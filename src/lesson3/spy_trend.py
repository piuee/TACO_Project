from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


# 用 pathlib 定位项目路径，代码换电脑也能运行。
PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_FILE = PROJECT_ROOT / "data" / "market_data_2018_2025.csv"
OUTPUT_FILE = PROJECT_ROOT / "data" / "spy_trend.png"
REQUIRED_COLUMNS = ["date", "SPY_Close"]


def load_spy_data():
    """读取 SPY 数据，缺文件或缺列时返回 None。"""
    if not DATA_FILE.exists():
        print(f"没有找到市场数据文件：{DATA_FILE}")
        print("请先确认 data/market_data_2018_2025.csv 是否存在。")
        return None

    try:
        df = pd.read_csv(DATA_FILE, parse_dates=["date"])
    except ValueError as exc:
        print("读取 CSV 时没有找到 date 列，无法使用 parse_dates=['date']。")
        print(f"错误信息：{exc}")
        return None

    missing_columns = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing_columns:
        print("市场数据列名不匹配。")
        print(f"当前实际列名：{list(df.columns)}")
        print(f"期望列名：{REQUIRED_COLUMNS}")
        print(f"缺失列名：{missing_columns}")
        return None

    return df.set_index("date")


def main():
    df = load_spy_data()
    if df is None:
        return

    # fig 是整张画布，ax 是画布上的一个坐标系。
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.plot(df.index, df["SPY_Close"], label="SPY")
    ax.set_title("S&P 500 ETF (SPY) Close Price 2018-2025")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend()

    plt.tight_layout()
    plt.savefig(OUTPUT_FILE, dpi=150)
    print(f"已保存 SPY 走势图：{OUTPUT_FILE}")
    plt.close(fig)


if __name__ == "__main__":
    main()
