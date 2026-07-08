# TACO 第10课：前后端架构说明

用途：本文件解释第10课 Streamlit 前端和 FastAPI 后端之间的关系。

## 一、完整链路

用户
↓
Streamlit 前端
↓
FastAPI 后端 POST /analyze
↓
Dify 三个工作流
↓
FastAPI 返回 JSON
↓
Streamlit 展示指标卡和图表

## 二、前端负责什么

* 输入框
* 按钮
* 加载提示
* 指标卡
* 图表
* 历史记录
* 错误提示

## 三、后端负责什么

* 接收 statement
* 调用 Dify 三个工作流
* 处理 API Key
* 处理错误
* 返回统一 JSON

## 四、为什么前端不直接调用 Dify

1. 避免暴露 API Key。
2. 保持前端简单。
3. 方便后续替换模型或工作流。
4. 统一处理错误。
5. 方便第11课部署。

## 五、两个终端

终端 1：

python -m uvicorn app.main:app --reload

终端 2：

streamlit run frontend/streamlit_app.py

两个终端必须同时运行。
