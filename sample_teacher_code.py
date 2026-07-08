#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TACO 课程 · 老师样例代码（标准答案参考）
====================================================
这份脚本对应 S02–S04 三节课学生要做的核心任务，是老师手里的"标准答案"。
运行后会打印每节的关键结果，方便老师对照学生作业、提前知道正确数值。

数据文件（与本脚本放同一目录）：
  - market_data_2018_2025.csv   每日收盘价（USO 原油 / GLD 黄金 / SPY 美股 / QQQ 纳指）
  - taco_cases.csv              35 条 Trump 言论案例（含强硬度、TACO标签、5日涨跌）

运行： python sample_teacher_code.py
依赖： pandas matplotlib （课程标准环境已装）
====================================================
注意：本数据为教学用合成数据，不是真实市场行情。详见《数据说明文档》。
"""

import pandas as pd

MARKET = "market_data_2018_2025.csv"
CASES  = "taco_cases.csv"


def line(t=""):
    print("\n" + "=" * 60)
    if t:
        print(t)
        print("=" * 60)


# ============================================================
# S02 · Python 金融数据抓取与读取
# 学生任务：用 pandas 读入价格数据，看懂金融时间序列的结构
# ============================================================
def s02_load_data():
    line("S02 · 读取并认识金融数据")
    df = pd.read_csv(MARKET, parse_dates=["date"])
    print(f"数据行数：{len(df)}  （每行 = 一个交易日）")
    print(f"日期范围：{df['date'].min().date()}  到  {df['date'].max().date()}")
    print(f"包含资产：USO 原油 / GLD 黄金 / SPY 美股 / QQQ 纳指")
    print("\n前 5 行：")
    print(df.head().to_string(index=False))
    print("\n基本统计（SPY 标普500）：")
    print(f"  最低 {df['SPY_Close'].min():.2f}   最高 {df['SPY_Close'].max():.2f}   "
          f"均值 {df['SPY_Close'].mean():.2f}")
    return df


# ============================================================
# S03 · 金融数据可视化（事件标注）
# 学生任务：画价格走势，在时间轴上用 axvline 标出 TACO 事件
# 这里不弹图，只验证"标注用的数据对得上"——图见 demo_chart_1
# ============================================================
def s03_event_alignment(df):
    line("S03 · 事件标注：每个案例日期都能在市场表里查到")
    cases = pd.read_csv(CASES, parse_dates=["date"])
    market_dates = set(df["date"])
    missing = [d.date() for d in cases["date"] if d not in market_dates]
    if missing:
        print(f"⚠️ 有 {len(missing)} 个案例日期不在市场表中：{missing}")
        print("   （上课前应已修复——所有案例日期都对到了真实交易日）")
    else:
        print(f"✓ 全部 {len(cases)} 个案例日期都能在市场表中找到，"
              f"axvline 标注不会错位。")
    print("\n可视化产物：见 demo_chart_1_走势事件标注.png")
    print("  绿色虚线 = TACO（软化/反悔）   红色虚线 = NOT_TACO（说到做到）")


# ============================================================
# S04 · 历史案例量化分析
# 学生任务：把案例量化，发现"硬度+是否兑现"与"市场反应"的规律
# ============================================================
def s04_quantify():
    line("S04 · 量化分析：两类言论的市场反应")
    cases = pd.read_csv(CASES, parse_dates=["date"])
    print(f"案例总数：{len(cases)}")
    print("\nTACO 标签分布：")
    print(cases["result"].value_counts().to_string())

    print("\n—— 按 result 分组，看 5 日平均涨跌（%）——")
    grp = cases.groupby("result")[["uso_5d", "gld_5d", "spy_5d"]].mean().round(2)
    print(grp.to_string())
    print("\n解读：NOT_TACO（说到做到）→ 原油美股跌、黄金涨（避险）；"
          "\n      TACO（软化反悔）→ 市场松一口气、温和反弹。")

    print("\n—— 按强硬度分档，看 SPY 5 日涨跌（%）——")
    def band(h):
        if h <= 4: return "软 (2-4)"
        if h <= 7: return "中 (5-7)"
        return "硬 (8-10)"
    cases["硬度档"] = cases["hardness"].apply(band)
    band_grp = cases.groupby("硬度档")["spy_5d"].mean().round(2)
    # 固定顺序
    for k in ["软 (2-4)", "中 (5-7)", "硬 (8-10)"]:
        if k in band_grp.index:
            print(f"  {k:10}  →  SPY 平均 {band_grp[k]:+.2f}%")
    print("\n这就是 RAG 知识库要喂给 AI 的'历史规律'，也是 S07 概率引擎判断的依据。")

    print("\n—— 找一周内的反转：4/2 加税大跌 → 4/9 暂停反弹 ——")
    apr = cases[(cases["date"] >= "2025-04-01") & (cases["date"] <= "2025-04-15")]
    if not apr.empty:
        print(apr[["date", "hardness", "result", "uso_5d", "gld_5d", "spy_5d"]]
              .to_string(index=False))
    print("\n可视化产物：见 demo_chart_2 / demo_chart_3 / demo_chart_4")


def main():
    print("TACO 课程 · 老师样例代码运行结果")
    print("（这是 S02–S04 学生任务的标准答案参考）")
    df = s02_load_data()
    s03_event_alignment(df)
    s04_quantify()
    line("全部样例运行完成 ✓")


if __name__ == "__main__":
    main()
