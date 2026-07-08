# Lesson 9 - FastAPI Backend Test Log

本文件记录第 9 课 FastAPI 后端接口测试结果。

测试接口：

```text
POST /analyze
```

测试地址：

```text
http://127.0.0.1:8000/docs
```

健康检查接口：

```text
GET /health
```

健康检查结果：

```json
{
  "status": "ok",
  "version": "1.0.0"
}
```

---

## Test Summary

| Test | Input Statement | Status Code | Classification | TACO Probability | Market Prediction | Result |
|---|---|---:|---|---|---|---|
| 1 | Trump threatens to impose 25% tariffs on imported goods next week. | 200 | hardness=8, domain=tariff | 30, confidence=med | USO down, GLD up, SPY down, magnitude=med | Success |
| 2 | Trump says he may delay the tariff plan and continue negotiations. | 200 | hardness=2, domain=tariff | 90, confidence=high | USO down, GLD up, SPY down, magnitude=low | Success |
| 3 | We might do something big next week. | 200 | returned complete classification | returned complete probability result | returned complete market prediction | Success |

---

## Test 1 - Strong Tariff Threat

### Request Body

```json
{
  "statement": "Trump threatens to impose 25% tariffs on imported goods next week."
}
```

### Response Summary

```text
Status Code: 200

classification:
- hardness: 8
- domain: tariff
- reasoning: 这句话包含25%的关税和下周执行的具体时间，威胁性很强，属于强硬关税施压。

taco_probability:
- taco_probability: 30
- confidence: med
- reasoning: 多数相似案例最终坚持执行关税威胁，结果为 HOLD；但历史上也存在软化先例。

market_prediction:
- USO: down
- GLD: up
- SPY: down
- key assets: SPY, GLD
- magnitude: med
```

### Observation

这条言论属于强硬关税威胁，模型识别为 `tariff` 领域，强硬度较高。由于 TACO 概率较低，系统认为该威胁更可能对市场造成较明显冲击，因此 SPY 偏下跌、GLD 偏上涨、USO 偏下跌。

---

## Test 2 - Softening and Negotiation

### Request Body

```json
{
  "statement": "Trump says he may delay the tariff plan and continue negotiations."
}
```

### Response Body

```json
{
  "statement": "Trump says he may delay the tariff plan and continue negotiations.",
  "classification": {
    "hardness": 2,
    "domain": "tariff",
    "reasoning": "这句话表示可能推迟关税计划并继续谈判，语气软化，没有具体措施或时间。"
  },
  "taco_probability": {
    "taco_probability": 90,
    "confidence": "high",
    "reasoning": "当前陈述硬度2、领域关税，与历史案例中2025年2月3日暂停加墨关税（硬度2）高度相似，且所有三个检索到的关税案例最终均出现TACO（软化、推迟或让步），历史模式高度一致，因此TACO概率极高。",
    "key_cases": [
      "2025-02-03 暂停加墨关税30天（硬度2）",
      "2025-04-23 暗示大幅降低对华关税（硬度3）"
    ]
  },
  "market_prediction": {
    "summary": "Market Impact Prediction\n\nUSO: down\nGLD: up\nSPY: down\n\nKey assets: SPY, GLD\nMagnitude: low\n\nReasoning:\nHigh tariff pressure typically triggers risk-off, but high taco probability (90) suggests markets expect policy reversal, softening impacts.\n"
  }
}
```

### Observation

这条言论包含 `may delay` 和 `continue negotiations`，语气明显软化，所以强硬度较低。系统检索到的历史案例大多属于软化、推迟或让步，因此 TACO 概率较高。市场影响幅度为 `low`，说明系统认为市场冲击会被软化预期削弱。

---

## Test 3 - Vague Statement

### Request Body

```json
{
  "statement": "We might do something big next week."
}
```

### Response Summary

```text
Status Code: 200

Expected behavior:
- The statement is vague and does not include a clear policy domain.
- The system still returned a complete JSON response.
- The result can be used to check whether the backend is stable for unclear inputs.
```

### Observation

这条言论非常模糊，没有明确领域、政策对象、执行方式或具体措施。系统仍然能够返回完整 JSON，说明后端接口具有一定稳定性。对于这类模糊输入，合理结果应该是较低置信度和较保守的市场方向判断。

---

## Backend Test Conclusion

第 9 课 FastAPI 后端测试通过。

已完成：

```text
1. /health 接口正常返回。
2. /docs Swagger UI 可以打开。
3. POST /analyze 可以接收 statement 输入。
4. 后端成功调用 Dify Workflow 1、Workflow 2、Workflow 3。
5. 接口返回完整 JSON，包括 classification、taco_probability、market_prediction。
6. 三组测试输入均返回 200。
```

完整链路如下：

```text
User / Swagger UI
↓
POST /analyze
↓
FastAPI Backend
↓
Workflow 1: Statement Classifier
↓
Workflow 2: TACO Probability Engine
↓
Workflow 3: Market Impact Prediction
↓
JSON Response
```

---

## Notes

本项目仅用于课程学习和事件影响方向性分析，不构成投资建议。

不要将 `.env`、Dify API Key 或任何密钥上传到 GitHub。