# TACO Project

这是一个基于新闻、市场数据和 AI 的事件分析项目。

## 项目目标

1. 抓取财经新闻
2. 整理 TACO 历史案例
3. 分析市场数据
4. 使用 AI 判断言论模式
5. 制作可展示的网页应用

## 文件夹说明

- data：存放 CSV、新闻、市场数据
- notebooks：存放 Jupyter Notebook 数据分析笔记
- src：存放 Python 源代码
- app：存放网页应用代码
- docs：存放项目说明文档

## Lesson 4 - TACO Historical Case Analysis

本节课使用项目根目录下已有的 taco_cases.csv，完成案例库检查、统计分析、可视化和 RAG 案例文件生成。

运行顺序：

1. python src/lesson4/load_cases.py
2. python src/lesson4/check_cases.py
3. python src/lesson4/boxplot_taco_vs_hold.py
4. python src/lesson4/scatter_hardness_uso.py
5. python src/lesson4/domain_analysis.py
6. python src/lesson4/format_rag.py

生成文件：

* data/boxplot_taco_vs_hold.png
* data/scatter_hardness_uso.png
* data/domain_summary.csv
* data/domain_uso_bar.png
* data/rag_cases.csv

说明：

* data/rag_cases.csv 是第5课 Dify + RAG 知识库搭建的输入文件。
* 不要删除或移动 taco_cases.csv。

## Lesson 5 - Dify + RAG Knowledge Base

本节课目标：
把第4课生成的 rag_cases.csv 转换成 Dify 可上传的知识库文本文件 taco_kb.txt，并在 Dify 中完成 RAG 检索测试。

运行顺序：

1. python src/lesson5/check_rag_cases.py
2. python src/lesson5/make_kb.py
3. python src/lesson5/make_test_queries.py

生成文件：

* data/taco_kb.txt：上传到 Dify Knowledge 的知识库文件
* data/dify_test_queries.txt：Dify 检索测试用语
* docs/dify_upload_steps.md：Dify 网页端操作说明
* docs/dify_test_template.md：Dify 检索结果记录表

Dify 网页端操作：

1. 打开 Dify
2. 点击 Knowledge
3. Create Knowledge
4. 上传 data/taco_kb.txt
5. 选择 High Quality
6. 等待状态变成 Available
7. 使用 dify_test_queries.txt 中的测试言论检查 Top-3 检索结果

说明：

* 本地代码只负责准备知识库文件。
* Dify 网页端需要手动操作。
* 不要把 API Key 上传到 GitHub。
* 第6课会继续使用这个知识库搭建言论分类工作流。

## Lesson 6 - Dify Workflow 1: Statement Classifier

本节课目标：
在 Dify 中搭建第一个工作流 Statement Classifier。输入 trump_statement，输出 hardness、domain 和 reasoning。

本地准备运行顺序：

1. python src/lesson6/make_manual_test_cases.py
2. python src/lesson6/validate_code_node.py

核心文件：

* src/lesson6/classifier_prompt.txt：复制到 Dify LLM 节点
* src/lesson6/code_node.py：复制到 Dify Code 节点
* data/lesson6_manual_test_cases.txt：手动测试语句
* docs/dify_workflow1_steps.md：Dify 网页端搭建步骤
* docs/lesson6_prompt_tuning_guide.md：Prompt 调优指南
* docs/lesson6_manual_test_record.md：手动测试记录表

Dify 工作流结构：

Start → LLM → Code → End

Start 输入：

* trump_statement

End 输出：

* hardness
* domain
* reasoning

说明：

* 本地代码不包含任何真实 API Key。
* Dify 网页端需要手动搭建。
* 批量测试代码 batch_test_template.py 只作为课后模板，需要自行配置环境变量 DIFY_API_KEY 和 DIFY_WORKFLOW_URL。
* 第7课会把这个分类器输出接入 TACO 概率引擎。

## Lesson 7 - TACO Probability Engine

本节课目标：
搭建 Dify Workflow 2，把第6课输出的 hardness / domain / reasoning 接入第5课 TACO 知识库，检索相似历史案例，并输出 TACO 概率和置信度。

本地辅助文件：

* src/lesson7/format_query_prompt.txt：LLM① 格式化检索查询 Prompt
* src/lesson7/probability_prompt.txt：LLM② 概率引擎 Prompt
* src/lesson7/validate_probability_code.py：Dify Code 节点清洗代码
* src/lesson7/lesson7_test_inputs.txt：A / B / C 三组测试输入
* docs/workflow2_probability_engine_steps.md：Dify 网页端搭建步骤
* docs/workflow2_test_log.md：测试记录模板
* docs/workflow2_homework.md：第7课作业说明

Dify 网页端工作流结构：

Start
输入 hardness / domain / reasoning
↓
LLM① Format Retrieval Query
↓
Knowledge Retrieval
选择第5课 TACO 案例库，Top-K = 3
↓
LLM② Probability Engine
↓
Code Validate Probability Output
↓
End
输出 taco_probability / confidence / reasoning / key_cases

