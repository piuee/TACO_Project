"""
第4课：按领域 domain 分析 TACO 历史案例。

本脚本会统计每个领域中的 TACO / HOLD 数量、TACO 比例、
平均强硬度和 5 日市场反应，并保存汇总表和柱状图。
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]
CASES_PATH = PROJECT_ROOT / "taco_cases.csv"
DATA_DIR = PROJECT_ROOT / "data"
SUMMARY_PATH = DATA_DIR / "domain_summary.csv"
BAR_PATH = DATA_DIR / "domain_uso_bar.png"

MARKET_COLUMNS = ["uso_5d", "gld_5d", "spy_5d"]


if not CASES_PATH.exists():
    print("没有找到 taco_cases.csv。")
    print(f"请确认文件是否放在项目根目录：{CASES_PATH}")
else:
    print("正在进行 domain 分析...")
    cases = pd.read_csv(CASES_PATH)

    required_columns = ["domain", "result", "hardness"] + MARKET_COLUMNS
    missing_columns = [col for col in required_columns if col not in cases.columns]

    if missing_columns:
        print("缺少以下列，无法完成 domain 分析：")
        print(missing_columns)
    else:
        cases["result"] = cases["result"].replace("NOT_TACO", "HOLD")
        cases["hardness"] = pd.to_numeric(cases["hardness"], errors="coerce")
        for column in MARKET_COLUMNS:
            cases[column] = pd.to_numeric(cases[column], errors="coerce")

        print("\n按 domain 和 result 统计数量：")
        domain_result_counts = pd.crosstab(cases["domain"], cases["result"])
        print(domain_result_counts)

        summary = domain_result_counts.copy()
        if "TACO" not in summary.columns:
            summary["TACO"] = 0
        if "HOLD" not in summary.columns:
            summary["HOLD"] = 0

        summary = summary[["TACO", "HOLD"]]
        summary["total"] = summary["TACO"] + summary["HOLD"]
        summary["taco_rate"] = summary["TACO"] / summary["total"]

        domain_means = cases.groupby("domain")[["hardness", "uso_5d", "gld_5d", "spy_5d"]].mean()
        summary["avg_hardness"] = domain_means["hardness"]
        summary["uso_5d_mean"] = domain_means["uso_5d"]
        summary["gld_5d_mean"] = domain_means["gld_5d"]
        summary["spy_5d_mean"] = domain_means["spy_5d"]

        summary = summary.reset_index()

        DATA_DIR.mkdir(parents=True, exist_ok=True)
        summary.to_csv(SUMMARY_PATH, index=False, encoding="utf-8-sig")
        print(f"\ndomain 汇总表已保存到：{SUMMARY_PATH}")

        # 为避免中文 domain 名称在图中乱码，横轴使用 Domain 1、Domain 2 等英文标签。
        plot_data = summary.sort_values("uso_5d_mean")
        x_labels = [f"Domain {i + 1}" for i in range(len(plot_data))]

        plt.figure(figsize=(9, 5))
        plt.bar(x_labels, plot_data["uso_5d_mean"])
        plt.axhline(0, color="gray", linestyle="--", linewidth=1)
        plt.title("Average USO 5-Day Reaction by Domain")
        plt.xlabel("Domain")
        plt.ylabel("Average USO 5-Day Change (%)")
        plt.xticks(rotation=30)
        plt.tight_layout()
        plt.savefig(BAR_PATH, dpi=150)
        print(f"domain 平均 USO 柱状图已保存到：{BAR_PATH}")

        print("\n图中英文标签与原始 domain 的对应关系：")
        for label, domain in zip(x_labels, plot_data["domain"]):
            print(f"{label}: {domain}")
