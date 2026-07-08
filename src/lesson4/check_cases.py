"""
第4课：检查 taco_cases.csv 是否符合课堂分析标准。

本脚本会检查必需列、summary 字段、缺失值、result 取值、
hardness 范围，以及 5 日市场反应列是否为数字。
"""

from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]
CASES_PATH = PROJECT_ROOT / "taco_cases.csv"

REQUIRED_COLUMNS = [
    "date",
    "hardness",
    "domain",
    "result",
    "uso_5d",
    "gld_5d",
    "spy_5d",
]
SUMMARY_COLUMNS = ["summary", "summary_zh", "summary_en"]
VALID_RESULTS = {"TACO", "HOLD", "NOT_TACO"}
MARKET_COLUMNS = ["uso_5d", "gld_5d", "spy_5d"]


if not CASES_PATH.exists():
    print("没有找到 taco_cases.csv。")
    print(f"请确认文件是否放在项目根目录：{CASES_PATH}")
else:
    print("开始检查 taco_cases.csv...")
    print(f"数据文件路径：{CASES_PATH}")

    cases = pd.read_csv(CASES_PATH)

    print("\n1. 检查必需列：")
    missing_columns = [col for col in REQUIRED_COLUMNS if col not in cases.columns]
    if missing_columns:
        print("缺少以下必需列：")
        print(missing_columns)
    else:
        print("必需列齐全。")

    print("\n2. 检查 summary 字段：")
    existing_summary_columns = [col for col in SUMMARY_COLUMNS if col in cases.columns]
    if existing_summary_columns:
        print(f"找到 summary 相关列：{existing_summary_columns}")
    else:
        print("没有找到 summary、summary_zh、summary_en 中的任何一列。")

    print("\n3. 检查缺失值：")
    missing_values = cases.isna().sum()
    missing_values = missing_values[missing_values > 0]
    if missing_values.empty:
        print("没有发现缺失值。")
    else:
        print("以下列存在缺失值：")
        print(missing_values)

    print("\n4. 检查 result 取值：")
    if "result" in cases.columns:
        result_values = set(cases["result"].dropna().astype(str).unique())
        invalid_results = sorted(result_values - VALID_RESULTS)
        if invalid_results:
            print("发现不符合要求的 result 取值：")
            print(invalid_results)
        else:
            print("result 只包含 TACO / HOLD / NOT_TACO。")

        if "NOT_TACO" in result_values:
            print("提示：NOT_TACO 会在第4课分析中统一视为 HOLD。")
    else:
        print("缺少 result 列，无法检查 result 取值。")

    print("\n5. 检查 hardness 是否在 1-10 之间：")
    if "hardness" in cases.columns:
        hardness_number = pd.to_numeric(cases["hardness"], errors="coerce")
        invalid_hardness = cases[hardness_number.isna() | ~hardness_number.between(1, 10)]
        if invalid_hardness.empty:
            print("hardness 全部在 1-10 之间。")
        else:
            print("以下行的 hardness 不符合 1-10 范围：")
            print(invalid_hardness[["date", "hardness"]])
    else:
        print("缺少 hardness 列，无法检查范围。")

    print("\n6. 检查 uso_5d、gld_5d、spy_5d 是否是数字：")
    for column in MARKET_COLUMNS:
        if column not in cases.columns:
            print(f"缺少 {column} 列，无法检查。")
            continue

        numeric_values = pd.to_numeric(cases[column], errors="coerce")
        invalid_rows = cases[numeric_values.isna()]
        if invalid_rows.empty:
            print(f"{column} 全部可以转换为数字。")
        else:
            print(f"{column} 中存在不能转换为数字的值：")
            print(invalid_rows[["date", column]])

    print("\n检查完成。")
