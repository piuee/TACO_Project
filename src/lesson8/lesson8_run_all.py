"""第8课本地辅助说明。

这个文件不会调用 Dify，也不会调用任何 API。
运行后只打印第8课本地文件说明、推荐运行顺序和 Dify 网页端手动操作顺序。
"""

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data"
DOCS_DIR = PROJECT_ROOT / "docs"
LESSON8_DIR = PROJECT_ROOT / "src" / "lesson8"


def main() -> None:
    print("TACO 第8课：TACO Market Impact Predictor")
    print()
    print("Codex 只生成本地辅助文件，不操作 Dify 网页，不处理真实 API Key。")
    print("本项目不是投资建议，只做事件影响方向性分析。")
    print()

    print("第8课本地文件：")
    files = [
        LESSON8_DIR / "market_prompt.txt",
        LESSON8_DIR / "validate_market_code.py",
        LESSON8_DIR / "lesson8_test_inputs.txt",
        LESSON8_DIR / "check_with_yfinance.py",
        LESSON8_DIR / "check_with_local_csv.py",
        LESSON8_DIR / "pipeline.py",
        PROJECT_ROOT / ".env.example",
    ]
    for index, path in enumerate(files, start=1):
        print(f"{index}. {path.relative_to(PROJECT_ROOT)}")

    print()
    print("第8课 Dify 网页端工作流结构：")
    print()
    print("Start")
    print("输入 taco_probability / confidence / domain")
    print("↓")
    print("LLM Market Reasoning")
    print("使用 market_prompt.txt")
    print("↓")
    print("Code Validate Market Output")
    print("使用 validate_market_code.py")
    print("↓")
    print("End")
    print("输出 direction_uso / direction_gld / direction_spy / key_assets / magnitude / reasoning")

    print()
    print("推荐运行顺序：")
    print("1. python src/lesson8/lesson8_run_all.py")
    print("2. python src/lesson8/check_with_local_csv.py")
    print("3. python src/lesson8/check_with_yfinance.py")
    print("4. 配置 .env 后，老师可演示：")
    print("   python src/lesson8/pipeline.py")


if __name__ == "__main__":
    main()
