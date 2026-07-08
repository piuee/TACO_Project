# TACO 第8课作业

用途：本文件说明第8课的轻量作业要求。

## 作业 1：提交 Workflow 3 截图

提交一张 Dify 工作流完整截图，要求能看到：

Start
LLM
Code
End

建议保存为：

docs/workflow3_market_predictor.png

## 作业 2：完成三组概率测试

使用 src/lesson8/lesson8_test_inputs.txt 中的三组测试数据，在 Dify 中运行 Workflow 3，并填写：

docs/workflow3_test_log.md

## 作业 3：完成一次市场方向对账

运行以下两个脚本中的至少一个：

python src/lesson8/check_with_local_csv.py

或：

python src/lesson8/check_with_yfinance.py

填写：

docs/market_backtest_log.md

## 作业 4：写 3-5 句话分析

回答：

1. 高 TACO 概率时，市场方向是否更偏乐观？
2. 低 TACO 概率时，SPY 是否更容易 down？
3. AI 预测和真实市场方向是否完全一致？
4. 为什么这个项目不是投资建议？
