# TACO 第12课：3 分钟 Demo 视频脚本

## 一、视频结构

| 时间        | 内容   | 重点                 |
| --------- | ---- | ------------------ |
| 0:00-0:30 | 问题背景 | 为什么这个项目值得做         |
| 0:30-1:30 | 系统演示 | 打开公开 URL，输入言论，展示结果 |
| 1:30-2:30 | 技术讲解 | 数据层、AI 层、应用层       |
| 2:30-3:00 | 收尾总结 | 学到了什么，下一步怎么升级      |

## 二、英文 Demo 讲稿

0:00-0:30 问题背景：

Every time Trump makes a strong policy statement, markets react quickly.
But the difficult question is whether he will actually follow through, or later soften his position.
So I built TACO Radar, an AI web app that analyzes Trump-related statements, estimates TACO probability, and predicts possible market impact.

0:30-1:30 系统演示：

Here is the live app deployed on Streamlit Cloud.
I can paste a statement into the input box and click Analyze.
The system first classifies the statement by hardness and policy domain.
Then it retrieves similar historical cases from a RAG knowledge base.
Finally, it estimates the TACO probability and predicts directions for USO, GLD, and SPY.

1:30-2:30 技术讲解：

The system has three major layers.
The data layer includes historical TACO cases and market data.
The AI layer uses Dify workflows, few-shot prompting, RAG retrieval, and JSON validation.
The application layer includes FastAPI, Streamlit, and Streamlit Cloud deployment.
The key engineering challenge was making LLM outputs stable enough for a multi-step pipeline.

2:30-3:00 收尾总结：

Through this project, I learned how to turn an idea into a full AI product, from data and prompts to backend, frontend, and deployment.
Next, I want to add scheduled news fetching and expand the historical case database, so the system can track new political statements automatically.

## 三、中文 Demo 讲稿

0:00-0:30 问题背景：

特朗普每次发表强硬言论，市场都会快速反应。
但真正难判断的是，他这次到底会坚持到底，还是最后又会软化。
所以我做了 TACO 雷达，这是一个用 AI 分析特朗普言论、检索历史案例、估计 TACO 概率，并预测市场方向的系统。

0:30-1:30 系统演示：

这是我部署到 Streamlit Cloud 的公开网页。
我可以输入一条特朗普相关言论，然后点击 Analyze。
系统会先判断这句话的强硬度和领域，再从历史案例库中检索相似案例，最后输出 TACO 概率、置信度，以及 USO、GLD、SPY 三个资产的方向判断。

1:30-2:30 技术讲解：

这个项目主要有三层。
第一层是数据层，包括历史 TACO 案例和市场数据。
第二层是 AI 分析层，包括 Dify 知识库、RAG 检索和三个 Dify 工作流。
第三层是应用层，包括 FastAPI 后端、Streamlit 前端和 Streamlit Cloud 部署。
我还在每个 LLM 输出后加入了 Code 节点，用来清洗 JSON 和保证输出稳定。

2:30-3:00 收尾总结：

通过这个项目，我学到的不只是 Python 或 AI 工具，而是如何把一个想法做成完整产品。
我从数据处理、AI 工作流、后端、前端一直做到部署上线。
下一步我希望加入自动新闻抓取和更多历史案例，让系统可以持续追踪新的政治言论。

## 四、录制前检查清单

* [ ] 公开 URL 可以打开
* [ ] Streamlit Cloud App 已经预热
* [ ] Dify 工作流可用
* [ ] 测试言论已准备好
* [ ] 麦克风可用
* [ ] 浏览器标签页干净
* [ ] 不展示 API Key
* [ ] 不展示 .env
* [ ] 不展示 Streamlit Secrets 页面
* [ ] 视频控制在 3 分钟左右

## 五、测试言论

1. Trump threatens to impose 25% tariffs on imported goods next week.
2. Trump says he may delay the tariff plan and continue negotiations.
3. We might do something big next week.

## 六、免责声明

本项目仅用于事件影响方向性分析，不构成投资建议。
