"""第10课：测试 FastAPI 后端是否在线。

本脚本只请求 /health，不调用 /analyze，不调用 Dify，也不需要 API Key。
"""

import requests


HEALTH_URL = "http://127.0.0.1:8000/health"


def main() -> None:
    try:
        response = requests.get(HEALTH_URL, timeout=5)
    except requests.ConnectionError:
        print("无法连接后端，请先运行：")
        print("python -m uvicorn app.main:app --reload")
        return
    except requests.RequestException as exc:
        print(f"测试后端连接失败：{exc}")
        return

    print(f"状态码：{response.status_code}")

    try:
        print("返回 JSON：")
        print(response.json())
    except ValueError:
        print("后端没有返回有效 JSON：")
        print(response.text)


if __name__ == "__main__":
    main()
