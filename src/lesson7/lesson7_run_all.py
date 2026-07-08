"""第7课本地辅助说明。

这个文件不会运行 Dify，也不会调用任何 API。
运行后只打印第7课本地文件说明和 Dify 网页端手动操作顺序。
"""

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data"
DOCS_DIR = PROJECT_ROOT / "docs"
LESSON7_DIR = PROJECT_ROOT / "src" / "lesson7"


def main() -> None:
    print("TACO 第7课：TACO Probability Engine")
    print()
    print("Codex 只生成本地辅助文件，不操作 Dify 网页，不处理 API Key。")
    print()

    print("第7课本地文件：")
    files = [
        LESSON7_DIR / "format_query_prompt.txt",
        LESSON7_DIR / "probability_prompt.txt",
        LESSON7_DIR / "validate_probability_code.py",
        LESSON7_DIR / "lesson7_test_inputs.txt",
    ]
    for index, path in enumerate(files, start=1):
        print(f"{index}. {path.relative_to(PROJECT_ROOT)}")

    print()
    print("第7课 Dify 网页端工作流结构：")
    print()
    print("Start")
    print("输入 hardness / domain / reasoning")
    print("↓")
    print("LLM① Format Retrieval Query")
    print("使用 format_query_prompt.txt")
    print("↓")
    print("Knowledge Retrieval")
    print("选择第5课 TACO 案例库，Top-K = 3")
    print("↓")
    print("LLM② Probability Engine")
    print("使用 probability_prompt.txt")
    print("↓")
    print("Code Validate Probability Output")
    print("使用 validate_probability_code.py")
    print("↓")
    print("End")
    print("输出 taco_probability / confidence / reasoning / key_cases")


if __name__ == "__main__":
    main()