说明：

* 本地文件只用于辅助搭建 Dify 工作流。
* Dify 网页端需要手动操作。
* 不要把 Dify API Key 写进代码或上传到 GitHub。
* 第8课会继续使用这个概率结果进行市场影响预测。

## Lesson 8 - Market Impact Prediction

本节课目标：
搭建 Dify Workflow 3，把第7课输出的 taco_probability / confidence / domain 转换成 USO、GLD、SPY 的市场方向判断，并使用 yfinance 或本地 CSV 做方向对账。

本地辅助文件：

* src/lesson8/market_prompt.txt：Workflow 3 LLM 节点 Prompt
* src/lesson8/validate_market_code.py：Dify Code 节点清洗代码
* src/lesson8/lesson8_test_inputs.txt：三组测试输入
* src/lesson8/check_with_yfinance.py：yfinance 市场方向对账脚本
* src/lesson8/check_with_local_csv.py：本地 CSV 市场方向对账脚本
* src/lesson8/pipeline.py：三工作流串联演示脚本
* src/lesson8/lesson8_run_all.py：第8课运行说明
* docs/workflow3_market_predictor_steps.md：Dify 网页端搭建步骤
* docs/workflow3_test_log.md：Workflow 3 测试记录模板
* docs/market_backtest_log.md：市场方向对账记录模板
* docs/workflow3_homework.md：第8课作业说明
* .env.example：环境变量示例文件

Dify 网页端工作流结构：

Start
输入 taco_probability / confidence / domain
↓
LLM Market Reasoning
↓
Code Validate Market Output
↓
End
输出 direction_uso / direction_gld / direction_spy / key_assets / magnitude / reasoning

推荐运行：

python src/lesson8/lesson8_run_all.py
python src/lesson8/check_with_local_csv.py
python src/lesson8/check_with_yfinance.py

如果要运行三工作流串联演示：

1. 复制 .env.example 为 .env。
2. 填写自己的 Dify API Key 和三个 Workflow ID。
3. 确认 .gitignore 中包含 .env。
4. 运行：

python src/lesson8/pipeline.py

说明：

* 本地文件只用于辅助搭建 Dify 工作流。
* Dify 网页端需要手动操作。
* 不要把 Dify API Key 写进代码或上传到 GitHub。
* 本项目不是投资建议，只做事件影响方向性分析。
* 第9课会把完整分析链路封装成 FastAPI 后端接口。

## Lesson 9 - FastAPI Backend

本节课目标：
把第8课的完整 TACO 分析链路封装成 FastAPI 后端接口。

后端接口：

* GET /health：健康检查
* POST /analyze：输入 Trump 相关言论，返回完整 TACO 分析 JSON

核心文件：

* app/models.py：定义 AnalyzeRequest
* app/dify_client.py：封装 Dify 三个 Workflow 调用
* app/main.py：创建 FastAPI 应用和接口
* src/lesson9/sample_requests.json：接口测试样例
* src/lesson9/test_health.py：测试 /health
* src/lesson9/test_analyze.py：测试 /analyze
* docs/backend_fastapi_steps.md：第9课操作步骤
* docs/backend_test_log.md：测试记录模板
* docs/backend_homework.md：第9课作业说明

安装依赖：

pip install fastapi uvicorn requests python-dotenv

从项目根目录启动：

python -m uvicorn app.main:app --reload

测试地址：

http://127.0.0.1:8000/health
http://127.0.0.1:8000/docs

环境变量：

请复制 .env.example 为 .env，然后填写：

DIFY_API_KEY
WF1_ID
WF2_ID
WF3_ID

安全提醒：

* 不要把 .env 上传到 GitHub。
* 不要把 Dify API Key 写进 Python 文件。
* 不要截图公开展示 API Key。
* 本项目不是投资建议，只做事件影响方向性分析。

第10课会使用 Streamlit 前端调用 POST /analyze 接口。

## Lesson 10 - Streamlit Frontend

本节课目标：
把第9课 FastAPI 后端 POST /analyze 接入 Streamlit 前端页面，让用户可以在网页中输入 Trump 相关言论，并查看 TACO 概率和市场影响预测。

前端文件：

* frontend/streamlit_app.py：Streamlit 前端主页面
* src/lesson10/sample_statements.txt：前端测试用语
* src/lesson10/test_backend_connection.py：测试 FastAPI 后端是否在线
* src/lesson10/lesson10_run_all.py：第10课运行说明
* docs/frontend_streamlit_steps.md：Streamlit 前端操作步骤
* docs/frontend_test_log.md：前端测试记录模板
* docs/frontend_homework.md：第10课作业说明
* docs/frontend_architecture.md：前后端架构说明

安装依赖：

pip install streamlit requests matplotlib

运行方式：

终端 1：启动 FastAPI 后端

cd D:\TACO\TACO_Project
python -m uvicorn app.main:app --reload

