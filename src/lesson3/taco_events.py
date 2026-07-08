from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_FILE = PROJECT_ROOT / "data" / "market_data_2018_2025.csv"
OUTPUT_FILE = PROJECT_ROOT / "data" / "taco_events.png"
PRICE_COLUMNS = ["USO_Close", "GLD_Close", "SPY_Close", "QQQ_Close"]
REQUIRED_COLUMNS = ["date"] + PRICE_COLUMNS
RENAME_COLUMNS = {
    "USO_Close": "USO",
    "GLD_Close": "GLD",
    "SPY_Close": "SPY",
    "QQQ_Close": "QQQ",
}
EVENTS = [
    ("2019-05-05", "Tariff hike 25%", "red"),
    ("2020-01-15", "Phase One Deal", "green"),
    ("2025-04-02", "Liberation Day", "red"),
    ("2025-04-09", "Tariff Pause 90d", "green"),
]


def load_price_data():
    """读取四资产数据，并筛选 2019 年以后的时间段。"""
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
    price_df = df[PRICE_COLUMNS].rename(columns=RENAME_COLUMNS).dropna()
    return price_df[price_df.index >= "2019-01-01"]


def main():
    price_df = load_price_data()
    if price_df is None:
        return
    if price_df.empty:
        print("2019 年以后的四资产价格数据为空，无法绘图。")
        return

    df_norm = price_df / price_df.iloc[0] * 100
    text_y = min(float(df_norm.max().max()) * 0.95, 140)

    fig, ax = plt.subplots(figsize=(14, 5))
    for asset in ["USO", "GLD", "SPY", "QQQ"]:
        ax.plot(df_norm.index, df_norm[asset], label=asset)

    # 用 pd.Timestamp 把事件日期转换成和日期索引兼容的时间对象。
    for date, label, color in EVENTS:
        event_x = pd.Timestamp(date)
        ax.axvline(x=event_x, linestyle="--", alpha=0.75, color=color)
        ax.text(
            event_x,
            text_y,
            label,
            rotation=90,
            color=color,
            va="top",
            ha="right",
            fontsize=8,
        )

    ax.set_title("Normalized Asset Prices with TACO Event Markers")
    ax.set_xlabel("Date")
    ax.set_ylabel("Indexed to 100")
    ax.legend()

    plt.tight_layout()
    plt.savefig(OUTPUT_FILE, dpi=150)
    print(f"已保存 TACO 事件标注图：{OUTPUT_FILE}")
    plt.close(fig)


if __name__ == "__main__":
    main()
