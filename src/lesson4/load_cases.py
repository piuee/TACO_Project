"""
第4课：读取并初步查看 TACO 历史案例数据。

本脚本会读取项目根目录下已有的 taco_cases.csv，
打印前 5 行、列名、数据形状，以及 result、domain、hardness 的统计信息。
"""

from pathlib import Path

import pandas as pd


# 当前文件位置是：项目根目录 / src / lesson4 / load_cases.py
# parents[2] 就是项目根目录 TACO_Project。
PROJECT_ROOT = Path(__file__).resolve().parents[2]
CASES_PATH = PROJECT_ROOT / "taco_cases.csv"


if not CASES_PATH.exists():
    print("没有找到 taco_cases.csv。")
    print(f"请确认文件是否放在项目根目录：{CASES_PATH}")
else:
    print("正在读取 TACO 历史案例数据...")
    print(f"数据文件路径：{CASES_PATH}")

    cases = pd.read_csv(CASES_PATH)

    print("\n前 5 行数据：")
    print(cases.head())

    print("\n列名：")
    print(list(cases.columns))

    print("\n数据形状：")
    print(f"共有 {cases.shape[0]} 行，{cases.shape[1]} 列。")

    if "result" in cases.columns:
        # 第4课统一把 NOT_TACO 看作 HOLD，方便后面进行两组比较。
        cases["result"] = cases["result"].replace("NOT_TACO", "HOLD")
        print("\nresult 分布（NOT_TACO 已统一视为 HOLD）：")
        print(cases["result"].value_counts(dropna=False))
    else:
        print("\n缺少 result 列，无法统计 result 分布。")

    if "domain" in cases.columns:
        print("\ndomain 分布：")
        print(cases["domain"].value_counts(dropna=False))
    else:
        print("\n缺少 domain 列，无法统计 domain 分布。")

    if "hardness" in cases.columns:
        print("\nhardness 描述性统计：")
        print(cases["hardness"].describe())
    else:
        print("\n缺少 hardness 列，无法统计 hardness。")
