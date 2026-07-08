# TACO 第9课作业

用途：本文件说明第9课的轻量作业要求。

## 作业 1：提交 /health 截图

启动后端：

python -m uvicorn app.main:app --reload

浏览器打开：

http://127.0.0.1:8000/health

截图保存为：

docs/health_check.png

## 作业 2：用 Swagger UI 测试 3 条言论

浏览器打开：

http://127.0.0.1:8000/docs

测试：

1. Trump threatens to impose 25% tariffs on imported goods next week.
2. Trump says he may delay the tariff plan and continue negotiations.
3. We might do something big next week.

截图保存为：

docs/analyze_test_1.png
docs/analyze_test_2.png
docs/analyze_test_3.png

## 作业 3：填写测试记录表

填写：

docs/backend_test_log.md

## 作业 4：回答问题

用 3-5 句话回答：

1. FastAPI 在 TACO 项目中负责什么？
2. 为什么前端不应该直接调用 Dify？
3. 为什么 API Key 要放在 .env？
4. try / except 在后端中有什么作用？
