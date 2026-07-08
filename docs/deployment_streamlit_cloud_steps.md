# TACO 第11课：Streamlit Cloud 部署步骤

用途：本文件说明如何把 TACO Radar 部署到 Streamlit Cloud。

## 一、本节课目标

把本地 TACO Radar Web App 部署到 Streamlit Cloud，获得一个公开 URL。

本地地址：

http://localhost:8501

只能自己电脑访问。

部署后公开地址类似：

https://your-taco-radar.streamlit.app

别人也可以访问。

## 二、云端架构

本地第10课架构：

Streamlit 前端
↓
FastAPI 后端
↓
Dify 工作流

第11课云端部署架构：

Streamlit Cloud
↓
Dify API
↓
Dify 三个工作流

原因：

Streamlit Cloud 上不能调用你电脑上的 http://127.0.0.1:8000/analyze。

所以云端版使用：

frontend/streamlit_cloud_app.py

直接调用 Dify Workflow API。

## 三、部署前检查

必须确认：

1. README.md 存在。
2. requirements.txt 存在。
3. .gitignore 存在。
4. .gitignore 包含 .env。
5. .gitignore 包含 .streamlit/secrets.toml。
6. GitHub 仓库中不能出现 .env。
7. GitHub 仓库中不能出现真实 secrets.toml。
8. frontend/streamlit_cloud_app.py 存在。
9. 代码中没有真实 API Key。
10. 本项目有免责声明：不构成投资建议。

## 四、requirements.txt

至少包含：

streamlit
requests
pandas
matplotlib
python-dotenv
yfinance
fastapi
uvicorn

如果云端报 ModuleNotFoundError，优先检查 requirements.txt。

## 五、推送 GitHub

参考命令：

cd D:\TACO\TACO_Project

git status
git add .
git commit -m "Prepare Streamlit Cloud deployment"
git push

注意：

推送前一定确认 .env 没有出现在 git status 待提交列表中。

如果 .env 已经被提交过，应立即重置 API Key。

## 六、Streamlit Cloud 部署

1. 打开 Streamlit Cloud。
2. 使用 GitHub 账号登录。
3. 点击 New app。
4. 选择 GitHub 仓库。
5. Branch 选择 main。
6. Main file path 填：

frontend/streamlit_cloud_app.py

7. 打开 Advanced settings。
8. 在 Secrets 中填写 Dify API Key 和 Workflow ID。
9. 点击 Deploy。
10. 等待构建完成。

## 七、Secrets 配置

在 Streamlit Cloud Secrets 中填写：

DIFY_API_KEY = "app-xxxxxxxxxxxx"
WF1_ID = "your_workflow_1_id"
WF2_ID = "your_workflow_2_id"
WF3_ID = "your_workflow_3_id"
DIFY_BASE_URL = "https://api.dify.ai"

注意：

不要把真实值写进 README。
不要截图公开显示真实 API Key。
不要把真实 secrets.toml 上传 GitHub。

## 八、线上测试

部署成功后，至少测试三条：

1. Trump threatens to impose 25% tariffs on imported goods next week.
2. Trump says he may delay the tariff plan and continue negotiations.
3. We might do something big next week.

每条都检查：

* hardness
* domain
* taco_probability
* confidence
* market_prediction
* complete JSON

## 九、常见错误

### 1. ModuleNotFoundError

原因：

requirements.txt 缺库。

解决：

补充依赖，提交 GitHub，重新部署。

### 2. KeyError: DIFY_API_KEY

原因：

Secrets 没配置或变量名拼错。

解决：

进入 Streamlit Cloud → App Settings → Secrets，检查变量名。

### 3. 仍然调用 localhost

原因：

使用了第10课本地版 frontend/streamlit_app.py。

解决：

Main file path 应使用：

frontend/streamlit_cloud_app.py

### 4. File not found

原因：

Main file path 填错。

解决：

检查仓库中是否真的有：

frontend/streamlit_cloud_app.py

### 5. API Key 泄露

处理：

立即删除公开仓库中的密钥文件，并重置 Dify API Key。
