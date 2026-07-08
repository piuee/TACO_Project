"""第12课收官说明脚本。

这个文件不用调用 Dify，不用运行 Streamlit，不用操作 GitHub。
运行后只打印第12课 Demo Day 的最终材料说明。
"""

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data"
DOCS_DIR = PROJECT_ROOT / "docs"


def main() -> None:
    print("TACO 第12课：Demo Day——项目演讲与申请落地")
    print()
    print("本节课目标：")
    print()
    print("1. 录制 3 分钟 Demo 视频")
    print("2. 完成项目英文介绍")
    print("3. 完成 Common App 活动描述")
    print("4. 整理最终项目材料")
    print("5. 为作品集和申请材料做准备")
    print()
    print("最终材料：")
    print()
    files = [
        "docs/demo_video_script.md",
        "docs/presentation_pitches.md",
        "docs/common_app_activity.txt",
        "docs/final_project_summary.md",
        "docs/demo_video_link.md",
        "docs/project_portfolio_checklist.md",
        "docs/final_project_checklist.md",
        "docs/next_steps.md",
    ]
    for index, path in enumerate(files, start=1):
        print(f"{index}. {path}")

    print()
    print("提醒：")
    print()
    print("* 不要展示 API Key。")
    print("* 不要展示 .env。")
    print("* 不要展示 Streamlit Secrets 页面。")
    print("* Demo 视频要展示公开 URL。")
    print("* 本项目仅用于事件影响方向性分析，不构成投资建议。")


if __name__ == "__main__":
    main()
