# TACO 第12课：三种听众的项目讲法

## 一、给父母讲：30 秒中文零术语版本

我做了一个 AI 分析工具，用户可以输入特朗普的一句话，系统会判断这句话有多强硬、他最后会不会软化，以及石油、黄金、美股可能怎么反应。它有一个公开网址，别人可以直接打开测试。这个项目不是投资建议，而是用 AI 学习新闻、历史案例和市场数据之间的关系。

## 二、给招生官讲：30-60 秒英文版本

I built TACO Radar, an AI-powered web app that analyzes Trump-related policy statements and estimates whether a strong statement is likely to be softened later. The system uses a three-stage pipeline: first, it classifies the statement by hardness and policy domain; second, it retrieves similar historical cases using a RAG knowledge base; third, it predicts possible market direction for oil, gold, and equities. I built the project with Python, Dify workflows, FastAPI, Streamlit, and deployed it on Streamlit Cloud with a public URL.

## 三、给技术同学讲：20-30 秒技术版本

这是一个 RAG + LLM pipeline。系统先用 Dify Workflow 做 few-shot statement classification，输出 hardness 和 domain；然后用 Knowledge Retrieval 在历史 TACO 案例中检索相似案例，估计 TACO probability 和 confidence；最后用第三个 workflow 输出 USO、GLD、SPY 的方向判断。前面用 FastAPI 封装过 /analyze 接口，最终用 Streamlit Cloud 做公开部署。

## 四、练习记录

| 听众   | 是否完成练习 | 是否超过时间 | 需要改进的地方 |
| ---- | ------ | ------ | ------- |
| 父母   |        |        |         |
| 招生官  |        |        |         |
| 技术同学 |        |        |         |

## 五、免责声明

本项目仅用于事件影响方向性分析，不构成投资建议。
