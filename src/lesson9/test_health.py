"""第9课：测试本地 FastAPI 的 /health 接口。

本脚本不调用 Dify，不需要 API Key。
运行前请先启动后端：
python -m uvicorn app.main:app --reload
"""

import requests


HEALTH_URL = "http://127.0.0.1:8000/health"


def main() -> None:
    try:
        response = requests.get(HEALTH_URL, timeout=5)
    except requests.ConnectionError:
        print("无法连接后端，请先运行：python -m uvicorn app.main:app --reload")
        return
    except requests.RequestException as exc:
        print(f"请求 /health 失败：{exc}")
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
