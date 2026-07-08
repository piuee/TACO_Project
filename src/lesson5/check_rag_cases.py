"""
第5课：检查第4课生成的 RAG 案例文件。

本脚本会检查 data/rag_cases.csv 是否存在，是否包含 date 和 rag_text 两列，
并检查 rag_text 是否为空或过短，帮助学生确认能否继续生成 taco_kb.txt。
"""

from pathlib import Path

import pandas as pd


# 当前文件位置是：项目根目录 / src / lesson5 / check_rag_cases.py
# parents[2] 就是项目根目录 TACO_Project。
PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data"
RAG_CASES_PATH = DATA_DIR / "rag_cases.csv"


if not RAG_CASES_PATH.exists():
    print("没有找到第4课生成的 RAG 案例文件。")
    print("\n请先运行第4课：")
    print("python src/lesson4/format_rag.py")
    print("\n生成：")
    print("data/rag_cases.csv")
else:
    print("正在检查 data/rag_cases.csv...")
    print(f"文件路径：{RAG_CASES_PATH}")

    rag_cases = pd.read_csv(RAG_CASES_PATH)

    print("\n前 5 行数据：")
    print(rag_cases.head())

    print("\n列名：")
    print(list(rag_cases.columns))

    print("\n数据形状：")
    print(f"共有 {rag_cases.shape[0]} 行，{rag_cases.shape[1]} 列。")

    required_columns = ["date", "rag_text"]
    missing_columns = [col for col in required_columns if col not in rag_cases.columns]

    if missing_columns:
        print("\n缺少以下必需列：")
        print(missing_columns)
        print("\n请先重新运行第4课：")
        print("python src/lesson4/format_rag.py")
        print("\n当前不能继续生成 taco_kb.txt。")
    else:
        print("\n已找到 date 和 rag_text 两列。")

        empty_rows = rag_cases[rag_cases["rag_text"].isna()]
        if empty_rows.empty:
            print("rag_text 没有空值。")
        else:
            print("以下行的 rag_text 是空值：")
            print(empty_rows[["date", "rag_text"]])

        text_length = rag_cases["rag_text"].fillna("").astype(str).str.len()
        short_rows = rag_cases[text_length < 20]
        if short_rows.empty:
            print("没有发现长度小于 20 的 rag_text。")
        else:
            print("以下行的 rag_text 可能太短，建议检查：")
            print(short_rows[["date", "rag_text"]])

        print(f"\n案例数量：{len(rag_cases)}")

        if empty_rows.empty and short_rows.empty:
            print("\n检查通过，可以继续生成 taco_kb.txt。")
            print("下一步运行：python src/lesson5/make_kb.py")
        else:
            print("\n检查发现需要关注的问题。")
            print("建议先确认 rag_text 内容，再生成 taco_kb.txt。")
