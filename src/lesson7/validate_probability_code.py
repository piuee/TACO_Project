# 用途：第7课 Dify 工作流中 Code 节点要粘贴的 Python 代码。
# 说明：这个文件不是为了本地运行，而是方便老师和学生复制到 Dify Code 节点。
# 注意：不要在这里填写 Dify API Key，也不要写调用 Dify API 的代码。

import json
import re


def main(llm_output: str) -> dict:
    """
    清洗 LLM 概率引擎的输出，保证最终结果稳定。

    输入：
        llm_output: LLM② 的原始输出文本

    输出：
        taco_probability: 0-100 的整数
        confidence: high / med / low
        reasoning: 简短理由
        key_cases: 支撑案例列表
    """

    try:
        # 1. 清理前后空格
        text = str(llm_output).strip()

        # 2. 去掉 markdown 代码块，例如 ```json ... ```
        text = re.sub(r"```json|```", "", text).strip()

        # 3. 如果 LLM 输出前后有多余文字，尝试提取第一个 JSON 对象
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            text = match.group(0)

        # 4. 解析 JSON
        data = json.loads(text)

        # 5. 读取 taco_probability，默认 50
        prob = data.get("taco_probability", 50)

        # 如果是 "73%" 字符串，去掉百分号
        if isinstance(prob, str):
            prob = prob.replace("%", "").strip()

        prob = float(prob)

        # 如果模型输出 0.73 或 0.8，自动转换成 73 或 80
        if prob <= 1.0:
            prob = prob * 100

        # 限制在 0-100
        prob = max(0, min(100, prob))

        # 6. 规范 confidence
        confidence = str(data.get("confidence", "low")).lower().strip()

        if confidence == "medium":
            confidence = "med"

        valid_confidence = ["high", "med", "low"]

        if confidence not in valid_confidence:
            confidence = "low"

        # 7. 获取 reasoning
        reasoning = data.get("reasoning", "")

        if not reasoning:
            reasoning = "模型未提供明确理由。"

        # 8. 获取 key_cases
        key_cases = data.get("key_cases", [])

        if not isinstance(key_cases, list):
            key_cases = [str(key_cases)]

        return {
            "taco_probability": int(round(prob)),
            "confidence": confidence,
            "reasoning": reasoning,
            "key_cases": key_cases,
        }

    except Exception:
        # 解析失败时，返回安全默认值
        # 50% 表示不确定，比返回 0% 更合理
        return {
            "taco_probability": 50,
            "confidence": "low",
            "reasoning": "LLM 输出解析失败，使用默认 50%。",
            "key_cases": [],
        }
