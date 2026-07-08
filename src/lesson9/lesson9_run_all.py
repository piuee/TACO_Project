"""第9课本地运行说明。

这个文件不用启动 FastAPI，也不用调用 Dify。
运行后只打印第9课的课堂演示步骤。
"""

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data"
DOCS_DIR = PROJECT_ROOT / "docs"


def main() -> None:
    print("TACO 第9课：FastAPI 后端开发")
    print()
    print("本节课目标：")
    print("把第8课的完整 TACO 分析链路封装成 POST /analyze 接口。")
    print()
    print("本地文件：")
    files = [
        "app/models.py",
        "app/dify_client.py",
        "app/main.py",
        "src/lesson9/test_health.py",
        "src/lesson9/test_analyze.py",
        "docs/backend_fastapi_steps.md",
        "docs/backend_test_log.md",
    ]
    for index, path in enumerate(files, start=1):
        print(f"{index}. {path}")

    print()
    print("推荐运行顺序：")
    print()
    print("1. 安装依赖：")
    print("   pip install fastapi uvicorn requests python-dotenv")
    print()
    print("2. 检查 .env.example，并复制为 .env 填入真实信息：")
    print("   DIFY_API_KEY")
    print("   WF1_ID")
    print("   WF2_ID")
    print("   WF3_ID")
    print()
    print("3. 从项目根目录启动 FastAPI：")
    print("   python -m uvicorn app.main:app --reload")
    print()
    print("4. 浏览器打开：")
    print("   http://127.0.0.1:8000/health")
    print("   http://127.0.0.1:8000/docs")
    print()
    print("5. 在 Swagger UI 中测试 POST /analyze。")
    print()
    print("提示：")
    print("* Codex 不处理真实 API Key。")
    print("* 不要把 .env 上传 GitHub。")
    print("* 如果没有配置 .env，/health 仍然可以测试，但 /analyze 会返回环境变量缺失的错误。")
    print("* 本项目不是投资建议。")


if __name__ == "__main__":
    main()
