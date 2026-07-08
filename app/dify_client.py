"""第9课：Dify 三个 Workflow 的调用封装。

本文件只从项目根目录的 .env 读取配置，不包含任何真实 API Key。
课堂重点是理解：后端负责保管密钥，并把三个 Dify 工作流串联起来。
"""

import os
from pathlib import Path
from typing import Any

import requests
from dotenv import load_dotenv


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
DOCS_DIR = PROJECT_ROOT / "docs"
ENV_PATH = PROJECT_ROOT / ".env"
DIFY_API_URL = "https://api.dify.ai/v1/workflows/run"


def check_env() -> dict[str, str]:
    """检查 Dify 调用需要的环境变量是否齐全。"""
    load_dotenv(ENV_PATH)

    required_keys = ["DIFY_API_KEY", "WF1_ID", "WF2_ID", "WF3_ID"]
    values = {key: os.getenv(key, "").strip() for key in required_keys}
    missing = [key for key, value in values.items() if not value]

    if missing:
        raise RuntimeError(
            "缺少环境变量："
            + "、".join(missing)
            + "。请复制 .env.example 为 .env，并填写自己的 Dify 配置。"
        )

    return values


def call_workflow(workflow_id: str, inputs: dict[str, Any]) -> dict[str, Any]:
    """调用一个 Dify Workflow，并返回 outputs。"""
    env_values = check_env()

    headers = {
        "Authorization": f"Bearer {env_values['DIFY_API_KEY']}",
        "Content-Type": "application/json",
    }
    payload = {
        "workflow_id": workflow_id,
        "inputs": inputs,
        "response_mode": "blocking",
        "user": "taco-api",
    }

    response = requests.post(DIFY_API_URL, headers=headers, json=payload, timeout=60)
    response.raise_for_status()

    data = response.json()

    try:
        outputs = data["data"]["outputs"]
    except (KeyError, TypeError) as exc:
        raise RuntimeError("Dify 返回格式不符合预期。") from exc

    if not isinstance(outputs, dict):
        raise RuntimeError("Dify 返回格式不符合预期。")

    return outputs


def require_fields(data: dict[str, Any], fields: list[str], label: str) -> None:
    """检查上一个工作流输出是否包含下一个工作流需要的字段。"""
    missing = [field for field in fields if field not in data]

    if missing:
        raise RuntimeError(f"{label} 缺少必要字段：{', '.join(missing)}。")


def run_full_taco_analysis(statement: str) -> dict[str, Any]:
    """串联三个 Dify Workflow，返回完整 TACO 分析结果。"""
    env_values = check_env()

    classification = call_workflow(
        env_values["WF1_ID"],
        {
            "trump_statement": statement,
        },
    )
    require_fields(classification, ["hardness", "domain", "reasoning"], "Workflow 1 输出")

    probability = call_workflow(
        env_values["WF2_ID"],
        {
            "hardness": classification["hardness"],
            "domain": classification["domain"],
            "reasoning": classification["reasoning"],
        },
    )
    require_fields(
        probability,
        ["taco_probability", "confidence"],
        "Workflow 2 输出",
    )

    market_prediction = call_workflow(
        env_values["WF3_ID"],
        {
            "taco_probability": probability["taco_probability"],
            "confidence": probability["confidence"],
            "domain": classification["domain"],
        },
    )

    return {
        "statement": statement,
        "classification": classification,
        "taco_probability": probability,
        "market_prediction": market_prediction,
    }
