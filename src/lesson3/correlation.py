from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]
CASE_FILE = PROJECT_ROOT / "taco_cases.csv"
OUTPUT_FILE = PROJECT_ROOT / "data" / "correlation_matrix.csv"
REQUIRED_COLUMNS = ["hardness", "uso_5d", "gld_5d", "spy_5d"]
OPTIONAL_COLUMNS = ["qqq_5d"]


def main():
    """计算硬度分数和资产 5 日涨跌幅之间的相关矩阵。"""
    if not CASE_FILE.exists():
        print("没有找到 taco_cases.csv，这部分可以等第4课案例库整理完成后再运行。")
        return

    df = pd.read_csv(CASE_FILE)
    missing_columns = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing_columns:
        print("taco_cases.csv 缺少必要列，无法计算相关矩阵。")
        print(f"当前实际列名：{list(df.columns)}")
        print(f"必要列名：{REQUIRED_COLUMNS}")
        print(f"缺失列名：{missing_columns}")
        return

    columns = REQUIRED_COLUMNS + [col for col in OPTIONAL_COLUMNS if col in df.columns]

    # corr 会计算每两列之间的 Pearson 相关系数。
    corr_matrix = df[columns].corr()
    print("相关矩阵：")
    print(corr_matrix)

    corr_matrix.to_csv(OUTPUT_FILE)
    print(f"已保存相关矩阵 CSV：{OUTPUT_FILE}")


if __name__ == "__main__":
    main()
