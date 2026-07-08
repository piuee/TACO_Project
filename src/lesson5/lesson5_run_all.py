"""
第5课：课堂运行顺序提示。

本脚本不导入其他脚本，只打印建议的运行顺序和第5课说明，
方便学生按步骤准备 Dify Knowledge 需要的本地文件。
"""


print("第5课运行顺序：")
print("1. python src/lesson5/check_rag_cases.py")
print("2. python src/lesson5/make_kb.py")
print("3. python src/lesson5/make_test_queries.py")

print("\n生成文件：")
print("* data/taco_kb.txt")
print("* data/dify_test_queries.txt")
print("* docs/dify_upload_steps.md")
print("* docs/dify_test_template.md")

print("\n说明：")
print("data/taco_kb.txt 是上传到 Dify Knowledge 的文件。")
print("Dify 网页端需要手动操作，Codex 不负责登录和上传。")
