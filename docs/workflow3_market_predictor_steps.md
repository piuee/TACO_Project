# TACO 第8课：Dify 工作流 3——市场影响预测

用途：本文件说明第8课 Dify Workflow 3 的网页端搭建步骤，供学生手动操作时参考。

## 一、本节课目标

使用第7课输出的 taco_probability、confidence 和 domain，预测 USO、GLD、SPY 在未来 5 个交易日的可能方向。

## 二、工作流结构

Start
输入 taco_probability / confidence / domain

LLM Market Reasoning
根据 TACO 概率、置信度和领域推断市场方向

Code Validate Market Output
清洗 JSON，保证方向字段只包含 up / down / sideways

End
输出 direction_uso / direction_gld / direction_spy / key_assets / magnitude / reasoning

## 三、Dify 操作步骤

1. 打开 Dify。
2. 进入 Studio。
3. Create from Blank。
4. 选择 Workflow。
5. 应用名称建议：TACO Market Impact Predictor。
6. 配置 Start 节点，添加：

   * taco_probability
   * confidence
   * domain
7. 添加 LLM 节点，粘贴 src/lesson8/market_prompt.txt。
8. 添加 Code 节点，粘贴 src/lesson8/validate_market_code.py。
9. 配置 End 节点，输出：

   * direction_uso
   * direction_gld
   * direction_spy
   * key_assets
   * magnitude
   * reasoning
10. 使用 src/lesson8/lesson8_test_inputs.txt 中的三组数据测试。

## 四、测试要求

至少测试三组：

A：低 TACO 概率
B：中等 TACO 概率
C：高 TACO 概率

每组记录：

* taco_probability
* confidence
* domain
* direction_uso
* direction_gld
* direction_spy
* key_assets
* magnitude
* reasoning
* 是否合理

## 五、注意事项

* 本项目不是投资建议。
* direction 只能是 up / down / sideways。
* magnitude 只能是 low / mid / high。
* 如果 confidence 是 low，方向应该更保守。
* 如果 taco_probability 在 30 到 70 之间，方向通常应偏 sideways。
* 不要把 Dify API Key 写进代码。
* 不要把 .env 上传到 GitHub。
