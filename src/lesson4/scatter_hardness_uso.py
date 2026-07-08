"""
第4课：观察强硬度 hardness 与 USO 5 日反应之间的关系。

本脚本会绘制散点图，使用不同 marker 区分 TACO 和 HOLD，
并用 numpy.polyfit 添加一条简单趋势线。
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]
CASES_PATH = PROJECT_ROOT / "taco_cases.csv"
DATA_DIR = PROJECT_ROOT / "data"
OUTPUT_PATH = DATA_DIR / "scatter_hardness_uso.png"


if not CASES_PATH.exists():
    print("没有找到 taco_cases.csv。")
    print(f"请确认文件是否放在项目根目录：{CASES_PATH}")
else:
    print("正在绘制 hardness 与 uso_5d 的散点图...")
    cases = pd.read_csv(CASES_PATH)

    required_columns = ["hardness", "uso_5d", "result"]
    missing_columns = [col for col in required_columns if col not in cases.columns]

    if missing_columns:
        print("缺少以下列，无法绘图：")
        print(missing_columns)
    else:
        cases["result"] = cases["result"].replace("NOT_TACO", "HOLD")
        cases["hardness"] = pd.to_numeric(cases["hardness"], errors="coerce")
        cases["uso_5d"] = pd.to_numeric(cases["uso_5d"], errors="coerce")
        plot_data = cases.dropna(subset=["hardness", "uso_5d"])

        plt.figure(figsize=(7, 5))

        taco_data = plot_data[plot_data["result"] == "TACO"]
        hold_data = plot_data[plot_data["result"] == "HOLD"]

        plt.scatter(taco_data["hardness"], taco_data["uso_5d"], marker="o", label="TACO")
        plt.scatter(hold_data["hardness"], hold_data["uso_5d"], marker="s", label="HOLD")

        plt.axhline(0, color="gray", linestyle="--", linewidth=1)

        if len(plot_data) >= 2:
            a, b = np.polyfit(plot_data["hardness"], plot_data["uso_5d"], 1)
            x_values = np.linspace(plot_data["hardness"].min(), plot_data["hardness"].max(), 100)
            y_values = a * x_values + b
            plt.plot(x_values, y_values, color="black", linewidth=1.5, label="Trend line")
            print(f"趋势线公式：USO_5D = {a:.3f} * hardness + {b:.3f}")
        else:
            print("有效数据少于 2 行，无法计算趋势线。")

        plt.title("Hardness vs USO 5-Day Reaction")
        plt.xlabel("Hardness")
        plt.ylabel("USO 5-Day Change (%)")
        plt.legend()

        DATA_DIR.mkdir(parents=True, exist_ok=True)
        plt.tight_layout()
        plt.savefig(OUTPUT_PATH, dpi=150)
        print(f"散点图已保存到：{OUTPUT_PATH}")
