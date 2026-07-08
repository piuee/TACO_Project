"""第11课部署说明脚本。

这个文件不用调用 Dify，也不用操作 GitHub 或 Streamlit Cloud。
运行后只打印第11课部署说明，适合课堂演示。
"""

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data"
DOCS_DIR = PROJECT_ROOT / "docs"


def main() -> None:
    print("TACO 第11课：系统整合与部署上线")
    print()
    print("本节课目标：")
    print("把本地 Streamlit Web App 部署到 Streamlit Cloud，获得公开 URL。")
    print()
    print("本地文件：")
    files = [
        "frontend/streamlit_cloud_app.py",
        "docs/deployment_streamlit_cloud_steps.md",
        "docs/streamlit_secrets_template.md",
        "docs/deployment_checklist.md",
        "docs/deployment_log.md",
    ]
    for index, path in enumerate(files, start=1):
        print(f"{index}. {path}")

    print()
    print("本节课云端架构：")
    print()
    print("Streamlit Cloud")
    print("↓")
    print("Dify API")
    print("↓")
    print("Dify 三个工作流")
    print()
    print("注意：")
    print("* 云端版不调用本地 FastAPI。")
    print("* 云端版不使用 http://127.0.0.1:8000/analyze。")
    print("* Streamlit Cloud 主文件路径填写：")
    print("  frontend/streamlit_cloud_app.py")
    print("* Secrets 在 Streamlit Cloud 后台配置，不写进代码。")
    print("* 不要上传 .env。")
    print("* 不要上传 .streamlit/secrets.toml。")
    print("* 本项目不是投资建议。")


if __name__ == "__main__":
    main()
