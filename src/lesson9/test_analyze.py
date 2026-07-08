"""第9课：测试本地 FastAPI 的 POST /analyze 接口。

运行前请先启动后端，并确认 .env 已配置。
本脚本不会写入或读取任何真实 API Key。
"""

import json
from pathlib import Path

import requests


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data"
DOCS_DIR = PROJECT_ROOT / "docs"
SAMPLE_PATH = PROJECT_ROOT / "src" / "lesson9" / "sample_requests.json"
ANALYZE_URL = "http://127.0.0.1:8000/analyze"


def main() -> None:
    try:
        samples = json.loads(SAMPLE_PATH.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"读取测试样例失败：{exc}")
        return

    for sample in samples:
        print("\n==============================")
        print(f"测试名称：{sample.get('name', '未命名测试')}")

        try:
            response = requests.post(
                ANALYZE_URL,
                headers={"Content-Type": "application/json"},
                json=sample["request"],
                timeout=90,
            )
        except requests.ConnectionError:
            print("无法连接后端，请先运行：python -m uvicorn app.main:app --reload")
            return
        except requests.RequestException as exc:
            print(f"请求 /analyze 失败：{exc}")
            continue

        print(f"状态码：{response.status_code}")

        try:
            result = response.json()
            print("返回结果：")
            print(json.dumps(result, ensure_ascii=False, indent=2))
        except ValueError:
            print("返回结果不是有效 JSON：")
            print(response.text)

        if response.status_code == 500:
            print("请检查：")
            print("* .env 是否配置")
            print("* DIFY_API_KEY 是否正确")
            print("* WF1_ID / WF2_ID / WF3_ID 是否正确")
            print("* Dify Workflow 是否已发布")

        if response.status_code in {400, 422}:
            print("请检查请求体字段是否是 statement。")


if __name__ == "__main__":
    main()