终端 2：启动 Streamlit 前端

cd D:\TACO\TACO_Project
streamlit run frontend/streamlit_app.py

访问地址：

FastAPI 后端：
http://127.0.0.1:8000/health
http://127.0.0.1:8000/docs

Streamlit 前端：
http://localhost:8501

说明：

* 前端只调用 FastAPI 后端，不直接调用 Dify。
* 后端和前端需要同时运行。
* 不要在项目根目录创建 app.py，避免和 app/ 后端包冲突。
* 不要把 Dify API Key 写进前端代码。
* 本项目不是投资建议，只做事件影响方向性分析。

第11课会继续学习部署上线。

## Lesson 11 - Deployment with Streamlit Cloud

本节课目标：
把 TACO Radar 从本地 Streamlit App 部署到 Streamlit Cloud，获得一个公开 URL。

本地第10课架构：

Streamlit Frontend
↓
FastAPI Backend
↓
Dify Workflows

第11课云端部署架构：

Streamlit Cloud
↓
Dify Workflow API

云端主文件：

frontend/streamlit_cloud_app.py

Streamlit Cloud 配置：

* Repository：GitHub 上的 TACO 项目仓库
* Branch：main
* Main file path：frontend/streamlit_cloud_app.py
* Secrets：

  * DIFY_API_KEY
  * WF1_ID
  * WF2_ID
  * WF3_ID
  * DIFY_BASE_URL

部署前检查：

* requirements.txt 已包含 streamlit、requests、matplotlib、pandas
* .gitignore 已包含 .env
* .gitignore 已包含 .streamlit/secrets.toml
* GitHub 仓库中没有真实 API Key
* GitHub 仓库中没有 .env
* GitHub 仓库中没有真实 secrets.toml

部署步骤：

1. 推送代码到 GitHub。
2. 打开 Streamlit Cloud。
3. 创建 New app。
4. 选择 GitHub 仓库。
5. Main file path 填 frontend/streamlit_cloud_app.py。
6. 在 Secrets 中填写 Dify API Key 和 Workflow ID。
7. 点击 Deploy。
8. 获得公开 URL。
9. 使用三条测试言论完成线上测试。

测试言论：

1. Trump threatens to impose 25% tariffs on imported goods next week.
2. Trump says he may delay the tariff plan and continue negotiations.
3. We might do something big next week.

安全提醒：

* 不要把 .env 上传 GitHub。
* 不要把 .streamlit/secrets.toml 上传 GitHub。
* 不要把 Dify API Key 写进 Python 文件。
* 不要截图公开展示真实 API Key。
* 如果 API Key 曾经出现在公开仓库，应立即重置。

免责声明：

This project is for educational event-analysis purposes only and is not financial advice.

第12课会继续完成 Demo 视频录制与英文项目展示。

## Lesson 3 - Financial Data Visualization

本课目标：

* 绘制 SPY 走势图
* 绘制四资产归一化走势图
* 标注 TACO 事件
* 计算相关矩阵和热力图

运行命令：

```powershell
python src\lesson3\lesson3_run_all.py
```

输出文件：

* data/spy_trend.png
* data/four_assets_normalized.png
* data/taco_events.png
* data/correlation_heatmap.png
* data/correlation_matrix.csv

说明：

本项目仅用于事件影响方向性分析和课程学习，不构成投资建议。

## Lesson 12 - Demo Day and Portfolio

本节课目标：
完成 TACO Radar 的最终展示材料，包括 Demo 视频、项目讲解稿、Common App 活动描述、项目总结和作品集材料整理。

最终展示材料：

* docs/demo_video_script.md：3 分钟 Demo 视频脚本
* docs/presentation_pitches.md：三种听众的项目讲法
* docs/common_app_activity.txt：Common App 活动描述
* docs/final_project_summary.md：最终项目总结
* docs/demo_video_link.md：Demo 视频链接记录
* docs/project_portfolio_checklist.md：作品集材料检查清单
* docs/final_project_checklist.md：项目收官检查清单
* docs/next_steps.md：后续升级方向
* docs/lesson12_homework.md：第12课作业

Demo 视频建议结构：

1. 0:00-0:30 问题背景
2. 0:30-1:30 系统演示
3. 1:30-2:30 技术讲解
4. 2:30-3:00 收尾总结

Common App 活动描述推荐版本：

Built AI system tracking Trump statements; RAG pipeline, 20 cases, 3 Dify workflows; live on Streamlit Cloud.

项目成果：

* GitHub 仓库
* Streamlit Cloud 公开 URL
* 3 分钟 Demo 视频
* README
* Common App 活动描述
* 项目讲解稿

安全提醒：

* 不要在 Demo 视频中展示 API Key。
* 不要展示 .env。
* 不要展示 Streamlit Secrets 页面。
* 不要把真实 API Key 写进 GitHub。
* 本项目仅用于事件影响方向性分析，不构成投资建议。
