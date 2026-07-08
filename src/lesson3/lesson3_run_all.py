import subprocess
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
LESSON_DIR = PROJECT_ROOT / "src" / "lesson3"
SCRIPTS = [
    "read_market_data.py",
    "spy_trend.py",
    "four_assets_normalized.py",
    "taco_events.py",
    "correlation.py",
    "correlation_heatmap.py",
]


def main():
    """第3课批量运行入口，逐个执行脚本并显示状态。"""
    print("开始运行第3课：金融数据可视化与事件标注", flush=True)

    for script_name in SCRIPTS:
        script_path = LESSON_DIR / script_name
        print(f"\n正在运行：{script_name}", flush=True)

        if not script_path.exists():
            print(f"没有找到脚本：{script_path}")
            continue

        # 使用当前 Python 解释器运行，避免同一台电脑有多个 Python 版本时混乱。
        result = subprocess.run([sys.executable, str(script_path)], cwd=PROJECT_ROOT)
        if result.returncode == 0:
            print(f"{script_name} 运行结束。", flush=True)
        else:
            print(f"{script_name} 返回非 0 状态码：{result.returncode}", flush=True)
            print("已继续运行后续脚本，请查看上方中文提示定位原因。", flush=True)

    print("\n第3课核心产出包括：", flush=True)
    print("data/spy_trend.png", flush=True)
    print("data/four_assets_normalized.png", flush=True)
    print("data/taco_events.png", flush=True)
    print("data/correlation_heatmap.png（如果 taco_cases.csv 可用）", flush=True)
    print("data/correlation_matrix.csv（如果 taco_cases.csv 可用）", flush=True)


if __name__ == "__main__":
    main()
