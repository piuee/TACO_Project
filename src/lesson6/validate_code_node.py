"""
第6课：本地测试 Dify Code 节点解析效果。

本脚本会导入 code_node.py 中的 main 函数，
用不同格式的 LLM 输出测试 JSON 清理和兜底逻辑。
"""

from code_node import main


test_inputs = [
    '{"hardness":8,"domain":"tariff","reasoning":"有明确关税威胁"}',
    """```json
{"hardness":9,"domain":"tech","reasoning":"立即限制芯片出口"}
```""",
    """好的，我来分析：
{"hardness":6,"domain":"energy","reasoning":"涉及能源限制"}
希望对你有帮助。""",
    '{"hardness":12,"domain":"tariff","reasoning":"过高测试"}',
    '{"hardness":5,"domain":"economy","reasoning":"领域不在列表中"}',
    "This is not JSON.",
]


print("开始测试 code_node.py 的解析效果...\n")

for index, raw_text in enumerate(test_inputs, start=1):
    result = main(raw_text)

    print(f"测试 {index}")
    print("原始输入：")
    print(raw_text)
    print("\n清洗后的输出：")
    print(result)
    print("---------------------------------------------------------------")

print("\n测试完成。")
