"""
第5课：把 rag_cases.csv 转换成 Dify Knowledge 可上传的文本文件。

本脚本会读取 data/rag_cases.csv，将每条 rag_text 写入 data/taco_kb.txt。
每条案例之间使用 --- 分隔，帮助 Dify 把案例切成独立 chunk。
"""

from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data"
RAG_CASES_PATH = DATA_DIR / "rag_cases.csv"
OUTPUT_PATH = DATA_DIR / "taco_kb.txt"


if not RAG_CASES_PATH.exists():
    print("没有找到 data/rag_cases.csv。")
    print("\n请先运行第4课：")
    print("python src/lesson4/format_rag.py")
else:
    print("正在读取 RAG 案例文件...")
    print(f"输入文件路径：{RAG_CASES_PATH}")

    rag_cases = pd.read_csv(RAG_CASES_PATH)

    if "rag_text" not in rag_cases.columns:
        print("缺少 rag_text 列，无法生成 taco_kb.txt。")
        print("请先检查第4课生成的 data/rag_cases.csv。")
    else:
        # fillna("") 可以避免空值在文本里变成 nan。
        texts = rag_cases["rag_text"].fillna("").astype(str).str.strip()
        texts = texts[texts != ""]

        if texts.empty:
            print("rag_text 没有有效内容，无法生成 taco_kb.txt。")
        else:
            # 分隔符 --- 很重要，不要把所有案例挤在一起。
            kb_text = "\n\n---\n\n".join(texts)

            DATA_DIR.mkdir(parents=True, exist_ok=True)
            OUTPUT_PATH.write_text(kb_text, encoding="utf-8")

            print(f"知识库文本文件已生成：{OUTPUT_PATH}")
            print(f"案例数量：{len(texts)}")

            print("\n第一条案例预览：")
            print(texts.iloc[0])

            print("\n最后一条案例预览：")
            print(texts.iloc[-1])

            print("\ntaco_kb.txt 是第5课上传到 Dify Knowledge 的文件。")
