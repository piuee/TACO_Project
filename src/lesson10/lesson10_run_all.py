"""第10课本地运行说明。

这个文件不用启动 Streamlit，也不用调用 Dify。
运行后只打印第10课的课堂演示步骤。
"""

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data"
DOCS_DIR = PROJECT_ROOT / "docs"


def main() -> None:
    print("TACO 第10课：Streamlit 前端开发")
    print()
    print("本节课目标：")
    print("把第9课 FastAPI 后端 POST /analyze 接入 Streamlit 前端页面。")
    print()
    print("本地文件：")
    files = [
        "frontend/streamlit_app.py",
        "src/lesson10/test_backend_connection.py",
        "src/lesson10/sample_statements.txt",
        "docs/frontend_streamlit_steps.md",
        "docs/frontend_test_log.md",
        "docs/frontend_homework.md",
    ]
    for index, path in enumerate(files, start=1):
        print(f"{index}. {path}")

    print()
    print("运行步骤：")
    print()
    print("终端 1：启动后端")
    print()
    print("cd D:\\TACO\\TACO_Project")
    print("python -m uvicorn app.main:app --reload")
    print()
    print("终端 2：启动前端")
    print()
    print("cd D:\\TACO\\TACO_Project")
    print("streamlit run frontend/streamlit_app.py")
    print()
    print("测试地址：")
    print()
    print("FastAPI:")
    print("http://127.0.0.1:8000/health")
    print("http://127.0.0.1:8000/docs")
    print()
    print("Streamlit:")
    print("http://localhost:8501")
    print()
    print("提示：")
    print("* 后端和前端需要同时运行。")
    print("* 如果后端没启动，前端会提示无法连接后端。")
    print("* 前端不处理 Dify API Key。")
    print("* 本项目不是投资建议。")


if __name__ == "__main__":
    main()
