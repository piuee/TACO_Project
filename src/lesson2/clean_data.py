# ==============================
# TACO 第2次课 示例5
# 新闻清洗函数
# 文件名：clean_data.py
# ==============================

# pandas 用来处理表格数据
import pandas as pd

# re 用来处理正则表达式，清理 HTML 标签
import re

# pathlib 用来处理路径
from pathlib import Path


def clean_news(df):
    """
    清洗新闻数据。

    参数：
        df: 原始新闻 DataFrame，至少包含 title 和 date 两列

    返回：
        清洗后的 DataFrame
    """

    # 1. 删除标题或日期为空的新闻
    # 没有标题或日期的新闻无法用于后续分析
    df = df.dropna(subset=["title", "date"])

    # 2. 统一日期格式
    # pd.to_datetime() 可以把字符串日期转换成日期格式
    # errors="coerce" 表示无法转换的日期会变成 NaT
    df["date"] = pd.to_datetime(df["date"], errors="coerce").dt.date

    # 日期转换后，可能出现 NaT，需要再次删除
    df = df.dropna(subset=["date"])

    # 3. 去 HTML 标签
    # 有些 RSS 摘要或标题中可能包含 <a>、<b>、<p> 等标签
    def strip_html(text):
        # 先把内容转成字符串，防止空值报错
        text = str(text)

        # r"<[^>]+>" 表示匹配 HTML 标签
        return re.sub(r"<[^>]+>", "", text)

    # 清理 title 中的 HTML 标签
    df["title"] = df["title"].apply(strip_html)

    # 如果有 summary 列，也清理 summary
    if "summary" in df.columns:
        df["summary"] = df["summary"].apply(strip_html)

    # 4. 删除重复新闻
    # 如果同一天出现完全相同标题，只保留一条
    df = df.drop_duplicates(subset=["date", "title"])

    return df


# ==============================
# 下面是测试代码
# ==============================

# 找到项目根目录
PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data"

# 原始新闻文件路径
raw_news_path = DATA_DIR / "raw_news.csv"

# 清洗后新闻文件路径
clean_news_path = DATA_DIR / "clean_news.csv"

if not raw_news_path.exists():
    print("没有找到 raw_news.csv。")
    print("请先运行 fetch_news_to_csv.py 抓取新闻。")
else:
    # 读取原始新闻
    raw_df = pd.read_csv(raw_news_path)

    print("清洗前数据数量：", len(raw_df))

    # 调用清洗函数
    clean_df = clean_news(raw_df)

    print("清洗后数据数量：", len(clean_df))

    print("\n清洗后数据预览：")
    print(clean_df.head())

    # 保存清洗后的新闻
    clean_df.to_csv(clean_news_path, index=False, encoding="utf-8-sig")

    print("\n清洗后的新闻已保存到：", clean_news_path)