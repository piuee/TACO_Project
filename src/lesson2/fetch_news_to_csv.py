# ==============================
# TACO 第2次课 示例2
# 把 RSS 新闻保存成 CSV
# 文件名：fetch_news_to_csv.py
# ==============================

import feedparser
import pandas as pd
from pathlib import Path
from urllib.parse import quote

# 项目根目录
# 当前文件在 src/lesson2 中
# parents[2] 可以回到 TACO_Project 根目录
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# data 文件夹路径
DATA_DIR = PROJECT_ROOT / "data"

# 如果 data 文件夹不存在，就创建
DATA_DIR.mkdir(exist_ok=True)

# 设置搜索关键词
# 注意：这里可以正常写空格
query = "Trump tariff"

# 把搜索关键词进行 URL 编码
# 例如："Trump tariff" 会变成 "Trump%20tariff"
query_encoded = quote(query)

# Google News RSS 地址
# q= 后面必须放编码后的关键词，不能直接放带空格的 query
url = f"https://news.google.com/rss/search?q={query_encoded}&hl=en-US&gl=US&ceid=US:en"

print("实际访问的 RSS 地址：")
print(url)

# 解析 RSS
rss = feedparser.parse(url)

# 用列表保存新闻
news_data = []

# 遍历前 20 条新闻
for entry in rss.entries[:20]:
    # 使用 get() 可以避免字段不存在时报错
    title = entry.get("title", "")
    published = entry.get("published", "")
    summary = entry.get("summary", "")
    link = entry.get("link", "")

    # 每条新闻保存成一个字典
    news_data.append({
        "title": title,
        "date": published,
        "summary": summary,
        "link": link
    })

# 转成 DataFrame 表格
df_news = pd.DataFrame(news_data)

# 判断是否抓取到新闻
if len(df_news) == 0:
    print("没有抓取到新闻，请检查网络或 RSS 地址。")
else:
    # 输出预览
    print("\n新闻数据预览：")
    print(df_news.head())

    # 保存到 data 文件夹
    output_path = DATA_DIR / "raw_news.csv"
    df_news.to_csv(output_path, index=False, encoding="utf-8-sig")

    print("\n原始新闻数据已保存到：")
    print(output_path)