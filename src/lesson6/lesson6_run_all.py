"""
第6课：本地文件准备运行顺序提示。

本脚本不真正调用其他脚本，只打印推荐运行顺序和重要文件说明。
"""


print("第6课本地文件准备运行顺序：")
print("1. python src/lesson6/make_manual_test_cases.py")
print("2. python src/lesson6/validate_code_node.py")

print("\n可选课后批量测试：")
print("python src/lesson6/batch_test_template.py")

print("\n重要文件：")
print("* src/lesson6/classifier_prompt.txt")
print("* src/lesson6/code_node.py")
print("* data/lesson6_manual_test_cases.csv")
print("* data/lesson6_manual_test_cases.txt")
print("* docs/dify_workflow1_steps.md")
print("* docs/lesson6_prompt_tuning_guide.md")
print("* docs/lesson6_workflow_output_schema.md")

print("\n说明：")
print("Dify 工作流需要在网页端手动搭建。")
print("Codex 只负责生成 Prompt、Code 节点代码、测试数据和说明文件。")
