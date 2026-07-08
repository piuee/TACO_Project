from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_FILE = PROJECT_ROOT / "data" / "market_data_2018_2025.csv"
OUTPUT_FILE = PROJECT_ROOT / "data" / "four_assets_normalized.png"
PRICE_COLUMNS = ["USO_Close", "GLD_Close", "SPY_Close", "QQQ_Close"]
REQUIRED_COLUMNS = ["date"] + PRICE_COLUMNS
RENAME_COLUMNS = {
    "USO_Close": "USO",
    "GLD_Close": "GLD",
    "SPY_Close": "SPY",
    "QQQ_Close": "QQQ",
}


def load_price_data():
    """读取四个资产的价格数据，并完成列名检查。"""
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

    df = df.set_index("date")
    return df[PRICE_COLUMNS].rename(columns=RENAME_COLUMNS).dropna()


def main():
    price_df = load_price_data()
    if price_df is None:
        return
    if price_df.empty:
        print("四资产价格数据为空，无法绘图。")
        return

    # 把每个资产第一天都设为 100，方便比较相对涨跌。
    df_norm = price_df / price_df.iloc[0] * 100

    fig, ax = plt.subplots(figsize=(12, 5))
    for asset in ["USO", "GLD", "SPY", "QQQ"]:
        ax.plot(df_norm.index, df_norm[asset], label=asset)

    ax.axhline(y=100, linestyle="--", linewidth=0.8)
    ax.set_title("Normalized Asset Prices 2018-2025")
    ax.set_xlabel("Date")
    ax.set_ylabel("Indexed to 100")
    ax.legend()

    plt.tight_layout()
    plt.savefig(OUTPUT_FILE, dpi=150)
    print(f"已保存四资产归一化走势图：{OUTPUT_FILE}")
    plt.close(fig)


if __name__ == "__main__":
    main()
