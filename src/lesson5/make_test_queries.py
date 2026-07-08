"""
第5课：生成 Dify 检索测试用语。

本脚本会把 5 条测试言论写入 data/dify_test_queries.txt，
方便学生复制到 Dify Knowledge 中测试 Top-3 检索结果。
"""

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data"
OUTPUT_PATH = DATA_DIR / "dify_test_queries.txt"

TEST_QUERIES = [
    {
        "number": 1,
        "type": "强硬",
        "query": "Trump threatens to impose new tariffs on imported goods.",
    },
    {
        "number": 2,
        "type": "强硬",
        "query": "The administration may restrict technology exports to foreign companies.",
    },
    {
        "number": 3,
        "type": "软化",
        "query": "Trump says he may delay the tariff plan and continue negotiations.",
    },
    {
        "number": 4,
        "type": "软化",
        "query": "Trade talks are making progress and policy adjustments are possible.",
    },
    {
        "number": 5,
        "type": "模糊",
        "query": "Future trade policy will depend on market conditions and negotiations.",
    },
]


print("正在生成 Dify 检索测试用语...")

lines = []
for item in TEST_QUERIES:
    lines.append(f"Test {item['number']}")
    lines.append(f"Type: {item['type']}")
    lines.append(f"Query: {item['query']}")
    lines.append("---------------------------------------------------------------")
    lines.append("")

DATA_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_PATH.write_text("\n".join(lines), encoding="utf-8")

print(f"测试用语文件已生成：{OUTPUT_PATH}")
print(f"测试言论数量：{len(TEST_QUERIES)}")
print("\n文件内容预览：")
print(OUTPUT_PATH.read_text(encoding="utf-8"))
