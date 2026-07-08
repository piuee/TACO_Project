# TACO 第9课：FastAPI 后端开发步骤

用途：本文件说明第9课 FastAPI 后端的创建、启动和测试方法。

## 一、本节课目标

把第8课的完整 TACO 分析链路封装成一个后端接口：

POST /analyze

输入：

{
"statement": "Trump threatens to impose 25% tariffs on imported goods next week."
}

输出：

classification
taco_probability
market_prediction

## 二、后端结构

app/models.py
定义 AnalyzeRequest，请求体必须包含 statement。

app/dify_client.py
封装 Dify 三个 Workflow 的调用。

app/main.py
创建 FastAPI 应用，提供 /health 和 /analyze。

## 三、安装依赖

pip install fastapi uvicorn requests python-dotenv

如果网络慢：

pip install fastapi uvicorn requests python-dotenv -i https://pypi.tuna.tsinghua.edu.cn/simple

## 四、配置 .env

复制：

.env.example

为：

.env

填写：

DIFY_API_KEY
WF1_ID
WF2_ID
WF3_ID

注意：

不要把 .env 上传到 GitHub。
不要截图公开展示 API Key。
不要把 API Key 写进 Python 文件。

## 五、启动后端

从项目根目录运行：

cd D:\TACO\TACO_Project
python -m uvicorn app.main:app --reload

看到：

Application startup complete

说明启动成功。

## 六、测试 /health

浏览器打开：

http://127.0.0.1:8000/health

期望返回：

{
"status": "ok",
"version": "1.0.0"
}

## 七、测试 Swagger UI

浏览器打开：

http://127.0.0.1:8000/docs

步骤：

1. 找到 POST /analyze。
2. 点击 Try it out。
3. 输入 JSON。
4. 点击 Execute。
5. 查看 Response Code 和 Response Body。

## 八、测试输入

{
"statement": "Trump threatens to impose 25% tariffs on imported goods next week."
}

{
"statement": "Trump says he may delay the tariff plan and continue negotiations."
}

{
"statement": "We might do something big next week."
}

## 九、状态码说明

200：成功。
400：statement 为空。
422：请求体格式不对，例如没有 statement 字段。
500：服务器内部错误，可能是 .env、API Key、Workflow ID 或 Dify 返回格式问题。
504：Dify API 超时。

## 十、常见问题

1. ModuleNotFoundError: No module named app
   请确认从项目根目录运行：
   python -m uvicorn app.main:app --reload

2. /docs 打不开
   请确认 uvicorn 是否启动成功。

3. /analyze 返回 500
   请检查 .env、API Key、Workflow ID、Dify Workflow 是否发布。

4. /analyze 返回 504
   Dify 响应超时，请稍后重试或检查网络。

5. /analyze 返回 422
   请求 JSON 必须包含 statement 字段。
