"""
第4课：把 TACO 历史案例转换为 RAG 知识库文本。

本脚本会读取 taco_cases.csv，把每一行案例整理成自然语言文本，
并保存为第5课 Dify 知识库会用到的 data/rag_cases.csv。
"""

from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]
CASES_PATH = PROJECT_ROOT / "taco_cases.csv"
DATA_DIR = PROJECT_ROOT / "data"
OUTPUT_PATH = DATA_DIR / "rag_cases.csv"


def choose_summary(row):
    """按 summary_zh、summary、summary_en 的顺序选择摘要。"""
    for column in ["summary_zh", "summary", "summary_en"]:
        if column in row.index and pd.notna(row[column]) and str(row[column]).strip():
            return str(row[column]).strip()
    return "无摘要"


def format_percent(value):
    """把数字格式化成带正负号的百分比文本。"""
    number = pd.to_numeric(value, errors="coerce")
    if pd.isna(number):
        return "缺失"
    return f"{number:+.1f}%"


if not CASES_PATH.exists():
    print("没有找到 taco_cases.csv。")
    print(f"请确认文件是否放在项目根目录：{CASES_PATH}")
else:
    print("正在生成 RAG 案例文本...")
    cases = pd.read_csv(CASES_PATH)

    required_columns = ["date", "hardness", "domain", "result", "uso_5d", "gld_5d", "spy_5d"]
    missing_columns = [col for col in required_columns if col not in cases.columns]

    if missing_columns:
        print("缺少以下列，无法生成 rag_cases.csv：")
        print(missing_columns)
    else:
        cases["result"] = cases["result"].replace("NOT_TACO", "HOLD")

        rag_rows = []

        for _, row in cases.iterrows():
            summary = choose_summary(row)

            if row["result"] == "TACO":
                result_text = "最终 TACO（软化、推迟或让步）"
            else:
                result_text = "HOLD（坚持原立场，没有明显软化）"

            rag_text = f"""日期：{row["date"]}
事件：{summary}
强硬度：{row["hardness"]}/10
领域：{row["domain"]}
结果：{result_text}
市场反应（事件后5个交易日）：

* 石油 USO：{format_percent(row["uso_5d"])}
* 黄金 GLD：{format_percent(row["gld_5d"])}
* 美股 SPY：{format_percent(row["spy_5d"])}
"""

            rag_rows.append(
                {
                    "date": row["date"],
                    "rag_text": rag_text,
                }
            )

        rag_cases = pd.DataFrame(rag_rows)

        DATA_DIR.mkdir(parents=True, exist_ok=True)
        rag_cases.to_csv(OUTPUT_PATH, index=False, encoding="utf-8-sig")
        print(f"RAG 案例文件已保存到：{OUTPUT_PATH}")

        if not rag_cases.empty:
            print("\n第一条案例预览：")
            print(rag_cases.iloc[0]["rag_text"])

            print("\n最后一条案例预览：")
            print(rag_cases.iloc[-1]["rag_text"])
