"""第10课：Streamlit 前端页面。

本页面只调用第9课 FastAPI 后端，不直接调用 Dify，也不处理 API Key。
运行方式：
streamlit run frontend/streamlit_app.py
"""

import os

import matplotlib.pyplot as plt
import requests
import streamlit as st


# API_URL 可以通过环境变量覆盖，默认连接本地 FastAPI 后端。
API_URL = os.getenv("TACO_API_URL", "http://127.0.0.1:8000/analyze")


def safe_probability(value) -> float:
    """把概率安全转换为 0-100 之间的数字。"""
    try:
        prob = float(value)
    except (TypeError, ValueError):
        return 0.0

    return max(0.0, min(100.0, prob))


def probability_label(prob) -> str:
    """根据 TACO 概率返回中文标签。"""
    try:
        prob_value = float(prob)
    except (TypeError, ValueError):
        return "未知概率"

    if prob_value > 70:
        return "高 TACO 概率"
    if 30 <= prob_value <= 70:
        return "中等不确定"
    return "低 TACO 概率"


def normalize_direction(direction) -> str:
    """把市场方向限制为 up / down / sideways。"""
    value = str(direction).lower().strip()
    if value in {"up", "down", "sideways"}:
        return value
    return "sideways"


def call_backend(statement: str) -> dict:
    """调用 FastAPI 后端 POST /analyze。"""
    response = requests.post(
        API_URL,
        json={"statement": statement},
        timeout=90,
    )
    response.raise_for_status()
    return response.json()


def plot_market_prediction(market_prediction: dict) -> None:
    """把 USO / GLD / SPY 的方向转换成柱状图。"""
    assets = ["USO 石油", "GLD 黄金", "SPY 标普"]
    fields = ["direction_uso", "direction_gld", "direction_spy"]
    direction_map = {
        "up": 1,
        "sideways": 0,
        "down": -1,
    }
    color_map = {
        "up": "green",
        "sideways": "gray",
        "down": "red",
    }

    directions = [
        normalize_direction(market_prediction.get(field, "sideways"))
        for field in fields
    ]
    values = [direction_map[direction] for direction in directions]
    colors = [color_map[direction] for direction in directions]

    fig, ax = plt.subplots(figsize=(7, 4))
    bars = ax.bar(assets, values, color=colors)
    ax.set_title("Market Impact Prediction")
    ax.set_ylim(-1.5, 1.5)
    ax.set_yticks([-1, 0, 1])
    ax.set_yticklabels(["down", "sideways", "up"])
    ax.axhline(0, color="black", linewidth=0.8)

    for bar, direction in zip(bars, directions):
        y = bar.get_height()
        text_y = y + 0.12 if y >= 0 else y - 0.18
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            text_y,
            direction,
            ha="center",
            va="center",
        )

    st.pyplot(fig)
    plt.close(fig)


def add_to_history(result: dict) -> None:
    """把本次分析结果放入最近 5 次历史记录。"""
    st.session_state["history"].insert(0, result)
    st.session_state["history"] = st.session_state["history"][:5]


# session_state 初始化
if "result" not in st.session_state:
    st.session_state["result"] = None

if "history" not in st.session_state:
    st.session_state["history"] = []


# 页面标题区
st.set_page_config(page_title="TACO雷达", layout="wide")
st.title("TACO雷达")
st.caption("AI追踪特朗普言论，分析 TACO 概率与市场影响")


# 输入区
statement = st.text_area(
    "输入特朗普言论 Statement",
    placeholder="Paste a Trump statement here...",
    height=130,
)

button_col1, button_col2 = st.columns([1, 1])

with button_col1:
    analyze_clicked = st.button("开始分析 / Analyze", type="primary")

with button_col2:
    clear_clicked = st.button("清空结果 / Clear")


# 按钮逻辑
if clear_clicked:
    st.session_state["result"] = None
    st.session_state["history"] = []
    st.success("结果已清空。")

