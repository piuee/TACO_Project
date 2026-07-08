"""
第4课：比较 TACO 和 HOLD 两组事件后的 5 日市场反应。

本脚本会生成 1 行 3 列箱线图，分别观察 USO、GLD、SPY
在事件后 5 个交易日的表现，并保存到 data 文件夹。
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]
CASES_PATH = PROJECT_ROOT / "taco_cases.csv"
DATA_DIR = PROJECT_ROOT / "data"
OUTPUT_PATH = DATA_DIR / "boxplot_taco_vs_hold.png"

MARKET_COLUMNS = ["uso_5d", "gld_5d", "spy_5d"]
MARKET_TITLES = ["USO 5D", "GLD 5D", "SPY 5D"]


if not CASES_PATH.exists():
    print("没有找到 taco_cases.csv。")
    print(f"请确认文件是否放在项目根目录：{CASES_PATH}")
else:
    print("正在读取数据并绘制箱线图...")
    cases = pd.read_csv(CASES_PATH)

    if "result" not in cases.columns:
        print("缺少 result 列，无法比较 TACO 和 HOLD。")
    else:
        cases["result"] = cases["result"].replace("NOT_TACO", "HOLD")

        for column in MARKET_COLUMNS:
            if column in cases.columns:
                cases[column] = pd.to_numeric(cases[column], errors="coerce")

        fig, axes = plt.subplots(1, 3, figsize=(12, 4))
        fig.suptitle("TACO vs HOLD: 5-Day Market Reaction", fontsize=14)

        for ax, column, title in zip(axes, MARKET_COLUMNS, MARKET_TITLES):
            if column not in cases.columns:
                ax.set_title(title)
                ax.text(0.5, 0.5, "Missing column", ha="center", va="center")
                ax.axhline(0, color="gray", linestyle="--", linewidth=1)
                continue

            taco_values = cases.loc[cases["result"] == "TACO", column].dropna()
            hold_values = cases.loc[cases["result"] == "HOLD", column].dropna()

            # 如果某一组为空，用 NaN 占位，避免绘图时报错。
            if taco_values.empty:
                taco_values = pd.Series([float("nan")])
            if hold_values.empty:
                hold_values = pd.Series([float("nan")])

            ax.boxplot([taco_values, hold_values], labels=["TACO", "HOLD"])
            ax.axhline(0, color="gray", linestyle="--", linewidth=1)
            ax.set_title(title)
            ax.set_ylabel("5-Day Change (%)")

        DATA_DIR.mkdir(parents=True, exist_ok=True)
        plt.tight_layout()
        plt.savefig(OUTPUT_PATH, dpi=150)
        print(f"箱线图已保存到：{OUTPUT_PATH}")
        plt.show()
