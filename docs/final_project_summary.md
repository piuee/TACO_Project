# TACO Radar 最终项目总结

## 一、项目简介

TACO Radar 是一个 AI 事件分析系统。用户输入特朗普相关政策言论后，系统会判断言论强硬度、检索历史 TACO 案例、估计 TACO 概率，并给出 USO、GLD、SPY 的市场方向判断。

本项目仅用于事件影响方向性分析和 AI 学习，不构成投资建议。

## 二、项目动机

特朗普相关政策言论经常影响市场情绪，但强硬言论最后不一定真正执行。TACO Radar 尝试用历史案例、RAG 检索和 AI 工作流，帮助分析一条新言论是否可能出现软化、推迟或反转。

## 三、技术栈

* Python
* Pandas
* Matplotlib
* Dify Knowledge
* Dify Workflow
* RAG
* FastAPI
* Streamlit
* Streamlit Cloud
* GitHub

## 四、系统架构

数据层：

* 历史 TACO 案例
* 市场数据
* 新闻和言论文本

AI 分析层：

* Workflow 1：Statement Classifier
* Workflow 2：TACO Probability Engine
* Workflow 3：Market Impact Predictor
* Dify Knowledge / RAG 检索
* Code 节点 JSON 清洗

应用层：

* FastAPI 后端
* Streamlit 前端
* Streamlit Cloud 部署

## 五、核心功能

1. 输入 Trump 相关言论。
2. 判断 hardness 和 domain。
3. 检索相似历史案例。
4. 输出 TACO probability 和 confidence。
5. 输出 USO、GLD、SPY 的方向判断。
6. 展示完整 JSON 和历史记录。
7. 部署为公开 Web App。

## 六、项目成果

* GitHub 仓库：
* Streamlit Cloud 公开 URL：
* Demo 视频：
* 主要截图：
* Common App 活动描述：

## 七、最大挑战

最大挑战是让 LLM 的输出稳定。因为 LLM 有时会输出多余解释、markdown 代码块、错误 JSON 或缺少字段。为了解决这个问题，项目在每个关键 LLM 节点后加入 Code 节点，用 Python 清洗 JSON、限制字段范围，并在解析失败时返回安全默认值。

## 八、学习收获

通过这个项目，我学习了如何从一个想法出发，完成数据处理、RAG 知识库、AI 工作流、后端 API、前端页面和云端部署。这个项目让我理解了 AI 产品开发不仅是写 Prompt，而是要把不稳定的模型输出变成稳定、可运行、可展示的系统。