if analyze_clicked:
    clean_statement = statement.strip()

    if not clean_statement:
        st.warning("请先输入一条 Trump 相关言论。")
    else:
        with st.spinner("AI分析中，请稍候..."):
            try:
                result = call_backend(clean_statement)
                st.session_state["result"] = result
                add_to_history(result)
            except requests.exceptions.ConnectionError:
                st.error("无法连接后端。请先启动 FastAPI：python -m uvicorn app.main:app --reload")
            except requests.exceptions.Timeout:
                st.error("请求超时。Dify 工作流可能响应较慢，请稍后重试。")
            except requests.exceptions.HTTPError as error:
                detail = None
                try:
                    detail = error.response.json().get("detail")
                except Exception:
                    detail = str(error)
                st.error(f"后端返回错误：{error.response.status_code}｜{detail}")
            except Exception as error:
                st.error(f"分析失败：{error}")


# 结果展示区
result = st.session_state["result"]

if result:
    st.subheader("核心分析结果")

    classification = result.get("classification", {})
    probability_info = result.get("taco_probability", {})
    market_prediction = result.get("market_prediction", {})

    hardness = classification.get("hardness", "N/A")
    domain = classification.get("domain", "N/A")
    prob = probability_info.get("taco_probability", 0)
    confidence = probability_info.get("confidence", "N/A")
    magnitude = market_prediction.get("magnitude", "N/A")

    prob_value = safe_probability(prob)

    metric_col1, metric_col2, metric_col3 = st.columns(3)

    with metric_col1:
        st.metric("强硬度 Hardness", f"{hardness}/10")
        st.caption(f"领域 Domain：{domain}")

    with metric_col2:
        st.metric("TACO概率", f"{prob_value:.0f}%")
        st.progress(prob_value / 100)
        st.caption(probability_label(prob))

    with metric_col3:
        st.metric("置信度 Confidence", confidence)
        st.caption(f"影响强度 Magnitude：{magnitude}")

    st.subheader("市场影响预测")
    market_col1, market_col2, market_col3 = st.columns(3)

    direction_uso = normalize_direction(market_prediction.get("direction_uso", "sideways"))
    direction_gld = normalize_direction(market_prediction.get("direction_gld", "sideways"))
    direction_spy = normalize_direction(market_prediction.get("direction_spy", "sideways"))

    with market_col1:
        st.metric("USO 石油", direction_uso)
    with market_col2:
        st.metric("GLD 黄金", direction_gld)
    with market_col3:
        st.metric("SPY 标普", direction_spy)

    plot_market_prediction(market_prediction)

    st.subheader("分析理由")
    st.markdown("**言论分类理由**")
    st.write(classification.get("reasoning", "无"))
    st.markdown("**TACO 概率理由**")
    st.write(probability_info.get("reasoning", "无"))
    st.markdown("**市场方向理由**")
    st.write(market_prediction.get("reasoning", "无"))

    key_cases = probability_info.get("key_cases", [])
    if isinstance(key_cases, str):
        key_cases = [key_cases]

    if isinstance(key_cases, list) and key_cases:
        st.subheader("关键历史案例")
        for index, case in enumerate(key_cases, start=1):
            st.write(f"{index}. {case}")

    with st.expander("查看完整 JSON 返回结果"):
        st.json(result)


# 历史记录区
if st.session_state["history"]:
    st.subheader("最近 5 次分析记录")

    for index, item in enumerate(st.session_state["history"], start=1):
        classification = item.get("classification", {})
        probability_info = item.get("taco_probability", {})
        statement_text = str(item.get("statement", ""))
        short_statement = statement_text[:80]
        if len(statement_text) > 80:
            short_statement += "..."

        domain = classification.get("domain", "N/A")
        prob = probability_info.get("taco_probability", "N/A")
        st.write(f"{index}. [{domain}] TACO概率：{prob}%｜{short_statement}")


# 底部说明
st.caption("提示：本项目仅用于事件影响方向性分析，不构成投资建议。")
