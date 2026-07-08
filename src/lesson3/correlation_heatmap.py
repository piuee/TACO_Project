from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]
CASE_FILE = PROJECT_ROOT / "taco_cases.csv"
OUTPUT_FILE = PROJECT_ROOT / "data" / "correlation_heatmap.png"
REQUIRED_COLUMNS = ["hardness", "uso_5d", "gld_5d", "spy_5d"]
OPTIONAL_COLUMNS = ["qqq_5d"]


def main():
    """使用 matplotlib 绘制相关性热力图，不使用 seaborn。"""
    if not CASE_FILE.exists():
        print("没有找到 taco_cases.csv，这部分可以等第4课案例库整理完成后再运行。")
        return

    df = pd.read_csv(CASE_FILE)
    missing_columns = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing_columns:
        print("taco_cases.csv 缺少必要列，无法绘制相关性热力图。")
        print(f"当前实际列名：{list(df.columns)}")
        print(f"必要列名：{REQUIRED_COLUMNS}")
        print(f"缺失列名：{missing_columns}")
        return

    columns = REQUIRED_COLUMNS + [col for col in OPTIONAL_COLUMNS if col in df.columns]
    corr_matrix = df[columns].corr()

    fig, ax = plt.subplots(figsize=(7, 6))
    image = ax.imshow(corr_matrix, vmin=-1, vmax=1, cmap="coolwarm")
    fig.colorbar(image, ax=ax)

    ax.set_xticks(range(len(columns)))
    ax.set_yticks(range(len(columns)))
    ax.set_xticklabels(columns, rotation=45, ha="right")
    ax.set_yticklabels(columns)

    # 在每个格子里写入两位小数，方便直接读数。
    for row in range(len(columns)):
        for col in range(len(columns)):
            value = corr_matrix.iloc[row, col]
            ax.text(col, row, f"{value:.2f}", ha="center", va="center", color="black")

    ax.set_title("Correlation Heatmap")
    plt.tight_layout()
    plt.savefig(OUTPUT_FILE, dpi=150)
    print(f"已保存相关性热力图：{OUTPUT_FILE}")
    plt.close(fig)


if __name__ == "__main__":
    main()
